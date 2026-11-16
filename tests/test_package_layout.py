"""Canonical domain packages preserve repository resource paths."""

import importlib
from pathlib import Path

import pytest


GROUPS = {
    "runtime": "agent_loop types repeat_guard tool_timeout memory",
    "models": "cloud_model ollama_model ollama_chat fake_model",
    "tools": "calculator mcp_server external_tools node_mcp tool_contracts",
    "authority": "policy workspace_authority command_bridge redaction output_retention spill",
    "config": "config_file deployment doctor",
}


@pytest.mark.parametrize(
    "group,name",
    [(group, name) for group, names in GROUPS.items() for name in names.split()],
)
def test_canonical_modules_live_in_their_domain_package(group: str, name: str) -> None:
    module = importlib.import_module(f"odessy.{group}.{name}")
    assert Path(module.__file__).parent.name == group


def test_repository_resources_survive_the_move() -> None:
    from odessy.config.config_file import default_config_file
    from odessy.tools.node_mcp import _public_repo_root

    root = Path(__file__).resolve().parents[1]
    assert default_config_file() == root / "config" / "odessy.env"
    assert _public_repo_root() == root
