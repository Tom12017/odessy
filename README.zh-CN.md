# Odessy

[English](README.md) | **简体中文** | [Español](README.es.md)

> 说明：英文文档为权威版本（canonical），本页为简体中文翻译，仅供参照；界面截图显示英文界面，应用本身尚未本地化。

**Developer Preview · v0.5.0-alpha**

> **不稳定的开发者预览版。** Odessy 是实验性软件。请预期缺陷、
> 破坏性变更与粗糙之处。目前尚不存在稳定版本。平台覆盖范围与已知限制见
> [支持与限制](docs/zh-CN/current-status.md)。

你好，这里是 Odessy，不是 Odyssey！⛵

> 想了解它是如何开始的？[阅读 Odessy 背后的故事](Story.md)（English only）。

Odessy 正朝着**语音优先（voice-first）的个人智能体**方向发展：由一个桌面端统一协调本地或云端模型，并在你的笔记本电脑或一台已连接的 Linux 计算机上执行经审阅的工作。长期灵感来自 JARVIS/FRIDAY；当前产品是一个实验性的、Windows 优先的应用，在你配置语音的过程中，打字对话已经可用。

**模型提出建议，由 Odessy 的策略层作出决定。** 服务会校验动作、获取所需的人工审批，并在派发工具调用之前重新检查授权。

