"""Local-model presets shared by configuration, diagnostics and adapters.

Names are defaults for existing installations. Every adapter accepts a configured
model name independently of the model family.
"""

DEFAULT_LOCAL_ENDPOINT = "http://127.0.0.1:11434"
DEFAULT_CHAT_MODEL = "lfm2.5-thinking:1.2b-q8_0"
DEFAULT_FAST_MODEL = "gemma3:1b"


def build_local_model(backend, *, model=None, endpoint=None, **options):
    if backend == "ollama":
        from .ollama_model import OllamaModel
        adapter = OllamaModel
        default_model = DEFAULT_FAST_MODEL
    elif backend in ("lfm", "llama_cpp"):
        from .ollama_chat import OllamaChatModel
        adapter = OllamaChatModel
        default_model = DEFAULT_CHAT_MODEL
    else:
        raise ValueError(f"Unknown local model backend: {backend}")
    if endpoint is not None:
        options["endpoint"] = endpoint
    return adapter(model=default_model if model is None else model, **options)
