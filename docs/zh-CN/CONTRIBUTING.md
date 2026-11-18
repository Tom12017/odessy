# 为 Odessy 贡献

[English](../../CONTRIBUTING.md) | **简体中文** | [Español](../es/CONTRIBUTING.md)

> 说明：英文文档为权威版本（canonical），本页为简体中文翻译，仅供参照；界面截图显示英文界面，应用本身尚未本地化。

**Developer Preview · v0.5.0-alpha**

请先阅读[受管的桌面端安装](getting-started.md)、[开放的 GitHub issue](https://github.com/Trisoma/odessy/issues)、[支持矩阵](./current-status.md)与[架构](ARCHITECTURE.md)。我们正在寻找能够承担一个聚焦领域并推进到评审的协作者；欢迎以志愿者身份投入你可用的时间。

> 这个项目的简短故事见 [Story](../../Story.md)（English only）

欢迎加入！⛵ 感谢你帮助改进 Odessy。缺陷报告、聚焦的修复以及更清晰的文档，都有助于让这个开发者预览版更易使用。本指南说明从哪里开始、如何搭建环境，以及提交改动时应包含哪些内容。

关于项目概览，请从 [README](../../README.zh-CN.md) 开始。架构与组件文档请从[文档索引](README.md)开始。

## 选择从哪里开始

| 贡献类型 | 如何开始 |
|---|---|
| 缺陷修复与小型文档修复 | 直接提交一个聚焦的 pull request。相关时请链接已有的 issue。 |
| 新功能、增强或较大改动 | 先开一个 issue，说明问题与拟采用的方案，然后再开始实现。 |
| 仅重构或 CI 变更 | 请不要为这类改动单独发起 pull request。 |
| 安全漏洞 | 请遵循 [SECURITY.md](../../SECURITY.md)（English only）。不要在公开 issue 中披露漏洞。 |

即使你无法自行实现修复，也欢迎报告问题。请告知你是否有意着手处理，以便他人与你协调。

## 通往领域负责人的路径

1. 选择一个[开放的 GitHub issue](https://github.com/Trisoma/odessy/issues)，复现该行为，并评论说明你拟处理的范围。开始之前请查看该 issue 当前的讨论与分工，并搜索是否已有重叠的工作。
2. 提交一个聚焦的 PR，并附上其验收检查。请说明哪些证据来自 fixture、哪些来自真实的服务提供方/硬件。第一份贡献可以是一个回归测试、诊断改进、展示层修复，或一份可复现的基准测试报告。
3. 在已有经评审的贡献之后，可以申请承担某个具名领域的职责：维护其测试与文档、分诊相关报告，并协助评审后续改动。请在公开 issue 中与项目维护者就边界与可投入时间达成一致。
4. 仓库权限或具名维护者角色需要另行明确决定。已合并的 PR、自行认领任务，或由 AI 撰写的计划，都不会带来任何权限。

策略/派发、凭据、配对/主机身份、安装归属以及恢复安全性需要项目负责人评审。桌面端的 `lib/app/`、各控制器与共享客户端同样需要依据各自的 `AGENTS.md` 由负责人评审；展示层工作可以在商定的视图文件中开始。在改动某个共享约定之前，请阅读[架构图](ARCHITECTURE.md)与本地说明。

这是志愿者维护，不保证响应时间 SLA。请把复现步骤、验收标准与检查项写进 issue/PR，使进展不依赖私信。若一周之后仍无回应，可补充一次简短的跟进，然后再着手较大的改动。贡献者的可信度与响应速度必须在实际互动中体现；提交量既不能证明前者，也不能证明后者。

## 在开 issue 之前

请检索已有的 issue 与 pull request（包括已关闭与已合并的），以免重复工作。查看相关源码与[已知限制](LIMITATION.md)，了解现有行为与约束。若已有 PR 处理该问题，可以考虑协助评审或改进它。

每个 issue 请聚焦一个问题。缺陷报告请包含：

- 版本或 commit、操作系统、架构以及模型后端。
- 复现问题的步骤，包括你运行的命令。
- 预期行为与实际行为，并在适用时提供已脱敏的诊断信息。

对于功能提案，请描述使用场景、期望行为以及你考虑过的其他方案。对于较大的工作，请在开始前先在 issue 中评论，以便其他贡献者避免重复投入。

## 准备 pull request

请以 `develop` 为目标分支，并让改动小到便于评审。请把不相关的修复、格式变更与依赖更新分开。

在请求评审之前：

- 说明问题以及该改动如何解决它。链接相关的 issue。
- 为行为变更新增或更新测试。绝不要为了让检查通过而删除测试或弱化安全断言。可借助 [LIMITATION.md](LIMITATION.md) 判断应当修正的是实现还是测试预期。
- 当安装、配置或用户可见行为发生变化时，请更新文档。
- 列出你实际执行的检查及其结果，包括失败项、被跳过的检查，以及你无法完成的验证。
- 从代码、fixture、日志与截图中移除密钥和隐私数据。

## 变更日志

对于用户可见的变更，请在 [CHANGELOG.md](../../CHANGELOG.md)（English only）的 **Unreleased** 下添加一条简短记录。描述对用户的影响；省略内部清理与仅修正错别字的改动。维护者在准备发布时会把条目归入某个版本与发布日期之下。详细的资格认定证据与已知限制请保留在 `docs/releases/` 下的发布说明中。

## AI 辅助贡献

欢迎 AI 辅助的贡献；我们的团队也在使用这些工具。请在 PR 中说明你何时使用了 AI 辅助，并描述你自行评审与验证的内容。你仍需对所提交代码的理解、对其行为的检查，以及确认自己有权贡献该代码负责。

## 密钥与安全

切勿提交 API 密钥、token、私人录音或特定机器的凭据。在分享诊断信息之前，请对敏感值与个人信息做脱敏处理。若你发现漏洞，请按 [SECURITY.md](../../SECURITY.md)（English only）中的私下报告说明操作。

## 开发环境搭建

以下命令来自 [CI](../../.github/workflows/ci.yml)（English only）与
[桌面端预览 CI](../../.github/workflows/desktop-preview.yml)（English only）。CI 覆盖 Ubuntu 上的 Python
3.10/3.13、Windows 上的 3.12/3.13，两个平台上的 Node 22/24，
stable Rust，以及 Ubuntu 上的 Flutter 3.47.7（stable）。这一覆盖范围并不构成对硬件、macOS 或实时服务提供方支持的确认。

使用 Python 3.10-3.13 创建并激活虚拟环境：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

在 Linux 上，使用 `source .venv/bin/activate` 激活。Python 集成检查使用 Node 22，配对相关的工作使用 stable Rust。在仓库根目录执行：

```powershell
cd tools
npm ci --no-audit --no-fund
npm run build
cd ..
python -m pip install -e ".[test,ui]" "pytest-xdist>=3.6,<4"
$env:ODESSY_CONFIG_FILE="$PWD/.ci-no-config.env"
$env:PYTHONUTF8="1"
```

在 Linux 上，请使用 `export ODESSY_CONFIG_FILE="$PWD/.ci-no-config.env"` 与
`export PYTHONUTF8=1`，代替 PowerShell 中的环境变量赋值。

### 快速开始的前提要求

以下是下文命令所依据的要求；安装打包好的应用并不需要其中的任何一项。

| 组件 | 已验证的要求 |
|---|---|
| Python | 3.10–3.13；CI 在 Ubuntu 上运行 3.10/3.13，在 Windows 上运行 3.12/3.13 |
| Node | 工具服务器（`tools/`）使用 22 或 24，通过 `npm ci` 安装 |
| Flutter | `apps/desktop` 使用 3.47.7 stable；`packages/odessy_client` 使用其自带的 Dart SDK |
| Rust | stable，仅用于 `native/odessy-link` 的配对工作 |

## 运行桌面端

经配置的、由桌面端托管的启动方式见[入门指南](getting-started.md)。应用会启动服务并处理本地认证。为了走通 [golden path](GOLDEN_PATH.md)，请在 Settings（设置）中配置真实模型。源码启动测试包括 `local_desktop_application_test.dart`、`source_setup_wiring_test.dart`，以及 `apps/desktop/test/` 下需显式启用的 `source_model_integration_test.dart`。最后一项使用真实的 Python 服务与一个回环地址的服务提供方 fixture，不涉及付费推理。

## 高级组件与 API 检查

模块 CLI 仍保留实现，用于诊断、无头使用与集成测试。使用受管的桌面端并不需要这些手动启动服务的命令。下文全部内容都不需要付费服务提供方、麦克风或远程主机。确定性的 fake model 检查的是组件之间的管线；它并不验证真实模型、实时审批体验、语音或远程执行。

启动后端（它会打印回环地址；API 需要 token）：

```powershell
$env:ODESSY_API_TOKEN = python -c "import secrets; print(secrets.token_urlsafe(32))"
python -m odessy serve --fake-model
```

在第二个终端中启动桌面应用：

```powershell
cd apps/desktop
flutter run -d windows
```

在 Linux 上，用以下命令生成一个本地 token 并启动服务器：

```sh
export ODESSY_API_TOKEN="$(python -c 'import secrets; print(secrets.token_urlsafe(32))')"
python -m odessy serve --fake-model
```

然后在 `apps/desktop` 中运行 `flutter run -d linux`。连接桌面应用时请使用生成的 token。在把 token 填入应用之前，可在 PowerShell 中用 `$env:ODESSY_API_TOKEN`、在 Linux 上用 `printf '%s\n' "$ODESSY_API_TOKEN"` 在本地显示它。请保持其私密。每台机器应生成各自的 token。

点击连接图标，输入打印出的回环地址与 token，然后发送 `what time is it?`。token 只保留在应用内存中；后端永远不会打印它。若不加 `--fake-model`，同样的步骤会使用已配置的真实模型及其现有预算，正因如此，实时服务提供方检查属于另一项独立工作。请先清除快速开始阶段的覆盖设置（Linux 上 `unset ODESSY_CONFIG_FILE`，PowerShell 中 `Remove-Item Env:ODESSY_CONFIG_FILE`），或将其指向你的个人配置。否则实时运行仍会使用 `.ci-no-config.env`。

`python -m odessy --fake-model "what time is it?"` 会在不启动桌面端的情况下运行同样的文本循环，这是对 Python 侧最小的端到端检查。

## 诊断本机工作站

```sh
python -m odessy doctor
python -m odessy doctor --voice
```

`doctor` 会列出每个失败或可选的步骤，并在旁边给出一条修复建议，例如模型端点没有响应、`tools/` 目录尚未构建，或可选的语音/唤醒资产缺失。Piper 与自定义服务提供方的检查尚不完整；请同时使用它们受控的服务提供方测试。在 Ollama（或其他端点）运行之前，模型端点出现 `[FAIL]` 是预期现象，不会阻断上文中的 fake-model 检查。它不会下载资产，也不会执行云端推理，但可以探测已配置的端点并列出第三方工具。它并不能完整复刻桌面端仅存于会话中的凭据，也不能替代物理音频验收测试。请把桌面端可见的错误与所选配置连同其输出一并保留。

## 运行相关检查

请为你所改动的组件运行相应检查，并在 PR 中给出确切的命令与结果。请说明哪些检查无法运行及原因。

### Python 运行时

在仓库根目录执行：

```sh
python -m pytest -q -n 2 --dist loadfile --tb=short --durations=10
python -m odessy --help
python -m odessy --fake-model "what time is it?"
python -m odessy --fake-model "list ."
```

CI 会检查 fake-model 的回复分别以 `The current time is ` 与 `Directory entries: ` 开头，并且目录回复中包含 `pyproject.toml`。这些是管线检查，不是真实模型验收。

### Node 工具服务器

在 `tools/` 中执行：

```sh
npm ci --no-audit --no-fund
npm run typecheck
npm test
```

### Rust 传输与配对

在 `native/odessy-link/` 中执行：

```sh
cargo test --locked
cargo clippy --all-targets -- -D warnings
cargo build --locked
```

对于配对集成测试，请先构建 Node 与 Rust，设置 `ODESSY_LINK_E2E=1`
（PowerShell：`$env:ODESSY_LINK_E2E="1"`），然后在仓库根目录运行：

```sh
python -m pytest -q tests/test_paired_transport.py tests/test_paired_integration.py tests/test_paired_agent.py tests/test_paired_host.py
```

### 远程计算机监控（SSH）

针对“已有别名 → 测试连接 → 首次带时间戳的状态 → 断开/重连”这一流程，请使用
[SSH 贡献者路径](../../src/odessy/ssh/README.md)（English only）。其中包含单台笔记本电脑的 fixture 命令、服务提供方/生命周期接缝以及故障排查。监控仍为只读。独立的 Custom SSH 执行选择只有在执行明确的 **Use for agent commands**（用于智能体命令）操作后才会暴露 `ssh.run`；在任何模式下，每条确切的远程命令都需要审批。它以 SSH 账户身份运行，没有远程沙箱。不支持 Harness SSH 执行、远程文件编辑与远程 PTY。见 [SSH 命令边界](../setup/ssh-computers.md)（English only）。已有的、经认证的配对主机仍是另一种受支持的传输方式。

### 实时 Linux 隔离

这些检查需要 bubblewrap、util-linux 以及可用的非特权用户命名空间。特定 runner 的 AppArmor 配置见 CI。设置 `ODESSY_SANDBOX_LIVE=1`，然后在仓库根目录运行：

```sh
python -m pytest -q tests/test_sandbox_live.py
```

在 `tools/` 中运行 `node --test dist/tests/sandbox-live.test.js`。CI 中的 doctor 检查是在仓库根目录的 Bash 下执行 `python -m odessy doctor | tee doctor.txt; grep -q "read-only: bwrap (full; network cut, credentials hidden)" doctor.txt`。这些检查需要真实的 Linux 内核；Windows 无法满足。

### 桌面端与 Dart 客户端

在仓库根目录执行：

```sh
python tool/check_desktop_contracts.py
python -m unittest discover -s tests -p test_desktop_settings_inventory.py -v
```

在 `packages/odessy_client/` 中，使用 Flutter 3.47.7 自带的 Dart SDK：

```sh
dart pub get
dart format --output=none --set-exit-if-changed lib test
dart analyze
dart test
```

在 `apps/desktop/` 中：

```sh
flutter pub get
dart format --output=none --set-exit-if-changed lib test
flutter analyze
flutter test
```

硬件、物理音频、真实网络配对与实时服务提供方检查属于另外的验收工作。若未运行，请明确说明。

## 贡献许可

提交贡献即表示你确认自己有权提交该贡献，并同意按项目的 [Apache-2.0 许可证](../../LICENSE)（English only）对其进行许可。
