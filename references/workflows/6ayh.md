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

- `docs/[中文任务名]/01_ALIGNMENT_[中文任务名].md`
- `docs/[中文任务名]/02_DESIGN_[中文任务名].md`
- `docs/[中文任务名]/03_TASK_[中文任务名].md`
- `docs/[中文任务名]/04_APPROVE_[中文任务名].md`
- `docs/[中文任务名]/05_ACCEPTANCE_[中文任务名].md`
- `docs/[中文任务名]/06_FINAL_[中文任务名].md`
- `docs/[中文任务名]/07_TODO_[中文任务名].md`
- `docs/[中文任务名]/99_REFERENCES_[中文任务名].md`

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
