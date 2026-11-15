# Model credentials

**Developer Preview · v0.5.0-alpha**

Provider API keys are separate from the local service bearer token. Neither belongs
in ordinary model configuration, screenshots, command-line URLs or issue reports.

## Save or use a key

In **Settings → Models and connections**, select the provider and endpoint,
enter the key in the masked API key field, and choose **Save securely** or
**Use for this session only**. The first-run setup exposes the same explicit choice.
Changing an endpoint changes the credential scope; save a key for the new scope
deliberately. Save model configuration through its separate section save control.

Session-only values are forgotten when Odessy closes. Secure storage uses an
approved OS backend where available: Windows Credential Manager or Linux Secret
Service. A missing/unavailable backend is an error, never permission to fall back
to a plaintext file. Linux code availability does not establish native D-Bus or
packaged acceptance on every distribution.

## Resolution and removal

Resolution is explicit session value, explicitly saved secure override, environment,
legacy saved key, then no key. Without a new explicit override, legacy configurations
retain their environment precedence. Settings reports the source without returning
the secret. Removing an override reveals the next available source; it does not
delete or change an environment variable. A replacement key becomes active only
after its operation is acknowledged.

## Contributor contract

The fixed setup operation is `model-credential`, with actions `describe`, `set`
and `remove`. Scope binds provider, endpoint and credential environment reference.
Values are passed over private stdin, not command arguments. Replies contain
source/configured/writable/persistence metadata, never the value. The existing
local API `CredentialStore` does not become a provider-key vault.

Package the existing keyring dependency and its reviewed closure/notices through
the normal installer pipeline. Secure storage reduces routine disclosure; it does
not protect secrets from arbitrary code running as the same OS user.

Native-vault, provider, installation and fixture checks remain distinct. Do not
qualify real keys or live providers using dummy-key/mock-provider receipts. See
[current support](../current-status.md) and [release verification](../release-verification.md).