**我们正在寻找 3–5 位开发者协作者**，希望他们运行真实工作流、报告遇到的问题，并承担一个有明确边界的领域。请从[桌面端手册](docs/zh-CN/GOLDEN_PATH.md)开始，选择一个[开放的 GitHub issue](https://github.com/Trisoma/odessy/issues)，并阅读[贡献与所有权路径](docs/zh-CN/CONTRIBUTING.md#通往领域负责人的路径)。

[从源码运行](docs/zh-CN/getting-started.md) · [架构](docs/zh-CN/ARCHITECTURE.md) ·
[截图](docs/view/README.md)（English only） · [支持与限制](docs/zh-CN/current-status.md)

## 架构层面的关键押注

- **策略掌握授权。** 模型输出只是建议。策略与审批由 Python 掌握；工具适配器在派发时重新校验。一条聊天消息或一台已连接的设备都不会授予任何权限。
- **单一协调者，执行目标彼此独立。** 模型可以留在笔记本电脑上，或放在选定的服务提供方；执行可选择本地、经认证的配对主机，或明确批准的 SSH 执行。SSH 计算机无需模型。边缘/LAN 集成的实验范围更窄，MCU/家庭自动化仍是可以贡献的方向，而非已实现的支持。
- **语音是预期中的主要接口。** STT、TTS 与唤醒监听同打字输入共享智能体生命周期与授权边界。语音配置、延迟与硬件兼容性仍需完善；以语音方式作出的审批并不等于身份认证。

这些是需要继续开发和验证的设计选择，并不意味着其他智能体没有审批机制、所有服务提供方都是本地的，或 Odessy 是一个完整的沙箱。

## 试用开发者预览版

常规使用体验是：**打开 Odessy → 在 Settings（设置）中配置模型 → 选择工作区 → 对话并审阅动作**。后端启动与本地认证由桌面端负责。用户无需手动运行 Python，也无需交换 bearer token。

- **已经有完整的候选版本？** 请按[图文手册](docs/zh-CN/GOLDEN_PATH.md)操作。Windows 安装包含其受支持的运行时，并采用带版本号的维护机制。
- **从源码构建？** 请参阅[入门指南](docs/zh-CN/getting-started.md)。安装开发者 SDK 之后，其桌面端托管模式使用相同的已配置服务生命周期。手动启动服务与 fake-model 命令属于独立的贡献者检查项。

完整的 Windows x64 安装程序已构建，维护者于 2026 年 11 月 18 日确认安装成功。安装时可选 **Piper（推荐用于 CPU）** 或 **Kokoro**，支持主动选择并校验语音下载，唤醒词另行选择。参见[安装步骤及校验值](docs/zh-CN/GOLDEN_PATH.md#1-安装并打开-odessy)。本次更新不会自动发布下载文件；请向分发者或在[发布页面](https://github.com/Trisoma/odessy/releases)取得匹配 EXE。旧的 `v0.5.0-unstable` UI 归档并非当前完整安装包。具体证据及待验证事项见[候选版本回执](docs/verification/windows-piper-installer-2026-11-18.md)（English only）。

## 你可以探索的内容

| 领域 | 开发者预览版行为 |
| --- | --- |
| 对话 | 项目、已保存的历史、搜索、导出、重命名、置顶与归档。Custom 支持有边界的重启后延续；重启后 Harness 历史为只读。 |
| 工具与权限 | 经审阅的动作、显式审批、取消操作，以及受支持的 Custom 访问模式。完全控制既不会覆盖硬性拒绝，也不会扩大已有授权。 |
| 工作区面板 | 限定范围的文件读取、提议的差异（diff）与已记录的命令输出。该输出不同于交互式终端。 |
| 上下文 | 显式项目记忆与按需启用的本地文档检索，包含来源引用，并提供有边界的 Custom 上下文准备。 |
| 本地终端 | 在已验证的原生辅助程序闭包可用时，提供有条件的 Windows PTY 支持；需要显式的 shell 授权。不提供 SSH 终端。 |
| 设备与 SSH | 只读监控，外加单独选择的 Custom SSH 命令，每条命令都需要逐条精确审批。仅登录不会获得执行或工作区访问权限；实验性的 LAN 是另一条独立路径。 |
| 语音与设置 | 现有的语音与模型配置、八个设置分组，以及本地外观偏好。物理音频与服务提供方行为需另行验证。 |

在 Windows 上，检查点的创建、列出与预览仍然可用，但在目录句柄安全性实现之前，**Windows 上的检查点恢复功能被禁用**。后端会拒绝直接恢复请求；桌面端会说明这一限制。受支持的非 Windows 恢复操作仍需精确审批。见[终端与检查点限制](docs/ui/terminal-checkpoints.md)（English only）。

## 平台范围

Windows x64 是主要的开发平台，也是记录在案的原生测试平台。Linux 具备源码/CI 覆盖以及范围有限的历史设备证据；这并不等同于完整的桌面端/软件包对等性。macOS 尚未通过资格认定（unqualified）。硬件要求尚未确定。在选择部署方式之前，请阅读[支持矩阵](docs/zh-CN/current-status.md)。

## 安全与隐私

策略与授权由 Python 掌握；现有的 MCP 工具执行由 Node 掌握；配对身份/传输由 Rust 掌握；可选遥测由 Go 汇总；Flutter 使用类型化客户端。选择云端模型会将请求数据发送到该服务提供方。脱敏处理属于尽力而为（best-effort），并不能保证信息不被披露。

经批准的交互式 shell 以用户的操作系统权限运行，并不是逐条命令的工作区沙箱。遗留的明文 LAN 执行方式不适用于不可信网络。请优先使用文档中说明的认证传输路径。请通过 [SECURITY.md](SECURITY.md)（English only）私下报告漏洞。

## 与我们共建 Odessy

我们是一个小团队：两位常驻贡献者，另有三位在短期内协助，也希望能有更多人同行。无论你想修复一个缺陷、改进某个组件，还是与我们一同推进 Odessy 中更大的部分，都欢迎加入。我们正在寻找能够把一个聚焦的任务从复现、实现一路推进到评审的协作者。复现、测试与文档都是很有价值的第一份贡献。

我们希望获得帮助的一些领域：

- **AI 智能体：** 编排、工具调用、模型集成与记忆。
- **硬件探索：** Jetson、Raspberry Pi、BLE 与 MCU 通信。这些是关注方向，并非对当前设备支持的承诺。
- **系统：** Rust、网络、mTLS 与安全执行。
- **桌面端：** Flutter、Dart、无障碍与 UI/UX。
- **基础设施：** Go、监控、遥测与多主机管理。
- **语音：** STT、TTS、唤醒词检测与音频处理。

文档、兼容性测试与可复现的缺陷报告同样欢迎。Odessy 是一个独立的、由志愿者驱动的项目。贡献没有报酬，也没有固定的时间投入要求：力所能及时伸出援手即可。

可以从 [Piper 诊断](https://github.com/Trisoma/odessy/issues/69)、
[SSH 连接状态](https://github.com/Trisoma/odessy/issues/70)、
[TTS 基准测试摘要](https://github.com/Trisoma/odessy/issues/71)，或
[记录输出体验](https://github.com/Trisoma/odessy/issues/72)开始。每个 GitHub issue 都包含范围、验收标准与测试命令。开始前请在 issue 中评论以进行协调。

请从[贡献指南](docs/zh-CN/CONTRIBUTING.md)开始，了解[架构](docs/zh-CN/ARCHITECTURE.md)，浏览
[开放的 issue](https://github.com/Trisoma/odessy/issues)，或提出一个想法。对于较大的改动，请在开始前先与我们讨论方案。欢迎 AI 辅助的贡献；贡献者仍需对评审、测试与署名负责。

Odessy 采用 [Apache-2.0](LICENSE)（English only）许可。随附的组件与模型资产另有其自身条款；见[第三方声明](THIRD-PARTY-NOTICES.md)（English only）与[许可证清单](docs/reference/third-party-licenses.md)（English only）。
