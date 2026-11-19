# Odessy documentation

**English** | [简体中文](zh-CN/README.md) | [Español](es/README.md)

**Developer Preview · v0.5.0-alpha**

Start with the guide for your task. The [current support matrix](current-status.md)
defines implemented behavior, unavailable capabilities and outstanding release gates.
Historical plans and test receipts describe their recorded snapshots, not today's support.

The [Windows draft candidate](verification/windows-piper-installer-2026-11-18.md) includes optional Piper/Kokoro setup. The [manual](GOLDEN_PATH.md) identifies its checksum and installation steps. Final maintainer verification and publication are pending; older installer acceptance applies to its original checksum.

| Task | Guide |
| --- | --- |
| Run the app and verify a local action | [Desktop manual](GOLDEN_PATH.md) · [Managed source launch](getting-started.md) |
| Install or manage a packaged candidate | [Setup wizard](setup/wizard.md) · [Installer](../installer/README.md) |
| Configure a model or credentials | [Headless setup](setup/headless.md) · [Cloud models](reference/cloud-models.mdx) · [Credentials](setup/secure-model-credentials.md) |
| Use the desktop | [Desktop guide](ui/README.md) · [Screen gallery](view/README.md) |
| Understand saved chats and SQLite | [Conversation history](ui/conversation-history.md) · [Database guide](database/README.md) |
| Understand tool authority | [Access modes](ui/access-modes.md) · [Permissions](reference/permissions.mdx) · [Security limits](reference/current-limitations.mdx) |
| Use memory and documents | [Context, memory and retrieval](ui/context-memory-retrieval.md) |
| Use local terminal or checkpoints | [Capabilities and safety limits](ui/terminal-checkpoints.md) |
| Connect computers | [SSH setup](setup/ssh-computers.md) · [Experimental executor](setup/executor-preview.md) · [Host pairing](reference/host-pairing.mdx) |
| Inspect telemetry | [Monitoring](monitoring/README.md) · [Monitoring API](monitoring/api.md) |
| Work on voice | [Desktop voice](ui/desktop-voice.md) · [Providers](reference/speech-providers.md) |
| Contribute and grow into an area | [Open GitHub issues](https://github.com/Trisoma/odessy/issues) · [Contribution/ownership path](../CONTRIBUTING.md#path-to-area-ownership) · [Architecture](ARCHITECTURE.md) |
| Prepare a release | [Alpha preview scope](releases/v0.5.0-alpha.md) · [Release verification](release-verification.md) |

## Reading evidence correctly

Source tests, hosted CI, native builds, installed acceptance, real-provider checks
and hardware checks answer different questions. A screenshot is design evidence;
it does not prove that a feature is available on every engine or installed package.
Never infer tool execution authority from device connectivity or project metadata.
