# 入门

[English](../getting-started.md) | **简体中文** | [Español](../es/getting-started.md)

> 说明：英文文档为权威版本（canonical），本页为简体中文翻译，仅供参照；界面截图显示英文界面，应用本身尚未本地化。

**Developer Preview · v0.5.0-alpha · Windows 11 x64**

打开桌面应用，在 Settings 中配置模型，选择一个一次性工作区，然后发送请求。桌面应用会自行启动并认证其本地服务。手动启动 Python 服务和复制 token 属于**高级集成检查**，不是普通用户工作流。模块 CLI 仍为开发和诊断而保留。

## 选择你的路径

- **Windows 安装程序：**维护者已确认候选安装包成功安装；其自带运行时，最终用户无需 Python、Node 或 Flutter SDK。请按[手册](./GOLDEN_PATH.md#1-安装并打开-odessy)核对 EXE/校验值，并完成安装、Piper/Kokoro 选择及可选唤醒设置。
- **源码检出：**使用下方开发者步骤；源码构建需要 SDK，与提供的安装包分开。本页不会发布下载文件；请向分发者取得匹配候选版本，或使用源码。旧 UI 归档不包含当前完整应用。

## 准备 Windows 源码检出

安装 Git、带 `py` 启动器的 Python 3.13、Node.js 22、Flutter 3.47.7 stable，以及 Visual Studio 的 **Desktop development with C++**（使用 C++ 的桌面开发）工作负载和 Windows SDK。用 `flutter doctor -v` 检查 Windows 构建就绪情况。键入式聊天不需要 GPU 或语音模型。依赖安装需要网络访问。

在 PowerShell 中，从你选择的父文件夹开始，使用一个新的检出：

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

如果任一命令失败，请停止。请将打印出的源码修订保存到任何缺陷报告中。你不需要激活虚拟环境，也不需要更改 PowerShell 执行策略。只有在构建各自的可选组件时才需要 Rust 和 Go；开始本地键入式聊天练习并不需要它们。

## 使用桌面托管的启动方式启动

在**同一个终端**中：

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

这些 defines 会在生产版 `lib/main.dart` 中选择 `LocalDesktopApplication`，并把服务归属方和安装辅助程序都绑定到该检出的 Python。单纯的 `flutter run -d windows` 会选择断开连接的客户端界面。两者都不是 `--demo`；托管模式必须报告启动失败，而不是用测试夹具替代。

无需第二个后端终端，也无需在命令行中手动生成 token 或 API 密钥。使用 **Settings → Models and connections**（设置 → 模型与连接）配置你的提供商/模型和掩码凭据。保存，遵循指示的应用/重连步骤，如尚未连接则使用 **Connect saved configuration**（连接已保存配置）。[手册](./GOLDEN_PATH.md#2-配置-deepseek)以 DeepSeek 作为其中一个已测试示例；另一个兼容提供商是可选的。云请求可能产生费用，并会把经允许的观察内容发送给该提供商。

如果发现先前的源码配置，请在连接前审阅其模型和工作区。预览连接器/运行时状态使用 `build/local-desktop/state`；桌面应用还可以在用户的 Odessy 设置中记住一个源码配置指针。这是一次检出构建，并不表示完整的配置文件隔离，也不代表安装程序更新。关闭应用会关闭其拥有的服务。

## 到达终点

通过 **Workspaces**（工作区）选择一个一次性文件夹，保存并应用任何重启提示，然后开始一个 **Custom** 聊天。按照手册的[本地 Deny → Approve once 练习](./GOLDEN_PATH.md#3-在你的-windows-笔记本上运行命令)操作。检查实际的工具输出和退出码。夹具问候语或助手的成功声明并不能证明真实工具运行过。

语音和 SSH 是可选的后续步骤。源码安装不会下载它们的资源，也不会构建可选的监控/密码辅助程序。它们各自的要求见[语音组件](../setup/voice-components.md)（English only）和 [SSH 安装](../setup/ssh-computers.md)（English only）。

## 诊断启动失败

从 Settings 中可见的错误开始。对于源码 CLI 诊断，回到仓库根目录，让 doctor 指向源码托管配置，并选择你配置的后端，例如：

```powershell
Set-Location $previewRepo
$env:ODESSY_CONFIG_FILE = "$previewRepo/build/local-desktop/state/odessy.env"
& $previewPython -m odessy doctor --model-backend deepseek
```

所选配置和模型凭据也有各自的安装/安全存储归属方；doctor 不是运行中桌面状态的完整复刻。仅会话使用的 API 密钥有意不在另一个进程中存在。不要为了满足 doctor 而把密钥复制到明文文件。无关的默认 Ollama 失败并不证明已配置的 DeepSeek 服务失败。doctor 可以探测已配置端点或列出已配置工具；它不会下载模型、运行实时云推理或测试物理音频。

使用手册中的[故障排查与脱敏报告步骤](./GOLDEN_PATH.md#故障排查与报告)。有关确定性的组件测试或手动管理的 API 服务器，参见[高级开发检查](./CONTRIBUTING.md#高级组件与-api-检查)。Linux CI/源码路径在那里仍然可用；本 Windows 指南并不验证 Linux/macOS 桌面软件包。
