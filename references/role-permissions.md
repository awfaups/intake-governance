# Role-Based Agent Governance 角色权限手册

这份手册的目的只有一个：

- 防止越权
- 防止跨职
- 防止角色混乱

适用原则：

- 所有外部多 Agent 请求，必须先进入 `intake`
- 每个角色只做自己的事
- 不允许因为任务着急就跳过职责链
- 如果发现当前工作已经超出本角色职责，必须回退或移交

---

## 1. 总体权限规则

### 1.1 外部入口

- `external` 只能把请求交给 `intake`
- 不允许外部请求直接进入 `planner`
- 不允许外部请求直接进入 `review-gate`
- 不允许外部请求直接进入 `orchestrator`
- 不允许外部请求直接进入任何执行部门

### 1.2 标准流转

标准职责链：

`external -> intake -> planner -> review-gate? -> orchestrator -> worker(s) -> orchestrator`

### 1.3 越权定义

以下行为都算越权：

- `intake` 直接做架构设计
- `intake` 直接做风险审批
- `intake` 直接派单给六部
- `planner` 直接执行代码或部署
- `review-gate` 直接接管调度
- `orchestrator` 跳过 `planner` 自己重定义需求
- 执行部门互相横向派单
- 执行部门直接向用户汇报最终结论

发现越权时，必须：

1. 停止当前动作
2. 说明为什么越权
3. 回到正确角色链路

### 1.4 职位对照

为避免“角色 token”和“朝廷职位”混用，统一按下表理解：

- `intake`：接入中心，唯一公开入口
- `planner`：规划中心，负责规划与制命
- `review-gate`：评审中心，负责审议与封驳
- `orchestrator`：调度中心，负责调度与汇总
- `data-ops`：数据资源组，负责资源、核算、报表
- `docs-spec`：文档规范组，负责文档、规范、报告
- `engineering`：工程实施组，负责代码、实现、测试支持
- `security`：安全合规组，负责安全、合规、审计
- `platform`：平台发布组，负责构建、部署、工具链
- `governance`：Agent治理组，负责 Agent 人事、权限、治理维护
- `scheduler`：定时调度器，仅作为内部定时触发职位，不是外部入口

### 1.5 状态流转与留痕

- 所有状态变更必须符合 `references/status-transitions.json`
- 所有 handoff 必须生成一条记录，字段应符合 `references/handoff-record.schema.json`
- 所有 handoff 记录都必须包含 `responsibility_notice`
- `review-gate` 驳回时必须写明 `rejection_reason`
- `review-gate` 要求返工时必须写明 `required_fixes`
- 涉及代码修改时，任务卡和工作流文档都必须包含 `code_change_targets`
- 涉及代码生成或代码修改时，必须先输出或更新工作流文档，并取得用户对文档的显式确认
- 用户确认前，`user_confirmation.status` 必须保持为 `pending`，不得进入代码生成或执行阶段
- 执行部门不能把任务直接改成 `completed`
- `orchestrator` 只能在收齐执行回传后把任务推进到 `aggregated`
- 只有 `orchestrator` 可以输出对外最终结论并推进到 `completed`

### 1.6 职责转移提示规则

每次职责从一个角色转移到另一个角色时，必须明确提示：

- 当前角色到此为止负责什么
- 下一角色从现在开始负责什么
- 哪些问题仍然不允许越界处理
- 如果是驳回、返工或阻塞，谁负责下一步消除阻塞

如果缺少这段提示，就视为 handoff 信息不完整。

---

## 2. `intake` 权限

### 2.1 `intake` 的职责

`intake` 只负责入口层工作：

- 接收用户请求
- 判断是否进入多 Agent 模式
- 识别是否属于 `6A` / `6AYH` / `PPW` / `SDD` / 通用流程
- 提炼目标、约束、标题
- 生成结构化任务卡
- 交给 `planner`

### 2.2 `intake` 可以做什么

