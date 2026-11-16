# Changelog

User-visible changes are recorded here, starting with the next release.

## Unreleased — v0.5.0-alpha (Developer Preview)

- Consolidate the production desktop with project/recent navigation, preserved Activity & usage, Jobs/Handoffs, inspector panels and local appearance preferences.
- Add durable conversation/project history, search/export and bounded Custom restart continuation; Harness restart history remains read-only.
- Add service-owned Custom access modes, explicit project memory and opt-in lexical document retrieval.
- Add conditional local Windows PTY integration and Git text checkpoints.
- Disable checkpoint restoration on Windows at the service/write boundary pending directory-handle safety; retain creation/list/preview and show the restriction in the desktop.
- Refresh user/developer documentation and distinguish current capabilities from historical release/qualification evidence.

- Add trusted SSH targets with read-only monitoring; SSH execution and workspace capabilities remain disabled.

- Keep Harness available after repair and upgrade, and reject incomplete Windows installers.
- Prevent repeated streamed voice replies and reset timing correctly for follow-up recordings.
- Preserve unsaved API keys on status refresh and wait for credential saves before leaving setup.
