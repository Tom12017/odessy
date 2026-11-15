# Screenshot provenance

The [screen gallery](../README.md) contains 30 recorded production renders:
29 connected views with deterministic provider output and one native Windows
settings window. The images cover conversation/history, navigation, workspace
panels and all eight settings groups. No new images were captured by this cleanup.

`manifest.json` preserves the recorded image hashes, source/build identities and
fixture/provider scope. Its capture snapshot predates subsequent merge/review
fixes, so the gallery is a visual reference, not final package qualification.

For new captures, use the production `main.dart` entry, an isolated profile and
explicitly labeled deterministic provider output. Record source hashes, window
dimensions, theme, native/widget capture method and any unavailable capabilities.
Review/redact private data before replacing images and update the manifest only
for an actually observed capture. A standalone design demo is not production evidence.

Do not recreate historical worker worktrees or use ignored maintainer-local scripts
as external contributor prerequisites. See [release verification](../../release-verification.md)
for separate source, native, installed and human acceptance gates.
