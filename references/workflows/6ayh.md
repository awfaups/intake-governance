# 6AYH Workflow
6AYH 工作流

## Activation
激活规则

When the user input contains `@6AYH`, output exactly:
当用户输入中包含 `@6AYH` 时，必须原样输出：

> ✅ 6A 优化工作流（6AYH · 前端渐进式优化模式）已激活
> 当前阶段：Align（目标与风险对齐）

## Stage ownership in the imperial model
在朝廷式模型中的阶段归属

- Align: `taizi` + `zhongshu`
- Align（目标与风险对齐）：`taizi` + `zhongshu`
- Architect: `zhongshu`
- Architect（方案设计）：`zhongshu`
- Atomize: `zhongshu`
- Atomize（原子化拆解）：`zhongshu`
- Approve: `menxia`
- Approve（审批）：`menxia`
- Automate: `shangshu` dispatching `bingbu`, `gongbu`, and `xingbu` as needed
- Automate（执行）：由 `shangshu` 根据需要调度 `bingbu`、`gongbu`、`xingbu`
- Assess: `shangshu` + `libu`
- Assess（评估）：`shangshu` + `libu`

## Required documents
必需文档

- `docs/[YYYY_MM_DD]_[中文任务名]/01_ALIGNMENT_[中文任务名].md`
- `docs/[YYYY_MM_DD]_[中文任务名]/02_DESIGN_[中文任务名].md`
- `docs/[YYYY_MM_DD]_[中文任务名]/03_TASK_[中文任务名].md`
- `docs/[YYYY_MM_DD]_[中文任务名]/04_APPROVE_[中文任务名].md`
- `docs/[YYYY_MM_DD]_[中文任务名]/05_ACCEPTANCE_[中文任务名].md`
- `docs/[YYYY_MM_DD]_[中文任务名]/06_FINAL_[中文任务名].md`
- `docs/[YYYY_MM_DD]_[中文任务名]/07_TODO_[中文任务名].md`
- `docs/[YYYY_MM_DD]_[中文任务名]/99_REFERENCES_[中文任务名].md`

## Document bootstrap
文档初始化规则

When 6AYH is selected, these files must be created or updated before optimization work starts.
当选中 6AYH 时，必须先创建或更新这些文件，然后才能开始优化工作。

- `taizi` must put the required-document list into the first task card
- `taizi` 必须把必需文档清单写入首张任务卡
- use the current date as a directory prefix in `YYYY_MM_DD` format, for example `docs/2026_03_17_首页优化/`
- 目录名前缀必须使用当前日期，格式为 `YYYY_MM_DD`，例如 `docs/2026_03_17_首页优化/`
- `zhongshu` must convert the document list into a staged plan
- `zhongshu` 必须把文档清单转成分阶段计划
- `shangshu` must dispatch `libu` to initialize missing files
- `shangshu` 必须调度 `libu` 初始化缺失文件
- every optimization step must have a corresponding doc update, rollback note, or validation note
- 每一步优化都必须有对应的文档更新、回滚说明或验证记录
- optimization execution is blocked until the document skeleton set exists
- 在文档骨架集合存在之前，优化执行被阻断

## Control rules
控制规则

- optimization must be progressive and reversible
- 优化必须是渐进式的，而且必须可回滚
- do not change external contracts unless explicitly approved
- 除非明确获批，否则不要修改对外契约
- every step must have rollback and observable validation
- 每一步都必须具备回滚路径和可观测验证
- if risk cannot be bounded, stop and return to Align
- 如果风险无法被明确边界化，立即停止并回到 Align
