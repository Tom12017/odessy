# Getting started

**Developer Preview · v0.5.0-alpha · Windows 11 x64**

Open the desktop, configure a model in Settings, choose a disposable workspace,
and send a request. The desktop starts and authenticates its local service for you.
Manual Python service startup and token copying are **advanced integration checks**,
not the normal user workflow. The module CLI still exists for development and diagnostics.

## Choose your route

- **Supplied full installer:** follow the [desktop manual](GOLDEN_PATH.md#1-install-and-open-odessy).
  The package supplies its runtime; no Python, Node or Flutter SDK is an end-user requirement.
- **Source checkout:** use the steps below. As of November 18, 2026, the public release page
  only supplies older UI-client archives, not a matching full installer. Do not combine them
  with current source. Source builds require development tools; first build time varies.

## Prepare a Windows source checkout

Install Git, Python 3.13 with the `py` launcher, Node.js 22, Flutter 3.47.7 stable,
and Visual Studio's **Desktop development with C++** workload with a Windows SDK.
Use `flutter doctor -v` to check Windows build readiness. No GPU or speech model is
required for typed chat. Dependency installation uses network access.

In PowerShell, from a parent folder of your choice, use a new checkout:

```powershell
git clone --branch develop --single-branch https://github.com/Trisoma/odessy.git odessy-preview
Set-Location odessy-preview
$previewRepo = (Get-Location).Path.Replace('\', '/')
$previewPython = "$previewRepo/.venv/Scripts/python.exe"
py -3.13 -m venv .venv
& $previewPython -m pip install -e ".[test,ui]"
Push-Location tools
npm.cmd ci --no-audit --no-fund
npm.cmd run build
Pop-Location
flutter doctor -v
git rev-parse HEAD
```

Stop if a command fails. Save the printed source revision with any bug report.
You do not need to activate the virtual environment or change PowerShell execution policy.
Rust and Go are needed only when building their optional components; they are not
required to begin the local typed-chat exercise.

## Launch with desktop-owned startup

In that **same terminal**:

```powershell
$previewDefines = @(
    '--dart-define=ODESSY_LOCAL_DESKTOP=true'
    "--dart-define=ODESSY_DESKTOP_ROOT=$previewRepo"
    "--dart-define=ODESSY_DESKTOP_PYTHON=$previewPython"
    "--dart-define=ODESSY_SETUP_ROOT=$previewRepo"
    "--dart-define=ODESSY_SETUP_PYTHON=$previewPython"
)
Set-Location apps/desktop
flutter pub get
flutter run -d windows @previewDefines
```

These defines select `LocalDesktopApplication` in production `lib/main.dart` and
bind both the service owner and setup helper to this checkout's Python. Plain
`flutter run -d windows` selects the disconnected client surface instead. Neither is
`--demo`; the managed mode must report a startup failure rather than substitute fixtures.

No second backend terminal, manually generated token or API key in the command line is
needed. Use **Settings → Models and connections** to configure your provider/model and
masked credential. Save, follow the indicated apply/reconnect step, and use
**Connect saved configuration** if not already connected. The [manual](GOLDEN_PATH.md#2-configure-deepseek)
walks through DeepSeek as one tested example; another compatible provider is optional.
Cloud requests can incur charges and send permitted observations to that provider.

If a previous source configuration is discovered, review its model and workspace
before connecting. Preview connector/runtime state uses `build/local-desktop/state`;
the desktop can also remember a source configuration pointer in the user's Odessy
settings. This is a checkout build, not a claim of complete profile isolation or an
installer update. Closing the app shuts down its owned service.

## Reach the finish line

Choose a disposable folder through **Workspaces**, save and apply any restart prompt,
then start a **Custom** chat. Follow the manual's [local Deny → Approve once exercise](GOLDEN_PATH.md#3-run-a-command-on-your-windows-laptop).
Check the actual tool output and exit code. A fixture greeting or an assistant's
success claim does not prove a real tool ran.

Voice and SSH are optional next steps. Source setup does not download their assets or
build the optional monitoring/password helpers. See [voice components](setup/voice-components.md)
and [SSH setup](setup/ssh-computers.md) for their separate requirements.

## Diagnose a failed start

Start with the visible error in Settings. For a source CLI diagnostic, return to the
repository root, point doctor at the source-managed profile and select the backend
you configured, for example:

```powershell
Set-Location $previewRepo
$env:ODESSY_CONFIG_FILE = "$previewRepo/build/local-desktop/state/odessy.env"
& $previewPython -m odessy doctor --model-backend deepseek
```

The selected configuration and model credentials also have setup/secure-store owners;
doctor is not a complete replica of the running desktop state. A session-only API key
is deliberately absent from another process. Do not copy a key into a plaintext file
to satisfy doctor. An unrelated default Ollama failure does not prove the configured
DeepSeek service failed. Doctor can probe configured endpoints or list configured tools;
it does not download models, run a live cloud inference or test physical audio.

Use the manual's [troubleshooting and sanitized reporting steps](GOLDEN_PATH.md#troubleshooting-and-reporting).
For deterministic component tests or a manually managed API server, see
[advanced development checks](../CONTRIBUTING.md#advanced-component-and-api-checks).
The Linux CI/source path remains available there; this Windows guide does not qualify
Linux/macOS desktop packages.
