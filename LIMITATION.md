# Known limitations

**Developer Preview · v0.5.0-alpha**

The [current support matrix](docs/current-status.md) is the maintained capability
and release baseline. This page summarizes constraints that affect adoption.

- **Release qualification:** CI and earlier installed receipts do not qualify a
  new final merged installer. Signing, clean-machine behavior and broader hardware
  acceptance remain separate gates.
- **Checkpoint safety:** Windows restore directory-handle race defense remains
  unresolved. Do not use restoration in a workspace whose directories can be
  concurrently changed by untrusted processes. Text-only snapshots are not a full
  backup and cannot undo executed commands or external effects.
- **Engine differences:** Custom supports bounded restart continuation. Harness
  history remains readable but cannot resume after restart through this adapter.
  Custom access modes and context injection are not silently emulated on Harness.
- **Authority:** full control never grants new workspace/remote rights or defeats
  hard denials. SSH targets are monitoring-only. Pairing, monitoring and execution
  authorization remain independent.
- **Interactive shell:** an explicitly approved local shell has user-level OS
  authority; it is not intercepted or sandboxed command by command. Native helper
  availability is platform/package dependent.
- **Isolation:** user-space path checks are not complete kernel confinement.
  Windows, Linux and Jetson isolation differ. Do not expose legacy unauthenticated
  plaintext LAN execution to untrusted networks.
- **Privacy:** cloud configuration sends request data and permitted observations
  to the selected provider. Redaction is best-effort. SQLite history and memory
  are local profile data, not an encrypted credential vault.
- **Hardware and voice:** no general minimum hardware specification or universal
  audio/provider compatibility is established. Models/assets are optional and
  subject to their own licenses. macOS and general MCU control are unqualified.
- **Coordination:** existing Jobs/Handoffs remain reachable, but supported behavior
  depends on the engine; deferred Harness delegation parity is not implemented
  merely because consultation or a page works.

See [detailed security boundaries](docs/reference/current-limitations.mdx),
[terminal/checkpoint semantics](docs/ui/terminal-checkpoints.md),
[history](docs/ui/conversation-history.md) and [historical evidence](docs/README.md).
