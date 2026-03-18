---
name: imperial-agent-governance
description: Portable Agent Skills package for a role-based multi-agent workflow using taizi, zhongshu, menxia, shangshu, and worker departments. Use when the user wants multi-agent orchestration, role-based delegation, planning-review-dispatch pipelines, imperial-role collaboration patterns, or explicitly uses @taizi as the only public entry token.
description_zh: 这是一个可移植的 Agent Skills 包，用于基于 taizi、zhongshu、menxia、shangshu 和执行部门的角色化多 Agent 工作流。当用户需要多 Agent 编排、基于角色的委派、规划-审议-调度流水线、朝廷式分工协作模式，或显式使用 @taizi 作为唯一公开入口时使用。
metadata:
  short-description: Portable imperial agent governance workflow
  short-description_zh: 可移植的朝廷式 Agent 治理工作流
---

# Imperial Agent Governance
朝廷式 Agent 治理工作流

This skill defines a portable multi-agent operating model based on the roles `taizi`, `zhongshu`, `menxia`, `shangshu`, and the worker departments.
这个 skill 定义了一套可移植的多 Agent 协作模型，核心角色为 `taizi`、`zhongshu`、`menxia`、`shangshu` 和各执行部门。

This is the only skill that needs to be published for the portable package.
这是通用主包里唯一需要发布的 skill。
It includes the former `taizi` entry behavior inside the main skill instead of relying on a second trigger skill.
它已经把原先单独 `taizi` 入口 skill 的行为并入主 skill，不再依赖第二个触发 skill。

This package is designed to work as a self-contained Agent Skills package.
这个包被设计成一个自包含的 Agent Skills 包。
Do not assume Codex-specific global files such as `~/.codex/config.toml` or `~/.codex/AGENTS.md`.
不要假设运行环境一定有 `~/.codex/config.toml` 或 `~/.codex/AGENTS.md` 这类 Codex 专属全局文件。
Enforce role boundaries, routing rules, and workflow behavior through this skill and its references.
角色边界、路由规则和工作流行为，都应通过这个 skill 及其 references 自身来约束。

For bilingual files in this skill, prefer reading the English line first.
对于这个 skill 下的双语文件，优先读取英文行。
If the English content is already sufficient, skip the Chinese counterpart to save tokens.
如果英文内容已经足够，就跳过对应的中文内容以节省 token。
Read the Chinese counterpart only when exact Chinese wording is required or the English content is not enough.
只有在需要精确中文表述，或英文内容本身不够时，才读取对应的中文部分。
Treat Chinese lines as human-reference annotations by default, not as primary model context.
默认把中文行当作给人看的参考注释，而不是给模型读取的主上下文。

Use this skill when:
在以下场景使用这个 skill：

- the user wants multi-agent design or orchestration
- 用户需要多 Agent 设计或编排
- the user wants role-based delegation rules
- 用户需要基于角色的委派规则
- the user refers to imperial roles or ministry-based collaboration
- 用户提到朝廷式角色或六部协作
- the user wants a planner, reviewer, dispatcher, and worker split
- 用户需要规划、审议、调度、执行分层模型
- the user input contains `@taizi`
- 用户输入中包含 `@taizi`

Do not force this skill onto trivial single-step tasks.
不要把这个 skill 强行套到简单的一步式任务上。

## Workflow
工作流

### Entry rule
入口规则

`@taizi` is the only public entry token for this portable skill.
`@taizi` 是这个通用 skill 唯一允许的公开入口 token。
If the user input contains `@taizi`, treat that as explicit activation of this governance model.
如果用户输入中包含 `@taizi`，就把它视为显式启用这套治理模型。
No request may bypass directly to `zhongshu`, `menxia`, `shangshu`, or any worker department.
任何请求都不能直接绕过进入 `zhongshu`、`menxia`、`shangshu` 或执行部门。

Use this default path for substantial tasks:
对于重要任务，使用以下默认路径：

`taizi -> zhongshu -> menxia? -> shangshu -> worker(s) -> shangshu`

`taizi` must first classify the request into one of these internal modes:
`taizi` 必须先把请求归类到以下内部模式之一：

