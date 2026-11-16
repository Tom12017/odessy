"""Ollama chat adapter with native tools, thinking and generation diagnostics.

Accepts any Ollama model name and falls back to structured text when the server
reports that tools are unsupported. Shared parsing and authority contracts live
in ollama_model and the runtime.
"""

from __future__ import annotations

import os
import time
from dataclasses import dataclass, field
from typing import Any

from odessy.tools.tool_contracts import build_openai_tools
from odessy.models.ollama_model import (
    _OllamaToolsUnsupported,
    _elapsed_ms,
    _add_diagnostic_ms,
    _add_tokens,
    _corrected_tool_request,
    _debug_model_repair,
    _debug_parsed_action,
    _default_call_timeout,
    _default_num_ctx,
    _default_num_predict,
    _default_progress_timeout,
    _extract_model_action_from_chat,
    _fallback_observation_response,
    _follow_up_tools,
    _history_messages,
    _observation_messages,
    _remember_observation,
    _start_turn_with_context,
    _strip_thinking,
    _looks_like_generic_final_response,
    _model_output_error,
    _repair_prompt,
    _system_prompt,
    _text_system_prompt,
    _request_ollama_chat,
)
from odessy.runtime.types import FinalResponse, ModelAction, ModelTurnDiagnostics, ToolObservation

from . import DEFAULT_CHAT_MODEL, DEFAULT_LOCAL_ENDPOINT

DEFAULT_CHAT_ENDPOINT = os.environ.get("ODESSY_MODEL_ENDPOINT", DEFAULT_LOCAL_ENDPOINT)


def normalize_ollama_chat_response(data: dict[str, Any]) -> dict[str, Any]:
    """Return the Ollama ``/api/chat`` response shape used by shared parsers."""
    message = data.get("message") or {}
    normalized = {
        "message": {
            "role": message.get("role", "assistant"),
            "content": message.get("content") or "",
            "tool_calls": message.get("tool_calls") or [],
        }
    }
    if "thinking" in message:
        normalized["message"]["thinking"] = message.get("thinking")
    for key in (
        "total_duration",
        "load_duration",
        "prompt_eval_duration",
        "prompt_eval_count",
        "eval_duration",
        "eval_count",
        "thinking",
        "thinking_token_count",
        "thinking_tokens",
    ):
        if key in data:
            normalized[key] = data[key]
    return normalized


