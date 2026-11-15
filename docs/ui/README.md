# Desktop guide

**Developer Preview · v0.5.0-alpha**

The production Flutter entry point is `apps/desktop/lib/main.dart` (`OdessyApp`).
Use [Getting started](../getting-started.md) for a connected local run and the
[screen gallery](../view/README.md) for the visual reference.

## Navigation

The project/chat sidebar contains Odessy, New chat, Projects with nested chats,
and Recent. The outer navigation keeps Activity & usage, Devices, Workspaces,
Jobs, Handoffs and Settings reachable. Tools and installation management belong
in Settings, not as additional project-sidebar sections. Inspector panels keep
advanced details out of the conversation/composer.

## Conversations and workspace panels

Select the correct project, workspace and model profile before sending a turn.
Switching panels must preserve drafts and voice/model state. Saved history is
separate from live sessions: Custom can continue a compatible saved conversation
in a fresh controller, while Harness restart history is read-only.

The inspector provides files, proposed diffs, recorded Output, used context,
project memory, documents/citations, and available terminal/checkpoint controls.
Viewing history, a file, a diff or Output grants no write or shell permission.
Read [history](conversation-history.md), [context](context-memory-retrieval.md)
and [terminal/checkpoint limits](terminal-checkpoints.md) before enabling effects.

## Settings

All eight groups remain available: General, Models and connections, Speech to
text, Text to speech, Voice, Devices and tool access, Advanced, and Installation.
Appearance preferences are local frontend state; runtime/model configuration is
service-owned. Save/Cancel/Reload, dirty drafts, stale revisions and errors must
reflect actual acknowledgments. Unsupported controls remain visibly unavailable.

## Connection and launch modes

- Normal `main.dart`: production client; disconnected until a service is connected
  or a supported owned-service launch path succeeds.
- Production `--demo`: explicitly labeled fixture mode, not live-service evidence.
- `lib/tastecode_demo.dart`: isolated design demo, not the production application.
- `--setup`, `--manage`, `--installed`: packaged lifecycle entry points documented
  in [the setup guide](../setup/wizard.md); do not handcraft installed paths.

A checkout-specific native build may depend on a local Python environment and
cached helpers. Its executable is not a portable installer. Build the normal
entry with `flutter build windows --release` from `apps/desktop` and keep its
DLLs/data beside it. Do not infer source identity from an old executable.

## Contributor checks

From `apps/desktop`, run `dart format --output=none --set-exit-if-changed lib test`,
`flutter analyze` and `flutter test`. From the repository root run
`python tool/check_desktop_contracts.py`. Use `--no-pub` only with a valid resolved
cache; tests/analysis are not installed or hardware acceptance.

The maintained screenshot set is exclusively under `docs/view/`; old UI screenshot sets are removed.

See [architecture](architecture.md), [API contracts](api-contract.md),
[design](design.md), [access modes](access-modes.md) and
[settings draft lifecycle](settings-draft-lifecycle.md). Read nested contributor
instructions before editing shared foundation.