- `6A`: new feature development
- `6A`：新增功能开发
- `6AYH`: progressive optimization or refactor
- `6AYH`：渐进式优化或重构
- `PPW`: project inventory and process clarification
- `PPW`：项目盘点与流程梳理
- `generic governance`: all other substantial engineering tasks
- `generic governance`：其他需要工程治理的任务

If `taizi` auto-classifies the request as `6A`, `6AYH`, or `PPW`, output that workflow's activation response exactly as defined in the workflow references before continuing.
如果 `taizi` 自动将请求归类为 `6A`、`6AYH` 或 `PPW`，那么在继续之前，必须先按工作流参考文件中的定义原样输出对应激活响应语句。

For `6A`, `6AYH`, and `PPW`, the workflow's required documents are mandatory deliverables, not advisory examples.
对于 `6A`、`6AYH` 和 `PPW`，工作流中的必需文档是强制交付物，不是参考示例。
When one of these modes is selected, the workflow must initialize or update the required files under the current IDE project's root `docs/` directory before implementation proceeds.
当选中这些模式之一时，工作流必须先在当前 IDE / 当前打开项目根目录下的 `docs/` 目录中初始化或更新必需文件，然后才能进入实施阶段。
Use a dated task directory in the form `docs/YYYY_MM_DD_中文任务名/`.
文档目录必须使用带日期前缀的命名方式：`docs/YYYY_MM_DD_中文任务名/`。
Never place generated workflow docs inside the skill package repository itself unless that repository is the active project being worked on.
除非当前正在处理的项目本身就是这个 skill 仓库，否则禁止把工作流文档写到 skill 包仓库自身目录里。

### Stage guidance
阶段指引

- `taizi`: normalize the request, extract intent, assign title and tags
- `taizi`：规范化请求、提取意图、生成标题和标签
- `taizi`: include the selected workflow mode and required-document manifest in the first task card when mode is `6A`, `6AYH`, or `PPW`
- `taizi`：当模式为 `6A`、`6AYH` 或 `PPW` 时，在首张任务卡中包含工作流模式和必需文档清单
- `zhongshu`: decompose the task, define execution steps, choose likely worker departments
- `zhongshu`：拆解任务、定义执行步骤、选择可能参与的执行部门
- `zhongshu`: convert required documents into a document-bootstrap plan and stage ownership
- `zhongshu`：把必需文档转成可执行的文档初始化计划和阶段归属
- `menxia`: review for quality, risk, ambiguity, and policy fit; either reject to `zhongshu` or approve to `shangshu`
- `menxia`：从质量、风险、歧义和规则适配角度做审议；要么驳回给 `zhongshu`，要么批准给 `shangshu`
- `shangshu`: dispatch to workers, track returns, aggregate outputs
- `shangshu`：把任务派给执行部门、跟踪返回结果并做汇总
- `shangshu`: dispatch `libu` to create or update required workflow documents before code execution or final reporting
- `shangshu`：在进入代码执行或最终汇报前，先调度 `libu` 创建或更新工作流必需文档
- workers: execute within their domain and return only to `shangshu`
- 执行部门：只在自己的职责范围内执行，并且只能把结果回给 `shangshu`

## Source of truth
事实来源

Read these reference files when you need precise behavior:
需要精确定义时，请读取以下参考文件：

- `references/agents.json`
- `references/status-transitions.json`
- `references/handoff-record.schema.json`
- `references/role-permissions.md`
- `references/routing-rules.json`
- `references/task-card.schema.json`
- `references/role-prompts.json`
- `references/workflow-routing.json`
- `references/engineering-governance.md`
- `references/taizi-classification.md`

Read these workflow files when the selected internal mode needs them:
当选中的内部模式需要对应工作流细节时，请读取以下文件：

- `references/workflows/6a.md`
- `references/workflows/6ayh.md`
- `references/workflows/ppw.md`

Treat each workflow file's `Required documents` section as an execution contract.
把每个工作流文件中的 `Required documents` 部分视为执行契约。
If those files do not exist yet, create skeleton documents first.
如果这些文件还不存在，先创建骨架文档。
If they already exist, update them stage by stage instead of silently skipping them.
如果这些文件已经存在，就按阶段更新它们，而不是静默跳过。

## Routing policy
路由规则

Route from `shangshu` by tags:
由 `shangshu` 根据标签进行派单：

