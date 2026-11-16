# Odessy

**Developer Preview · v0.5.0-alpha**

> **Unstable developer preview.** Odessy is experimental software. Expect bugs,
> breaking changes and rough edges. No stable release exists yet. See
> [support and limits](docs/current-status.md) for platform coverage and known limitations.

Hi, this is Odessy, not Odyssey! ⛵

> Curious how this started? [Read the story behind Odessy](Story.md).

Odessy is a single-user AI agent application with a Flutter desktop interface,
local or cloud model connections, policy-controlled tools and optional voice.
The model proposes actions; Odessy's service validates authority and obtains
the required approval before dispatch.

The desktop brings projects, conversations, workspace inspection, activity and
usage, device monitoring and settings into one application. This is experimental
software: expect bugs and changing interfaces, and use a disposable workspace
before granting access to important files.

[Get started](docs/getting-started.md) · [Documentation](docs/README.md) ·
[Screenshots](docs/view/README.md) · [Support and limits](docs/current-status.md) ·
[Contribute](CONTRIBUTING.md)

## Try the developer preview

For a reproducible source setup and first offline conversation, follow
[Getting started](docs/getting-started.md). It uses the production application
with an explicitly deterministic model; no paid provider, microphone, remote
computer or model download is required for that first check.

The repository also implements a Windows setup application with private runtime
components, versioned installation and maintenance. See [installed setup](docs/setup/wizard.md)
and [the installer build guide](installer/README.md). An implementation or an old
qualification receipt does not mean a matching public installer is available.
The previously published `v0.5.0-unstable` UI-client archives are historical and
do not contain the complete current preview. Do not mix them with current source.

## What you can explore

| Area | Developer-preview behavior |
| --- | --- |
| Conversations | Projects, saved history, search, export, rename, pin and archive. Custom supports bounded restart continuation; Harness history is read-only after restart. |
| Tools and permissions | Reviewed actions, explicit approvals, cancellation and supported Custom access modes. Full control never overrides hard denials or expands an existing grant. |
| Workspace panels | Scoped file reads, proposed diffs and recorded command output. Output is distinct from an interactive terminal. |
| Context | Explicit project memory and opt-in local document retrieval, with source citations and bounded Custom context preparation. |
| Local terminal | Conditional Windows PTY support when the verified native helper closure is available; requires an explicit shell grant. No SSH terminal. |
| Devices | Opt-in read-only monitoring through existing paired or SSH connections. SSH authentication does not grant execution or workspace access. |
| Voice and settings | Existing voice and model configuration, eight settings groups and local appearance preferences. Physical audio and provider behavior need separate validation. |

Checkpoint creation, listing and preview remain available on Windows, but
**checkpoint restoration is disabled on Windows** until directory-handle safety
is implemented. The backend refuses direct restore requests; the desktop explains
the restriction. Supported non-Windows restoration still requires exact approval. See [terminal and checkpoint limits](docs/ui/terminal-checkpoints.md).

## Platform scope

Windows x64 is the primary development and recorded native-test platform. Linux
has source/CI coverage and scoped historical device evidence; that is not full
desktop/package parity. macOS is unqualified. Hardware requirements have not been
established. Read the [support matrix](docs/current-status.md) before choosing a deployment.

## Security and privacy

Python owns policy and authorization; Node owns existing MCP tool execution;
Rust owns paired identity/transport; Go aggregates optional telemetry; Flutter
uses typed clients. Selecting a cloud model sends request data to that provider.
Redaction is best-effort, not a guarantee against disclosure.

An approved interactive shell runs with the user's OS permissions and is not a
per-command workspace sandbox. Legacy plaintext LAN execution is unsuitable for
untrusted networks. Prefer the documented authenticated transport paths.
Report vulnerabilities privately through [SECURITY.md](SECURITY.md).

## Build Odessy with us

We're a small team of two regular contributors, with three others helping out
on a short-term basis, and we'd love some company. Whether you'd like to fix a
bug, improve a component or work with us on a larger part of Odessy, you're welcome.

Some areas we'd love help with:

- **AI agents:** orchestration, tool calling, model integration and memory.
- **Hardware exploration:** Jetson, Raspberry Pi, BLE and MCU communication.
  These are areas of interest, not claims of current device support.
- **Systems:** Rust, networking, mTLS and secure execution.
- **Desktop:** Flutter, Dart, accessibility and UI/UX.
- **Infrastructure:** Go, monitoring, telemetry and multi-host management.
- **Voice:** STT, TTS, wake-word detection and audio processing.

Documentation, compatibility tests and reproducible bug reports are welcome too.
Odessy is an independent, volunteer-driven project. Contributions are unpaid,
and there's no fixed time commitment: help when you can.

Start with [Contributing](CONTRIBUTING.md), explore the
[architecture](docs/ARCHITECTURE.md), browse
[open issues](https://github.com/Trisoma/odessy/issues), or suggest an idea.
For larger changes, discuss the approach with us before starting.
AI-assisted contributions are welcome; contributors remain responsible for review,
testing and attribution.

Odessy is licensed under [Apache-2.0](LICENSE). Bundled components and model assets
have their own terms; see [third-party notices](THIRD-PARTY-NOTICES.md) and
[the license inventory](docs/reference/third-party-licenses.md).