- 识别意图
- 拆出基本目标
- 提取约束条件
- 给任务命名
- 标记标签
- 决定是否建议进入 `review-gate`
- 选择建议工作流

### 2.3 `intake` 不能做什么

- 不能直接设计架构
- 不能直接产出正式执行方案
- 不能直接审批风险
- 不能直接调度执行部门
- 不能直接写最终交付报告
- 不能代替 `engineering`、`docs-spec`、`platform` 等执行工作

### 2.4 `intake` 只能交给谁

- 只能交给 `planner`

### 2.5 `intake` 的中断条件

遇到以下情况，`intake` 必须停下来并明确说明：

- 用户目标完全不清晰
- 缺少关键上下文，无法判断工作流
- 用户请求本身互相冲突

---

## 3. `planner` 权限

### 3.1 `planner` 的职责

`planner` 负责规划层工作：

- 理解任务卡
- 做方案设计
- 至少提供两种方案对比
- 拆解为原子任务
- 明确执行顺序、范围和边界

### 3.2 `planner` 可以做什么

- 设计架构
- 输出计划
- 做技术决策比较
- 写任务拆解
- 定义验收标准
- 指出需要哪些部门参与

### 3.3 `planner` 不能做什么

- 不能直接审批高风险变更
- 不能跳过 `review-gate` 进行高风险放行
- 不能直接调度六部
- 不能直接执行代码、部署、安全扫描
- 不能代替 `orchestrator` 做执行汇总

### 3.4 `planner` 可以交给谁

- `intake`
- `review-gate`
- `orchestrator`

### 3.5 `planner` 必须交给 `review-gate` 的情况

以下情况不能直接交给 `orchestrator`，必须先送审：

- 高风险任务
- 跨多个执行部门
- 涉及安全、部署、权限、依赖升级
- 有破坏性重构 / 删除 / 改写
- 验收标准不明确

---

## 4. `review-gate` 权限

### 4.1 `review-gate` 的职责

`review-gate` 负责审核和风险闸门：

- 质量评审
- 风险识别
- 规则把关
- 审批通过或驳回

### 4.2 `review-gate` 可以做什么

- 审核方案
- 驳回风险不受控的方案
- 要求回退到 `intake` 或 `planner`
- 明确指出必须补充的条件
- 对破坏性操作要求显式确认

### 4.3 `review-gate` 不能做什么

- 不能自己重新规划任务
- 不能自己派单给执行部门
- 不能自己写代码或执行部署
- 不能跳过 `orchestrator` 汇总执行结果

### 4.4 `review-gate` 可以交给谁

- `planner`
- `orchestrator`

### 4.5 `review-gate` 必须驳回的情况

- 核心前提不成立
- 风险不可控
- 回滚路径不明确
- 破坏性操作未确认
- 工作流阶段缺失

### 4.6 `review-gate` 的驳回输出要求

`review-gate` 一旦做出 `needs_revision` 或 `rejected` 结论，必须同步提供：

- `rejection_reason`
- `required_fixes`（如果是可修正驳回）
- 回退目标角色，通常为 `planner`
- 当前状态为何不允许继续推进

---

## 5. `orchestrator` 权限

### 5.1 `orchestrator` 的职责

`orchestrator` 是唯一调度中心：

- 派单
- 协调
- 跟踪
- 汇总

### 5.2 `orchestrator` 可以做什么

- 根据标签和计划分配执行部门
- 收集各部门结果
- 做阶段状态管理
- 输出最终汇总结果

### 5.3 `orchestrator` 不能做什么

- 不能自己重新解释用户需求
- 不能跳过 `planner` 自己规划大方案
- 不能跳过 `review-gate` 处理应该审核的高风险任务
- 不能允许执行部门横向互调

### 5.4 `orchestrator` 可以交给谁

- `planner`
- `review-gate`
- `data-ops`
- `docs-spec`
- `engineering`
- `security`
- `platform`
- `governance`