- code, bugfix, feature, algorithm, performance -> `bingbu`
- `code`、`bugfix`、`feature`、`algorithm`、`performance` -> `bingbu`
- docs, api, report, spec -> `libu`
- `docs`、`api`、`report`、`spec` -> `libu`
- data, cost, reporting, resource -> `hubu`
- `data`、`cost`、`reporting`、`resource` -> `hubu`
- security, compliance, audit -> `xingbu`
- `security`、`compliance`、`audit` -> `xingbu`
- deploy, cicd, tooling, automation -> `gongbu`
- `deploy`、`cicd`、`tooling`、`automation` -> `gongbu`
- agent, permission, training, registry -> `libu_hr`
- `agent`、`permission`、`training`、`registry` -> `libu_hr`

If no worker matches, return to `zhongshu` for replanning.
如果没有匹配到合适的执行部门，就回到 `zhongshu` 重新规划。

## Review policy
审议规则

Send the task through `menxia` when any of the following is true:
当满足以下任一条件时，任务必须经过 `menxia`：

- the task is high risk
- 任务风险较高
- the task spans multiple worker departments
- 任务跨多个执行部门
- the acceptance criteria are unclear
- 验收标准不清晰
- the task touches security, compliance, deployment, or permissions
- 任务涉及安全、合规、部署或权限

When `menxia` rejects or sends back a task, it must emit `rejection_reason` and, when applicable, `required_fixes`.
当 `menxia` 驳回或打回任务时，必须输出 `rejection_reason`，并在适用时给出 `required_fixes`。

## Task-card requirements
任务卡要求

Use a structured task card rather than a loose message. Required fields:
使用结构化任务卡，而不是松散的自由文本。必填字段如下：

- `task_id`
- `title`
- `from`
- `to`
- `goal`
- `brief`
- `tags`
- `constraints`
- `deliverables`
- `review_required`
- `workflow_mode`
- `current_stage`
- `required_documents`
- `document_status`
- `handoff_history`
- `status`

## Output discipline
输出纪律

- record why each handoff happened
- 记录每次 handoff 发生的原因
- ensure each handoff can be represented by `references/handoff-record.schema.json`
- 确保每次 handoff 都能落到 `references/handoff-record.schema.json` 定义的结构里
- every handoff must include a responsibility-transfer notice stating what the current role stops owning, what the next role starts owning, and what remains out of scope
- 每次 handoff 都必须带上职责转移提示，明确当前角色停止负责什么、下一角色开始负责什么、哪些内容仍然不在职责范围内
- for `6A`, `6AYH`, and `PPW`, record the required-document list in the first task card and keep the docs status visible in subsequent handoffs
- 对于 `6A`、`6AYH` 和 `PPW`，要在首张任务卡中记录必需文档清单，并在后续 handoff 中持续暴露文档状态
- only move task status according to `references/status-transitions.json`
- 只能按照 `references/status-transitions.json` 推进任务状态
- keep worker outputs scoped to their own domain
- 执行部门的输出必须严格限制在自身职责范围内
- aggregate final results in `shangshu`
- 最终结果必须由 `shangshu` 汇总
- do not start implementation for `6A` or `6AYH` until the workflow document skeletons are created
- 对于 `6A` 和 `6AYH`，在工作流文档骨架创建完成之前，不得开始实施
- do not advance `PPW` beyond inventory without its required project documents being initialized
- 对于 `PPW`，在项目必需文档初始化完成之前，不得推进到资产盘点之后的阶段
- do not let workers bypass the handoff graph
- 不允许执行部门绕过 handoff 图
- do not let workers close a task directly; workers return evidence, `shangshu` closes
- 不允许执行部门直接关单；执行部门只回传证据，由 `shangshu` 统一结案
- when a workflow needs a fixed activation response, output that response verbatim before continuing
- 当某个工作流要求固定激活响应时，必须先原样输出该响应再继续
- when in doubt about role boundaries, follow `references/role-permissions.md` before acting
- 当你不确定角色边界时，先遵循 `references/role-permissions.md` 再行动
- for bilingual references, avoid reading both language versions unless needed
- 对于双语参考内容，除非确有需要，否则不要同时读取两种语言版本