@dataclass(frozen=True)
class OllamaChatModel:
    """Configurable Ollama chat model using the shared ModelAdapter protocol."""

    model: str = DEFAULT_CHAT_MODEL
    endpoint: str = DEFAULT_CHAT_ENDPOINT
    #: Seconds of allowed silence between streamed chunks. Not a total budget.
    timeout: int = field(default_factory=_default_progress_timeout)
    temperature: float = 0.0
    think: bool | str | None = None
    #: Tokens one call may generate, including thinking tokens.
    num_predict: int = field(default_factory=_default_num_predict)
    #: Context window; prompt plus ``num_predict`` has to fit inside it.
    num_ctx: int = field(default_factory=_default_num_ctx)
    #: Stream wall-time budget checked between lines; includes silence, excludes
    #: connection/header waits, and can overrun during a blocking read.
    call_timeout: float = field(default_factory=_default_call_timeout)
    keep_alive: int | None = None
    conversation_context: tuple = ()

    @property
    def last_turn_diagnostics(self) -> ModelTurnDiagnostics:
        diagnostics = getattr(self, "_last_turn_diagnostics", None)
        if isinstance(diagnostics, ModelTurnDiagnostics):
            return diagnostics
        return ModelTurnDiagnostics()

    def propose(self, user_text: str, *, context: Any = None) -> ModelAction:
        diagnostics = ModelTurnDiagnostics()
        object.__setattr__(self, "_last_turn_diagnostics", diagnostics)
        _start_turn_with_context(self, context)
        try:
            action = self._chat_native_action(user_text, diagnostics)
        except ValueError as error:
            diagnostics.proposal_valid = False
            diagnostics.repair_triggered = True
            model_error = _model_output_error("", error, user_text)
            repair_prompt = _repair_prompt(user_text, model_error)
            _debug_model_repair(
                [
                    ("first model proposal", "invalid structured output"),
                    ("validation failure", model_error.validation_error),
                    ("repair prompt", repair_prompt),
                ]
            )
            try:
                action = self._chat_text_action(
                    user_text,
                    repair_prompt,
                    diagnostics,
                    generation_field="repair_generation_ms",
                )
            except ValueError as retry_error:
                raise ValueError(
                    f"Model repair failed after one retry: {retry_error}"
                ) from retry_error
            _debug_model_repair([("second model proposal", "repaired structured output")])
        _debug_parsed_action(action)
        return action

    def _chat_text_action(
        self,
        user_text: str,
        prompt: str,
        diagnostics: ModelTurnDiagnostics,
        *,
        generation_field: str = "proposal_generation_ms",
    ) -> ModelAction:
        started = time.perf_counter()
        _record_model_call_attempt(diagnostics)
        response = self._chat([{"role": "user", "content": prompt}])
        _add_diagnostic_ms(diagnostics, generation_field, _elapsed_ms(started))
        _record_ollama_response(diagnostics, response)
        parse_started = time.perf_counter()
        try:
            return _extract_model_action_from_chat(response, user_text)
        finally:
            if generation_field == "proposal_generation_ms":
                _add_diagnostic_ms(
                    diagnostics,
                    "proposal_parsing_ms",
                    _elapsed_ms(parse_started),
                )

    def _chat_native_action(
        self,
        user_text: str,
        diagnostics: ModelTurnDiagnostics,
    ) -> ModelAction:
        messages = [
            {"role": "system", "content": _system_prompt()},
            *_history_messages(self),
            {"role": "user", "content": user_text},
        ]
        try:
            started = time.perf_counter()
            _record_model_call_attempt(diagnostics)
            response = self._chat(messages, tools=build_openai_tools())
            _add_diagnostic_ms(diagnostics, "proposal_generation_ms", _elapsed_ms(started))
            _record_ollama_response(diagnostics, response)
        except _OllamaToolsUnsupported:
            return self._chat_text_action(
                user_text,
                _text_system_prompt(user_text),
                diagnostics,
            )
        parse_started = time.perf_counter()
        try:
            return _extract_native_action_from_chat(response, user_text)
        finally:
            _add_diagnostic_ms(
                diagnostics,
                "proposal_parsing_ms",
                _elapsed_ms(parse_started),
            )

    def _chat(
        self,
        messages: list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        return normalize_ollama_chat_response(
            _request_ollama_chat(self, messages, tools)
        )

    def finalize_observations(self, observations) -> None:
        for observation in observations:
            _remember_observation(self, observation)

    def respond_to_observations(self, user_text, observations) -> ModelAction:
        for observation in observations[:-1]:
            _remember_observation(self, observation)
        return self.respond_to_observation(user_text, observations[-1])

    def respond_to_observation(
        self,
        user_text: str,
        observation: ToolObservation,
    ) -> ModelAction:
        diagnostics = self.last_turn_diagnostics
        started = time.perf_counter()
        _record_model_call_attempt(diagnostics)
        response = self._chat(
            _observation_messages(user_text, _remember_observation(self, observation)),
            tools=_follow_up_tools(),
        )
        diagnostics.final_generation_ms = _elapsed_ms(started)
        _record_ollama_response(diagnostics, response)
        object.__setattr__(self, "_last_turn_diagnostics", diagnostics)
        corrected = _corrected_tool_request(response, user_text)
        if corrected is not None:
            return corrected
        text = _strip_thinking((response.get("message") or {}).get("content") or "")
        if text and not _looks_like_generic_final_response(text):
            return FinalResponse(text=text)
        return FinalResponse(text=_fallback_observation_response(observation))


def _extract_native_action_from_chat(response: dict[str, Any], user_text: str) -> ModelAction:
    message = response.get("message") or {}
    if message.get("tool_calls"):
        return _extract_model_action_from_chat(response, user_text)
    content = _strip_thinking(message.get("content") or "")
    if not content:
        # Includes content that was only unfinished reasoning: there is no answer to
        # give, so the repair path asks again.
        raise ValueError("Ollama returned neither a tool call nor content")
    if content.startswith("{") or content.startswith("```"):
        return _extract_model_action_from_chat(response, user_text)
    return FinalResponse(text=content)


def _record_model_call_attempt(diagnostics: ModelTurnDiagnostics) -> None:
    diagnostics.model_call_count += 1


def _record_ollama_response(
    diagnostics: ModelTurnDiagnostics,
    response: dict[str, Any],
) -> None:
    _add_duration_ms(diagnostics, "model_total_duration_ms", response.get("total_duration"))
    _add_duration_ms(diagnostics, "model_load_duration_ms", response.get("load_duration"))
    _add_duration_ms(
        diagnostics,
        "prompt_eval_duration_ms",
        response.get("prompt_eval_duration"),
    )
    _add_duration_ms(diagnostics, "eval_duration_ms", response.get("eval_duration"))
    _add_tokens(diagnostics, "prompt_tokens", response.get("prompt_eval_count"))
    _add_tokens(diagnostics, "completion_tokens", response.get("eval_count"))
    _add_tokens(diagnostics, "prompt_eval_count", response.get("prompt_eval_count"))
    _add_tokens(diagnostics, "eval_count", response.get("eval_count"))

    message = response.get("message") or {}
    content = message.get("content")
    if isinstance(content, str):
        diagnostics.response_chars += len(content)
    thinking = message.get("thinking", response.get("thinking"))
    if isinstance(thinking, str):
        diagnostics.thinking_exposed = True
        diagnostics.thinking_chars += len(thinking)

    thinking_tokens = response.get("thinking_token_count")
    if thinking_tokens is None:
        thinking_tokens = response.get("thinking_tokens")
    if thinking_tokens is None:
        thinking_tokens = message.get("thinking_token_count")
    _add_tokens(diagnostics, "thinking_token_count", thinking_tokens)

    if diagnostics.eval_duration_ms and diagnostics.eval_count is not None:
        diagnostics.generation_tokens_per_sec = diagnostics.eval_count / (
            diagnostics.eval_duration_ms / 1000.0
        )


def _add_duration_ms(
    diagnostics: ModelTurnDiagnostics,
    field_name: str,
    value: Any,
) -> None:
    if not isinstance(value, (int, float)):
        return
    value_ms = float(value) / 1_000_000.0
    current = getattr(diagnostics, field_name)
    setattr(
        diagnostics,
        field_name,
        value_ms if current is None else current + value_ms,
    )
