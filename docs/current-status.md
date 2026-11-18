# Current support and release status

**Developer Preview · v0.5.0-alpha**  
Documentation reviewed: November 18, 2026.

## Source and release baseline

This review uses local `develop` at `1a50944ca717f9b5590063bdf1a7566054cf90be`
after PR #68, before the contributor/manual and translation documentation commits.
Runtime metadata and source functionality are separate from those documentation edits.

The [November 18 installed receipt](verification/ssh-voice-installed-update-2026-11-18.md)
identifies the upgraded Windows candidate built from `7f3b925`, with preservation,
component checks and their limits. It does not qualify every later merged revision.
The manual's real SSH captures identify that installed executable; gallery fixtures
and deterministic service tests remain separately labeled.

The intended next public label is **v0.5.0-alpha**, not beta. A matching full installer
is not on the public release page as of this review; `v0.5.0-unstable` archives are an
older UI-client snapshot. A functioning supplied/local installer is different from
a published download. No publication, signing or clean-machine qualification is
implied by this page. Earlier PR #67 CI/review receipts retain their own scope and
cannot certify the current head automatically.

## First contributor run

The normal installed workflow is **open app → Settings → model/workspace → chat**.
The desktop starts its authenticated service; no user-operated backend terminal is
needed. [Source setup](getting-started.md) uses the same managed lifecycle after
installing development SDKs. The CLI fake model and manual token handshake are
separate component/API checks, not the product's main onboarding route.

[Open GitHub issues](https://github.com/Trisoma/odessy/issues) and the [path to area ownership](../CONTRIBUTING.md#path-to-area-ownership)
give concrete contribution routes. They do not prove external onboarding success,
maintainer response times or a contributor permission grant. First-run timing and
an external reader's golden-path acceptance remain unmeasured.

## Capability matrix

| Capability | Implemented scope | Important boundary |
| --- | --- | --- |
| Desktop | Production Flutter shell, projects/recent chats, inspector, Activity & usage, Jobs, Handoffs and eight settings groups | A visible page does not guarantee that its backend capability is available. |
| Durable history | Profile-local SQLite projects/conversations/events, search and bounded export | History browsing has no side effects; stored calls are not replayed. |
| Custom continuation | Restores completed public exchanges into a fresh authorized controller | Workspace binding must match; grants, approvals, jobs and process handles are not restored. |
| Harness | Selectable runtime and saved readable history | Restart continuation and Custom access-mode/context parity are unavailable; no silent fallback. |
| Access modes | Custom ask/auto/full with service acknowledgments and revisions | Existing policy, hard denials, sensitive paths and independent grants remain effective. |
| Context/memory/retrieval | Explicit project facts, opt-in bounded lexical indexing and Custom context/citations | Source validation and current live workspace authority remain required. No automatic cloud indexing. |
| Interactive terminal | Local Windows PTY with verified packaged Node/native helper and explicit grant | Runs with user OS permissions; no remote PTY, restored handles or replayed input. Missing closure means unavailable. |
| Checkpoints | Git-backed bounded text snapshots and preview; supported non-Windows restoration uses exact approval and a safety snapshot | Windows restoration is disabled in the service and UI pending handle-based safety. Creation/list/preview remain available; binary/sensitive/unsupported files are excluded. |
| Monitoring | Optional Go aggregation with local/paired telemetry and read-only SSH status | Connectivity, permission and freshness remain separate. Monitoring DTOs grant no execution or workspace access. |
| SSH execution | Explicit temporary Custom target selection and exactly approved `ssh.run` commands | Separate from monitoring; no remote sandbox, PTY, file inspector or Harness SSH execution. Reconnect after service restart. |
| Voice | Existing provider/controller lifecycle and scoped prior audio evidence | Microphone, echo, model assets and device/provider compatibility require their own checks. |
| Setup | Windows Flutter setup, private runtime closure and versioned maintenance | Final merged source has not been qualified as one new coherent installed release candidate. |

## Platform matrix

| Platform | Evidence and support level |
| --- | --- |
| Windows x64 | Primary developer-preview target; source/CI and recorded native/installed checks exist for specific snapshots. Final candidate qualification remains separate. |
| Linux x86_64 | Source/CI coverage; portable packaging and native GUI acceptance are not established for the final snapshot. |
| Jetson/Linux ARM64 | Direction-specific historical monitoring, pairing and voice evidence only. Not a blanket desktop or execution claim. |
| macOS | Unqualified. |

No general minimum RAM/GPU specification, complete sandbox, autonomous coordination
parity or MCU support is claimed. SSH command execution has the bounded Custom scope
above; it is not a general remote IDE or confinement guarantee.

## Gates before a beta claim

1. Keep Windows checkpoint restoration disabled in the release candidate until
   handle-based protection is verified. Resolve or disable any other safety/data-loss findings.
2. Build and audit one coherent candidate from the final source snapshot with
   pinned runtime/helper closure, licenses and artifact hashes.
3. Verify isolated install/update/uninstall and profile/history/settings preservation
   against that candidate; distinguish fixtures from real vault/provider evidence.
4. Match onboarding, supported workflows, screenshots and limitations to the candidate.
5. Record maintainer visual acceptance and remaining platform/hardware/provider gates.

Alpha does not waive safety requirements. Do not distribute an unsafe restore
path as production-safe. See [release verification](release-verification.md).
