# PPW Workflow
PPW 工作流

## Activation
激活规则

When the user input contains `@PPW` or clearly requests project-process inventory, output exactly:
当用户输入中包含 `@PPW`，或明确要求项目流程梳理 / 盘点时，必须原样输出：

> ✅ 项目流程梳理工作流（PPW）已激活
> 当前阶段：A1 – 项目资产盘点（Inventory）

## Stage ownership in the imperial model
在朝廷式模型中的阶段归属

- A1 Inventory: `taizi` + `gongbu`
- A1 Inventory（资产盘点）：`taizi` + `gongbu`
- A2 Goals: `zhongshu`
- A2 Goals（目标与上下文）：`zhongshu`
- A3 Flows: `zhongshu` + `libu`
- A3 Flows（系统与流程图谱）：`zhongshu` + `libu`
- A4 Contracts: `zhongshu` + `libu`
- A4 Contracts（接口与契约）：`zhongshu` + `libu`
- A5 Risks: `menxia` + `xingbu`
- A5 Risks（质量与风险）：`menxia` + `xingbu`
- A6 Gaps: `zhongshu` + `hubu`
- A6 Gaps（差距与路线图）：`zhongshu` + `hubu`
- A7 Sign-off: `shangshu` + `libu`
- A7 Sign-off（评审与签收）：`shangshu` + `libu`

## Required documents
必需文档

- `docs/[YYYY_MM_DD]_[中文任务名]/01_INVENTORY.md`
- `docs/[YYYY_MM_DD]_[中文任务名]/02_GOALS.md`
- `docs/[YYYY_MM_DD]_[中文任务名]/03_FLOWS.md`
- `docs/[YYYY_MM_DD]_[中文任务名]/04_CONTRACTS.md`
- `docs/[YYYY_MM_DD]_[中文任务名]/05_RISK_REGISTER.md`
- `docs/[YYYY_MM_DD]_[中文任务名]/06_ROADMAP.md`
- `docs/[YYYY_MM_DD]_[中文任务名]/07_CONSENSUS.md`
- `docs/[YYYY_MM_DD]_[中文任务名]/08_DECISIONS.md`

## Document bootstrap
文档初始化规则

When PPW is selected, these files must be created or updated under the current active project's root `docs/` directory as the project's fact base.
当选中 PPW 时，必须在当前打开项目根目录下的 `docs/` 目录中创建或更新这些文件，作为项目事实源。

- `taizi` must put the required-document list into the first task card
- `taizi` 必须把必需文档清单写入首张任务卡
- use the current date as a directory prefix in `YYYY_MM_DD` format, for example `docs/2026_03_17_项目流程梳理/`
- 目录名前缀必须使用当前日期，格式为 `YYYY_MM_DD`，例如 `docs/2026_03_17_项目流程梳理/`
- the `docs/` directory is always relative to the active project root in the IDE
- `docs/` 目录始终相对于当前 IDE 中打开项目的根目录
- `zhongshu` must convert the document list into a phased project-document plan
- `zhongshu` 必须把文档清单转成阶段化的项目文档计划
- `shangshu` must dispatch `libu` to initialize missing files
- `shangshu` 必须调度 `libu` 初始化缺失文件
- progress beyond A1 should not happen while the project-document set is still missing
- 当项目文档集仍然缺失时，不应推进到 A1 之后的阶段

## Control rules
控制规则

- record facts, verified information, and clear decisions only
- 只记录事实、已验证信息和明确决策
- do not invent future roadmap items without evidence
- 没有证据时，不要凭空发明未来路线图
- if critical repositories, environment config, or secret provenance are missing, stop before A2
- 如果关键仓库、环境配置或密钥来源缺失，就在进入 A2 之前停止
