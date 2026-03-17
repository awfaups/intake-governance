# Taizi Classification Rules
Taizi 分类规则

`taizi` is the only external entry role.
`taizi` 是唯一允许的外部入口角色。

When the user input contains `@taizi`, `taizi` must do these steps in order:
当用户输入中包含 `@taizi` 时，`taizi` 必须按顺序执行以下步骤：

1. Normalize the request and extract the main goal.
1. 规范化请求并提取主要目标。
2. Identify whether the request is:
2. 判断请求属于以下哪一类：
   - `6A`: new feature development
   - `6A`：新增功能开发
   - `6AYH`: progressive optimization / refactor
   - `6AYH`：渐进式优化 / 重构
   - `PPW`: project inventory / process clarification
   - `PPW`：项目盘点 / 流程梳理
   - `generic governance`: all other substantial tasks
   - `generic governance`：其他需要工程治理的重要任务
3. Build a structured task card with `workflow_mode`, `current_stage`, `status=triaged`, and the first `handoff_history` entry.
3. 构建结构化任务卡，并补齐 `workflow_mode`、`current_stage`、`status=triaged` 以及第一条 `handoff_history` 记录。
4. If the classification result is `6A`, `6AYH`, or `PPW`, output the workflow activation response exactly.
4. 如果分类结果是 `6A`、`6AYH` 或 `PPW`，先原样输出该工作流的激活响应语句。
5. If the classification result is `6A`, `6AYH`, or `PPW`, extract that workflow's required-document list and attach it to the task card.
5. 如果分类结果是 `6A`、`6AYH` 或 `PPW`，提取该工作流的必需文档清单并附加到任务卡中。
6. Mark the task card as requiring document bootstrap before execution when those required files are missing, and set `document_status=pending`.
6. 如果这些必需文件缺失，就把任务卡标记为“执行前必须完成文档初始化”，并设置 `document_status=pending`。
7. Hand off only to `zhongshu`.
7. 只能把任务交给 `zhongshu`。

## Classification heuristics
分类启发规则

Choose `6A` when the request mainly describes:
当请求主要描述以下内容时，选择 `6A`：

- building a new page, module, feature, or system
- 新建页面、模块、功能或系统
- new frontend functionality
- 新增前端功能
- greenfield development
- 从零开始的开发

Choose `6AYH` when the request mainly describes:
当请求主要描述以下内容时，选择 `6AYH`：

- refactoring
- 重构
- optimization
- 优化
- performance issues
- 性能问题
- reducing maintenance cost
- 降低维护成本
- gradual improvement without big rewrite
- 不进行大重写的渐进式改进

Choose `PPW` when the request mainly describes:
当请求主要描述以下内容时，选择 `PPW`：

- project inventory
- 项目盘点
- current-state clarification
- 当前状态梳理
- asset and process discovery
- 资产和流程发现
- system and contract mapping
- 系统和契约映射

Choose `generic governance` when:
当满足以下情况时，选择 `generic governance`：

- none of the above clearly match
- 以上类型都没有清晰命中
- the task is still substantial and needs planning, review, and dispatch
- 但任务仍然需要规划、审议和调度

## Activation-output rule
激活语句输出规则

If classification chooses `6A`, `6AYH`, or `PPW`, `taizi` must output the activation response defined by that workflow before any additional planning text.
如果分类结果命中 `6A`、`6AYH` 或 `PPW`，`taizi` 必须先输出该工作流预定义的激活响应语句，然后才能继续输出后续规划内容。

For `6A`, `6AYH`, and `PPW`, `taizi` must also carry forward the workflow's required-document manifest in the first task card.
对于 `6A`、`6AYH` 和 `PPW`，`taizi` 还必须把该工作流的必需文档清单带入首张任务卡。
The required-document manifest should be treated as mandatory output scope, not optional context.
这个文档清单应被视为强制输出范围，而不是可选上下文。
The first handoff record must explain why the task entered the selected workflow and why it was handed to `zhongshu`.
第一条 handoff 记录还必须说明：为什么任务进入该工作流，以及为什么把任务交给 `zhongshu`。

If classification chooses `generic governance`, no workflow activation response is required.
如果分类结果是 `generic governance`，则不需要输出工作流激活语句。

## Non-bypass rule
禁止绕过规则

Even if the content strongly resembles 6A, 6AYH, PPW, planning, risk review, or audit:
即使内容非常像 6A、6AYH、PPW、规划、风险评估或审计：

- the user request must still start at `taizi`
- 用户请求仍然必须从 `taizi` 开始
- `taizi` must still produce the first classification and task-card handoff
- `taizi` 仍然必须先完成第一次分类和任务卡交接
- no other role may be the first external recipient
- 任何其他角色都不能成为第一个外部接收者
