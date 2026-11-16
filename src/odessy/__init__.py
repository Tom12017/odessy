"""Odessy command-line agent runtime.

``__version__`` is the single source of truth for the runtime version. Anything
that needs to stamp a version -- benchmark metadata in particular -- must read it
from here rather than repeat the literal, which is how the version previously
drifted out of step with ``pyproject.toml`` and the README.

Package metadata in ``pyproject.toml`` must match this value. Preparing a version
does not publish a release or create a Git tag.
"""

__version__ = "0.5.0.dev0"

__all__ = ["runtime", "models", "tools", "authority", "config", "voice"]
