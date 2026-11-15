# Current support and release status

**Developer Preview · v0.5.0-alpha**  
Documentation reviewed: November 15, 2026.

## Source and release baseline

This documentation targets the implementation merged by [PR #67](https://github.com/Trisoma/odessy/pull/67)
into `develop` at `3a52fcc69efe750c5f97526920c8bbc757bb65f6`.
The reviewed feature tip was `b89361b58b4aa0da8efb3b313eaac89dd2ccdcb8`.
Required hosted jobs passed on that PR head; the last CodeRabbit check was cancelled.
That is not a claim that every review finding is resolved.

The local develop integration combines this implementation with the refreshed
developer-preview documentation. Earlier `80f2580` source lacked these modules;
check your actual source revision when diagnosing an unavailable feature.
Documentation alone does not enable a runtime capability.

`v0.5.0-alpha` is the intended next preview label, not a claim that an artifact
has been published. The older `v0.5.0-unstable` release remains a separate snapshot.

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
| Checkpoints | Git-backed bounded text snapshots, preview, exact approval and safety snapshot | Windows directory replacement race defense remains unresolved. Binary/sensitive/unsupported files are excluded. |
| Monitoring | Optional Go aggregation with local/paired telemetry and read-only SSH target support | Connectivity, permission and freshness are separate; SSH execution/workspace capabilities remain false. |
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
parity, MCU support or general remote execution over SSH is claimed.

## Gates before a beta claim

1. Resolve safety/data-loss findings, including Windows checkpoint path races, or
   explicitly make the affected capability unavailable in the release candidate.
2. Build and audit one coherent candidate from the final source snapshot with
   pinned runtime/helper closure, licenses and artifact hashes.
3. Verify isolated install/update/uninstall and profile/history/settings preservation
   against that candidate; distinguish fixtures from real vault/provider evidence.
4. Match onboarding, supported workflows, screenshots and limitations to the candidate.
5. Record maintainer visual acceptance and remaining platform/hardware/provider gates.

Alpha does not waive safety requirements. Do not distribute an unsafe restore
path as production-safe. See [release verification](release-verification.md).
