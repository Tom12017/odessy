# Getting started

**Developer Preview · v0.5.0-alpha**

This guide runs the production desktop against an authenticated local service
with deterministic model replies. It verifies the contributor plumbing, not
real-model quality or release-package qualification. Check the
[source baseline](current-status.md#source-and-release-baseline) first.

## Choose your installation path

- **Packaged candidate:** use its matching release instructions and checksum manifest,
  then follow the [setup wizard](setup/wizard.md). A complete package carries its
  own supported runtime; development SDKs are not an end-user prerequisite.
- **Source checkout:** use the commands below. Do not combine an old published
  UI-client archive with the latest service and assume protocol compatibility.

## Prepare a source checkout

On Windows, use Python 3.10–3.13, Node 22 and Flutter 3.47.7 stable.
Git is required; Rust and Go are needed only for the components you build.
Dependency installation uses network access unless a verified cache is available.

From the repository root in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[test,ui]"
Set-Location tools
npm ci --no-audit --no-fund
npm run build
Set-Location ..
python -m odessy doctor
```

A missing live model in `doctor` is expected before you configure one. It does
not prevent the fake-model text check. Do not download a model just to run this guide.

## Start the service

Keep the token private. After connecting, select a disposable workspace through
Workspaces before requesting file or shell actions:

```powershell
$env:ODESSY_API_TOKEN = python -c "import secrets; print(secrets.token_urlsafe(32))"
python -m odessy serve --fake-model
```

Leave that terminal open. The service prints its loopback address, not the token.
Read the token locally from `$env:ODESSY_API_TOKEN` when connecting the desktop;
never include it in an issue, screenshot or command-line URL.

## Start the desktop

In a second terminal from the repository root:

```powershell
Set-Location apps/desktop
flutter pub get
flutter run -d windows
```

Open the connection control, enter the printed loopback address and token, and
send `what time is it?`. The app normally starts disconnected; it must not
silently substitute demo data when the service is unavailable.

For a CLI-only deterministic check, use:

```powershell
python -m odessy --fake-model "what time is it?"
```

On Linux, activate the environment with `source .venv/bin/activate`, export a
locally generated `ODESSY_API_TOKEN`, and use `flutter run -d linux`. Linux native
desktop/package acceptance is a separate gate. macOS is unqualified.

## Connect a real model

Stop the fake-model service. Configure an existing model in **Settings → Models
and connections**, or use [headless setup](setup/headless.md). Start the service
without `--fake-model`; select the intended profile for the next turn. Local
inference requires an available compatible endpoint; cloud inference requires
your explicit provider configuration and may incur charges.

Voice is optional. Do not enable microphone capture or download audio assets
unless you intend to use it. See [voice components](setup/voice-components.md).

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Connection refused | Confirm the owning service is running and use its actual loopback port. |
| HTTP 401 | Use the token from that service launch. Do not reuse tokens from another profile or restart. |
| Feature unavailable / HTTP 501 | Check the live engine and capability response; opening a panel cannot enable missing services. |
| Native terminal unavailable | Verify the packaged helper/native closure; Output is not an interactive shell. |
| History appears missing | Check the service's configuration/profile path and engine; do not delete or recreate databases. |
| Saved chat cannot resume | Harness restart history is read-only; Custom continuation also requires a valid matching workspace. |
| Monitoring unavailable / HTTP 503 | Check opt-in configuration, collector readiness and read-only permissions independently of SSH login. |

Continue with [the desktop guide](ui/README.md), [contributor checks](../CONTRIBUTING.md)
and [known limitations](../LIMITATION.md).
