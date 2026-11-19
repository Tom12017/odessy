# Current support and release status

**English** | [简体中文](zh-CN/current-status.md) | [Español](es/current-status.md)

**Developer Preview · v0.5.0-alpha**  
Documentation reviewed: November 19, 2026 (November 18 release work).

## Source and release baseline

The Windows x64 draft candidate was built from committed application source `6f96e71c0d1517030bf30729546d4bb90578bdc3` on `fix/windows-setup-long-paths`. The [candidate receipt](verification/windows-piper-installer-2026-11-18.md) records the exact checksum and reused hash-verified dependency closure. Later documentation-only commits do not change its application source identity.

Final human verification of this rebuilt candidate is pending. Automated checks include 131 affected Python tests, 68 setup and management widgets, clean Flutter analysis, 107 settings contracts and a prior fresh installed Piper baseline. Final-source isolated upgrade/repair passed: installed Piper generated audio, device/model/workspace choices and user-file sentinels were preserved, and installed source hashes matched. Hosted CI passed on `6f96e71`, including full Python/desktop suites and native offline installation. The maintainer accepted the earlier November 18 installer; that acceptance remains historical and applies only to its original hash.

The observed `ssh -G failed` was traced to the qualification launcher's missing
Windows `ProgramData` environment variable. The same installed app passed its
authenticated SSH inspection after a corrected relaunch, and the maintainer
confirmed login works. No application files or installer were replaced for that
repair. Seven regression cases now cover system/profile environment preservation;
52 focused Windows-launch/installed/SSH checks pass.

The public preview label remains **v0.5.0-alpha**. The intended release is an unpublished prerelease draft for maintainer verification; it must not be published automatically. Signing and clean-machine/hardware/provider acceptance remain separate. Existing screenshots and the [earlier installed receipt](verification/ssh-voice-installed-update-2026-11-18.md) retain their original source identities.

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
| Setup | Windows installer with private runtime, versioned maintenance and optional Piper/Kokoro installation | Rebuilt draft awaits final human verification; signing, broad hardware and clean-machine qualification remain separate. |

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
