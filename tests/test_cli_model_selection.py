from __future__ import annotations

import io
import json

import pytest

from odessy.models import build_local_model
from odessy.runtime.types import FinalResponse

from odessy.cli import _build_model
from odessy.models.fake_model import FakeModel
from odessy.models.ollama_chat import OllamaChatModel
from odessy.models.ollama_model import OllamaModel


def test_text_mode_defaults_to_lfm_model() -> None:
    model = _build_model(False, ollama_model="gemma3:1b")

    assert isinstance(model, OllamaChatModel)
    assert model.model == "lfm2.5-thinking:1.2b-q8_0"


def test_legacy_gemma_switch_remains_available() -> None:
    model = _build_model(False, backend="ollama", ollama_model="gemma3:1b")

    assert isinstance(model, OllamaModel)
    assert model.model == "gemma3:1b"


def test_legacy_fake_model_switch_remains_available() -> None:
    model = _build_model(True, ollama_model="gemma3:1b")

    assert isinstance(model, FakeModel)


def test_explicit_model_is_announced_to_stderr(capsys) -> None:
    from odessy.cli import _announce_model

    _announce_model(OllamaChatModel(model="odessy-lfm-q8:jetson"))
    output = capsys.readouterr()
    assert "odessy-lfm-q8:jetson" in output.err
    assert "backend=lfm" in output.err
    assert output.out == ""


@pytest.mark.parametrize("backend", ["ollama", "lfm", "llama_cpp"])
def test_arbitrary_model_reaches_ollama_without_family_substitution(backend, monkeypatch):
    requests = []

    def respond(request, timeout):
        requests.append((request.full_url, json.loads(request.data)))
        return io.BytesIO(json.dumps({
            "message": {"role": "assistant", "content": '{"type":"final","text":"Ready"}'},
            "done": True,
        }).encode() + b"\n")

    monkeypatch.setattr("urllib.request.urlopen", respond)
    model = build_local_model(
        backend, model="my-custom-model:latest",
        endpoint="http://127.0.0.1:9123", num_predict=384,
    )
    assert model.propose("Hello") == FinalResponse(text="Ready")
    url, payload = requests[0]
    assert url == "http://127.0.0.1:9123/api/chat"
    assert payload["model"] == "my-custom-model:latest"
    assert payload["options"]["num_predict"] == 384


def test_unknown_local_backend_is_rejected():
    with pytest.raises(ValueError, match="Unknown local model backend"):
        build_local_model("unknown", model="my-custom-model")
