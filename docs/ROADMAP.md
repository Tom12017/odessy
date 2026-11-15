# Contributor roadmap

**Developer Preview · v0.5.0-alpha**

This roadmap identifies useful next work, not promised release dates. Check the
[support matrix](current-status.md) for implemented behavior and evidence limits.

| Area | Implemented foundation | Next useful contribution |
| --- | --- | --- |
| Desktop | Production projects/recent sidebar, inspector, retained Activity & usage/Jobs/Handoffs, eight settings groups | Focused accessibility, narrow-layout and error-state improvements backed by tests |
| History | SQLite projects/events/search/export and Custom restart continuation | Profile migration/restore and continuation regression coverage |
| Permissions | Existing policy, explicit grants and revision-bound Custom access modes | Boundary tests; no broadening authority as a UI convenience |
| Context | Explicit memory and opt-in lexical document retrieval | Source-validation, budget and citation regression coverage |
| Terminal/checkpoints | Conditional local Windows PTY and Git text checkpoints | Resolve Windows restore path-race safety before widening use; qualify native closure |
| Installation | Role-aware Windows setup and versioned maintenance | One coherent final-candidate acceptance run, clean-machine evidence and signing |
| Monitoring | Optional Go history/aggregation, local/paired telemetry and read-only SSH | Direction-specific device evidence and honest freshness diagnostics |
| Voice/providers | Existing adapters and scoped audio evidence | Reproducible provider/device compatibility and acoustic interruption tests |
| Platforms | Windows primary; Linux source/CI | Native Linux package/GUI evidence; no unsupported parity claim |

Contributors can start with [setup and checks](../CONTRIBUTING.md), inspect
[open issues](https://github.com/Trisoma/odessy/issues), and propose one bounded
improvement with an acceptance test. Security-sensitive restoration, grants and
runtime dispatch need maintainer review. MCU support, a custom wake word,
automatic updating and full Harness coordination parity are not current guarantees.
