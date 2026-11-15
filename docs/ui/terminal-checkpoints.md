# Local terminal and workspace checkpoints

**Developer Preview · v0.5.0-alpha**

## Interactive terminal versus recorded Output

Output displays bounded, session-owned tool observations and accepts no shell input.
Opening or restoring Output never executes a command. A local interactive terminal
is a distinct capability backed by the owned Node helper and a real native PTY.

The production composition registers terminal routes only when the verified helper,
Node runtime and matching native dependency closure are available. The reviewed
dependency receipt pins `node-pty 1.1.0` and `node-addon-api 7.1.1` with integrity
and license records. Native Windows ConPTY tests and prior installed checks exist
for recorded snapshots; they do not qualify a new final release candidate.

The service capability response is authoritative. Missing closure means unavailable;
there is no fixture fallback, remote SSH terminal or automatic package download.
Creation requires an explicit exact shell grant through existing policy/broker
ownership. A shell runs with the user's OS permissions: its input is not individually
intercepted or confined to the selected workspace. Do not grant it for untrusted work.

Routes are scoped to `/v1/sessions/{sid}/terminals`: create, read bounded ordered
output, submit input, resize, interrupt and close. Session/service identity,
revision, current authority and handle ownership remain checked. Revocation and
session/service shutdown close owned helpers. Restart never restores handles,
replays input or resumes a shell.

## Checkpoints

Checkpoints use a private Git index and owned `refs/odessy/checkpoints/*` refs.
Metadata lives outside the workspace. They do not reset the user's index, branch
or unrelated dirty files. Git must already be available; non-Git roots are unsupported.

Bounds: 1,000 files, 2 MiB per file, 10 MiB total captured text and 20 retained
checkpoints per workspace. Sensitive paths, Git internals, links/reparse points,
NUL/non-UTF8/binary content and unsupported files are excluded and reported.
This is not a general backup or full-filesystem restoration service.

Creation and restoration use the existing explicit approval owner. Preview binds
the checkpoint, workspace, current content hashes and revision. Changed content
or a stale revision requires a new review; opening a preview grants no permission.
Restoration takes a safety checkpoint first and writes only supported captured
paths, atomically per file. It is not a multi-file atomic transaction and cannot
undo network calls, executed commands or other external effects.

## Unresolved Windows safety limit

**Directory-handle protection against concurrent path replacement remains an open
review finding on Windows.** Existing containment/reparse checks do not eliminate
the race between validation and replacement. Do not use restore where untrusted
processes can mutate workspace directory structure concurrently. A beta candidate
must fix this finding or make affected restoration unavailable; an alpha label is
not a security mitigation. POSIX no-follow directory-descriptor defenses do not
establish Windows parity.

## Ownership and verification

`application/basics_integration.py` owns production composition; session lifecycle
owns cleanup; terminal/checkpoint services use trusted inspector/policy/broker
callbacks. Feature availability is not inferred from a rendered widget.

Source checks include `tests/test_checkpoint_service.py`,
`tests/test_agent_basics_production.py` and `tests/test_terminal_native.py`.
Native terminal checks require the reviewed helper/runtime closure and are separate
from ordinary offline fixtures. See [release verification](../release-verification.md) for candidate acceptance requirements.