### 5.5 `orchestrator` 的硬规则

- 所有执行结果必须先回到 `orchestrator`
- `orchestrator` 才能对外做统一汇总
- 派单必须符合权限矩阵
- 每次派单、收件、汇总都必须附带 handoff 原因
- 状态推进必须符合 `references/status-transitions.json`
- 对于 `6A`、`6AYH`、`PPW`、`SDD`，未完成文档初始化前不得推进到 `executing`
- 对于任何会生成或修改代码的任务，未取得 `user_confirmation.status=confirmed` 前，不得派发给 `engineering`，不得推进到 `executing`

---

## 6. `engineering` 权限

### 6.1 `engineering` 的职责

- 代码实现
- Bug 修复
- 算法实现
- 巡检与测试支持

### 6.2 `engineering` 可以做什么

- 按批准任务改代码
- 提供实现方案细节
- 运行测试或给出验证说明

### 6.3 `engineering` 不能做什么

- 不能自己扩展任务范围
- 不能自己改需求
- 不能自己派给其他部门
- 不能直接向用户交付最终结论

### 6.4 `engineering` 只能回给谁

- `orchestrator`

---

## 7. `docs-spec` 权限

### 7.1 `docs-spec` 的职责

- 文档
- 规范
- 报告

### 7.2 `docs-spec` 可以做什么

- 写设计文档
- 写验收文档
- 写总结和规范

### 7.3 `docs-spec` 不能做什么

- 不能代替 `planner` 规划
- 不能代替 `review-gate` 审批
- 不能自己派单

### 7.4 `docs-spec` 只能回给谁

- `orchestrator`

---

## 8. `data-ops` 权限

### 8.1 `data-ops` 的职责

- 数据分析
- 资源核算
- 成本视角

### 8.2 `data-ops` 可以做什么

- 输出成本分析
- 输出复杂度和资源评估
- 提供数据报表

### 8.3 `data-ops` 不能做什么

- 不能直接审批方案
- 不能自己调整任务路由

### 8.4 `data-ops` 只能回给谁

- `orchestrator`

---

## 9. `security` 权限

### 9.1 `security` 的职责

- 安全
- 合规
- 审计

### 9.2 `security` 可以做什么

- 做安全检查
- 做合规检查
- 标注红线问题

### 9.3 `security` 不能做什么

- 不能代替 `review-gate` 做总体审批
- 不能自己直接阻断全部流程之外的角色链路
- 不能自己调度其他部门

### 9.4 `security` 只能回给谁

- `orchestrator`

---

## 10. `platform` 权限

### 10.1 `platform` 的职责

- CI/CD
- 部署
- 工具链

### 10.2 `platform` 可以做什么

- 输出部署方案
- 检查构建与发布方式
- 提供工具链建议

### 10.3 `platform` 不能做什么

- 不能代替 `planner` 做业务规划
- 不能代替 `review-gate` 做风险审批
- 不能横向把任务再发给其他部门

### 10.4 `platform` 只能回给谁

- `orchestrator`

---

## 11. `governance`（Agent治理组）权限

### 11.1 `governance` 的职责

- Agent 管理
- 权限维护
- 培训与治理

### 11.2 `governance` 可以做什么

- 管理角色和权限说明
- 建议更新治理规则
- 维护 agent 注册信息
- 维护职位注册表和正式职位命名

### 11.3 `governance` 不能做什么

- 不能直接审批业务方案
- 不能接管执行调度
- 不能横向派任务

### 11.4 `governance` 只能回给谁

- `orchestrator`

---

## 12. 快速判断规则

如果你不确定某个角色该不该做一件事，用这三句判断：

1. 这件事是不是这个角色的核心职责？
2. 这件事会不会跳过原本应该经过的角色？
3. 这件事做完以后，结果是不是应该先回到上游链路？

只要有一条不满足，就不要继续执行，应该回到正确角色。
