# Odessy 文档

[English](../README.md) | **简体中文** | [Español](../es/README.md)

> 说明：英文文档为权威版本（canonical），本页为简体中文翻译，仅供参照；界面截图显示英文界面，应用本身尚未本地化。

**Developer Preview · v0.5.0-alpha**

请从与你任务对应的指南开始。[当前支持矩阵](./current-status.md)
定义了已实现的行为、尚不可用的能力以及尚未完成的发布关卡。
历史计划与测试记录描述的是它们被记录时的快照，而非当前的支持状况。

[Windows 草稿候选版本](../verification/windows-piper-installer-2026-11-18.md)（English only）可选 Piper/Kokoro；校验值与安装步骤见[手册](GOLDEN_PATH.md)。维护者最终验收及公开发布仍待完成；较早安装包的人工验收仅适用于原校验值。

| 任务 | 指南 |
| --- | --- |
| 运行应用并验证一个本地动作 | [桌面端手册](GOLDEN_PATH.md) · [受管的源码启动](getting-started.md) |
| 安装或管理打包的候选版本 | [安装向导](../setup/wizard.md)（English only） · [安装程序](../../installer/README.md)（English only） |
| 配置模型或凭据 | [无头安装](../setup/headless.md)（English only） · [云端模型](../reference/cloud-models.mdx)（English only） · [凭据](../setup/secure-model-credentials.md)（English only） |
| 使用桌面端 | [桌面端指南](../ui/README.md)（English only） · [界面截图库](../view/README.md)（English only） |
| 了解已保存的对话与 SQLite | [对话历史](../ui/conversation-history.md)（English only） · [数据库指南](../database/README.md)（English only） |
| 了解工具授权 | [访问模式](../ui/access-modes.md)（English only） · [权限](../reference/permissions.mdx)（English only） · [安全限制](../reference/current-limitations.mdx)（English only） |
| 使用记忆与文档 | [上下文、记忆与检索](../ui/context-memory-retrieval.md)（English only） |
| 使用本地终端或检查点 | [能力与安全限制](../ui/terminal-checkpoints.md)（English only） |
| 连接计算机 | [SSH 设置](../setup/ssh-computers.md)（English only） · [实验性执行器](../setup/executor-preview.md)（English only） · [主机配对](../reference/host-pairing.mdx)（English only） |
| 查看遥测 | [监控](../monitoring/README.md)（English only） · [监控 API](../monitoring/api.md)（English only） |
| 从事语音相关的工作 | [桌面端语音](../ui/desktop-voice.md)（English only） · [服务提供方](../reference/speech-providers.md)（English only） |
| 参与贡献并成长为某个领域的负责人 | [开放的 GitHub issue](https://github.com/Trisoma/odessy/issues) · [贡献/所有权路径](CONTRIBUTING.md#通往领域负责人的路径) · [架构](ARCHITECTURE.md) |
| 准备发布 | [Alpha 预览范围](../releases/v0.5.0-alpha.md)（English only） · [发布验证](../release-verification.md)（English only） |

## 正确理解证据

源码测试、托管 CI、原生构建、安装验收、真实服务提供方检查与硬件检查回答的是不同的问题。
截图属于设计证据；它不能证明某个功能在每个引擎或已安装的软件包中都可用。
切勿从设备连通性或项目元数据推断工具执行授权。
