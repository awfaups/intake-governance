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

- `docs/project/01_INVENTORY.md`
- `docs/project/02_GOALS.md`
- `docs/project/03_FLOWS.md`
- `docs/project/04_CONTRACTS.md`
- `docs/project/05_RISK_REGISTER.md`
- `docs/project/06_ROADMAP.md`
- `docs/project/07_CONSENSUS.md`
- `docs/project/08_DECISIONS.md`

## Control rules
控制规则

- record facts, verified information, and clear decisions only
- 只记录事实、已验证信息和明确决策
- do not invent future roadmap items without evidence
- 没有证据时，不要凭空发明未来路线图
- if critical repositories, environment config, or secret provenance are missing, stop before A2
- 如果关键仓库、环境配置或密钥来源缺失，就在进入 A2 之前停止
