# Current support and release status

**English** | [简体中文](zh-CN/current-status.md) | [Español](es/current-status.md)

**Developer Preview · v0.5.0-alpha**  
Documentation reviewed: November 18, 2026.

## Source and release baseline

The current Windows x64 candidate is based on `1834c1a441fb444ecb1712429c550bafce7d3b19`
on `fix/windows-setup-long-paths`, plus the uncommitted Piper/setup fixes recorded in
its adjacent `verification.json`. It is a recorded dirty source snapshot, not a
claim that commit `1834c1a` alone contains every packaged fix.

The maintainer confirmed successful installation of the rebuilt EXE on November 18,
2026. The [candidate receipt](verification/windows-piper-installer-2026-11-18.md) identifies the checksum,
109 affected Python tests, 650 Flutter tests passed/15 skipped, clean analysis,
isolated installed Piper synthesis and the remaining limitations. The full Python
suite was stopped before completion; it is not reported green.

The observed `ssh -G failed` was traced to the qualification launcher's missing
Windows `ProgramData` environment variable. The same installed app passed its
authenticated SSH inspection after a corrected relaunch, and the maintainer
confirmed login works. No application files or installer were replaced for that
repair. Seven regression cases now cover system/profile environment preservation;
52 focused Windows-launch/installed/SSH checks pass.

The public preview label remains **v0.5.0-alpha**. No upload, signing or publication
was performed by this documentation update. A supplied, tested candidate and a
published download remain distinct. Existing manual images and the [earlier installed
receipt](verification/ssh-voice-installed-update-2026-11-18.md) identify their own
older source; they do not automatically certify the current candidate.

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
| Voice | Piper recommended for CPU; Kokoro selectable; optional Whisper input and separate wake downloads | Installed Piper model load/synthesis verified; microphone, playback, echo and wake require device-specific acceptance. |
| Setup | Windows installer with private runtime, versioned maintenance and optional Piper/Kokoro installation | Exact candidate installation accepted by the maintainer; signing, broad hardware and clean-machine qualification remain separate. |

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
