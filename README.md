# Odessy

**English** | [简体中文](README.zh-CN.md) | [Español](README.es.md)

**Developer Preview · v0.5.0-alpha**

> **Unstable developer preview.** Odessy is experimental software. Expect bugs,
> breaking changes and rough edges. No stable release exists yet. See
> [support and limits](docs/current-status.md) for platform coverage and known limitations.

Hi, this is Odessy, not Odyssey! ⛵

> Curious how this started? [Read the story behind Odessy](Story.md).

Odessy is building toward a **voice-first personal agent**: one desktop coordinates
local or cloud models and reviewed work on your laptop or a connected Linux computer.
The long-term inspiration is JARVIS/FRIDAY; today's product is an experimental
Windows-first app, with typed chat available while you configure voice.

**The model proposes; Odessy's policy layer decides.** The service validates actions,
obtains required human approval and rechecks authority before tool dispatch.

**We are looking for 3–5 developer collaborators** who want to run a real workflow,
report what breaks and take on a bounded area. Start with the [desktop manual](docs/GOLDEN_PATH.md),
choose an [open GitHub issue](https://github.com/Trisoma/odessy/issues), and read the [contribution and ownership path](CONTRIBUTING.md#path-to-area-ownership).

[Run from source](docs/getting-started.md) · [Architecture](docs/ARCHITECTURE.md) ·
[Screenshots](docs/view/README.md) · [Support and limits](docs/current-status.md)

## Architectural bets

- **Policy owns authority.** Model output is a proposal. Python owns policy and approvals;
  tool adapters revalidate at dispatch. A chat message or connected device grants no rights.
- **One coordinator, separate execution targets.** Keep the model on the laptop or a chosen
  provider; select local, authenticated paired, or explicitly approved SSH execution.
  The SSH computer needs no model. Edge/LAN integration has narrower experimental scope,
  and MCU/home automation remains a direction for contribution, not implemented support.
- **Voice is an intended primary interface.** STT, TTS and wake listening share the agent
  lifecycle and authority boundaries with typed input. Speech setup, latency and hardware
  compatibility still need work; spoken approval is not identity authentication.

These are design choices to develop and test, not claims that other agents lack approvals,
that every provider is local, or that Odessy is a complete sandbox.

## Try the developer preview

The normal experience is **open Odessy → configure a model in Settings → choose a
workspace → chat and review actions**. The desktop owns backend startup and local
authentication. Users do not manually run Python or exchange bearer tokens.

- **Have a full candidate?** Follow the [illustrated manual](docs/GOLDEN_PATH.md).
  The Windows setup includes its supported runtime and versioned maintenance.
- **Building from source?** Follow [Getting started](docs/getting-started.md).
  Its desktop-managed mode uses the same configured-service lifecycle, after installing
  the developer SDKs. Manual server and fake-model commands are separate contributor checks.

A full Windows x64 installer is prepared for an **unpublished verification draft**. It offers **Piper (recommended for CPU)** or **Kokoro**, optional verified speech downloads and a separate wake-word choice. Follow the [installer steps and checksum](docs/GOLDEN_PATH.md#1-install-and-open-odessy). The maintainer must verify this rebuilt candidate before deciding to publish it; acceptance of the earlier November 18 installer applies only to that earlier file. Obtain the exact candidate from the maintainer, or use source. Public files will appear on the [release page](https://github.com/Trisoma/odessy/releases) only after publication. Older `v0.5.0-unstable` UI archives are not equivalent. See the [candidate receipt](docs/verification/windows-piper-installer-2026-11-18.md).

## What you can explore

| Area | Developer-preview behavior |
| --- | --- |
| Conversations | Projects, saved history, search, export, rename, pin and archive. Custom supports bounded restart continuation; Harness history is read-only after restart. |
| Tools and permissions | Reviewed actions, explicit approvals, cancellation and supported Custom access modes. Full control never overrides hard denials or expands an existing grant. |
| Workspace panels | Scoped file reads, proposed diffs and recorded command output. Output is distinct from an interactive terminal. |
| Context | Explicit project memory and opt-in local document retrieval, with source citations and bounded Custom context preparation. |
| Local terminal | Conditional Windows PTY support when the verified native helper closure is available; requires an explicit shell grant. No SSH terminal. |
| Devices and SSH | Read-only monitoring plus separately selected Custom SSH commands, each requiring exact approval. Login alone grants no execution or workspace access; experimental LAN is a separate path. |
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
We are seeking collaborators who can take a focused task through reproduction,
implementation and review. Reproductions, tests and documentation are useful first contributions.

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

Start with [Piper diagnostics](https://github.com/Trisoma/odessy/issues/69),
[SSH connection status](https://github.com/Trisoma/odessy/issues/70),
[TTS benchmark summaries](https://github.com/Trisoma/odessy/issues/71), or
[recorded-output UX](https://github.com/Trisoma/odessy/issues/72). Each GitHub issue
contains scope, acceptance criteria and test commands. Comment on the issue to coordinate before starting.

Start with [Contributing](CONTRIBUTING.md), explore the
[architecture](docs/ARCHITECTURE.md), browse
[open issues](https://github.com/Trisoma/odessy/issues), or suggest an idea.
For larger changes, discuss the approach with us before starting.
AI-assisted contributions are welcome; contributors remain responsible for review,
testing and attribution.

Odessy is licensed under [Apache-2.0](LICENSE). Bundled components and model assets
have their own terms; see [third-party notices](THIRD-PARTY-NOTICES.md) and
[the license inventory](docs/reference/third-party-licenses.md).
