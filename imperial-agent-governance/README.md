# Imperial Agent Governance

Portable multi-agent governance skill for role-based planning, review, dispatch, and execution.

一个可移植的多 Agent 治理 skill 包，用于基于 `taizi`、`zhongshu`、`menxia`、`shangshu` 与执行部门的角色化协作流程。

这个仓库不是应用程序，也不是 SDK，而是一套可复用的治理规则、工作流参考和任务卡约束，适合在 Agent Skills 场景中直接挂载使用。

## 适用场景

在以下场景启用这套模型：

- 多 Agent 设计或编排
- 基于角色的任务委派
- 规划 / 审议 / 调度 / 执行分层协作
- 工程治理型流程，如规划、审计、风险评估、重构治理
- 用户显式输入 `@taizi`

对于简单的一步式请求，不应强行套用这套多 Agent 流程。

## 核心原则

- `taizi` 是唯一允许的外部入口
- 外部请求不能直接进入 `zhongshu`、`menxia`、`shangshu` 或执行部门
- 标准流转链路为 `taizi -> zhongshu -> menxia? -> shangshu -> worker(s) -> shangshu`
- 执行部门只能向 `shangshu` 回传结果，禁止横向派单
- 高风险、跨部门、目标不清或涉及安全 / 部署 / 权限的任务必须经过 `menxia`

## 角色分工

| 角色 | 职责 |
| --- | --- |
| `taizi` | 入口接收、需求归一、标题标准化、工作流识别 |
| `zhongshu` | 规划、拆解、方案设计、验收标准定义 |
| `menxia` | 风险审议、质量把关、批准或驳回 |
| `shangshu` | 派发、协调、汇总、状态跟踪 |
| `hubu` | 数据、资源、核算、报表 |
| `libu` | 文档、规范、报告 |
| `bingbu` | 代码、功能开发、Bug 修复、巡检 |
| `xingbu` | 安全、合规、审计 |
| `gongbu` | 部署、CI/CD、工具、自动化 |
| `libu_hr` | Agent 注册、权限、培训、治理维护 |

## 支持的工作流别名

入口仍然由 `taizi` 统一接管，但可根据别名路由到不同治理模式：

- `@init`：项目初始化分析
- `@plan`：任务规划
- `@refactor`：渐进式重构
- `@risk`：风险评估
- `@decision`：技术决策
- `@audit`：架构 / 代码审计
- `@ask`：快速问题拆解
- `@ppw` / `@PPW`：项目流程梳理
- `@6A`：新增功能开发
- `@6AYH`：渐进式优化

当请求内容匹配 `6A`、`6AYH` 或 `PPW` 的自动识别信号时，`taizi` 也应先输出对应工作流规定的激活响应，再继续内部流转。

## 标签到执行部门的默认路由

- `code`、`bugfix`、`feature`、`algorithm`、`performance` -> `bingbu`
- `docs`、`api`、`report`、`spec` -> `libu`
- `data`、`cost`、`reporting`、`resource` -> `hubu`
- `security`、`compliance`、`audit` -> `xingbu`
- `deploy`、`cicd`、`tooling`、`automation` -> `gongbu`
- `agent`、`permission`、`training`、`registry` -> `libu_hr`

如果没有合适的执行部门，任务应回退到 `zhongshu` 重新规划。

## 任务卡要求

推荐使用结构化任务卡，而不是自由文本委派。至少包含以下字段：

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
- `status`

完整 schema 见 [references/task-card.schema.json](references/task-card.schema.json)。

## 目录结构

```text
.
├── SKILL.md
└── references
    ├── agents.json
    ├── engineering-governance.md
    ├── role-permissions.md
    ├── role-prompts.json
    ├── routing-rules.json
    ├── taizi-classification.md
    ├── task-card.schema.json
    ├── workflow-routing.json
    └── workflows
        ├── 6a.md
        ├── 6ayh.md
        └── ppw.md
```

## 关键文件说明

- [SKILL.md](SKILL.md)：主 skill 定义、启用条件、总流程、读取策略
- [references/agents.json](references/agents.json)：角色定义与可收发关系
- [references/role-permissions.md](references/role-permissions.md)：越权边界与强制职责链
- [references/workflow-routing.json](references/workflow-routing.json)：别名、自动分类信号、激活响应
- [references/task-card.schema.json](references/task-card.schema.json)：任务卡 JSON Schema
- [references/workflows/6a.md](references/workflows/6a.md)：新增功能开发工作流
- [references/workflows/6ayh.md](references/workflows/6ayh.md)：渐进式优化工作流
- [references/workflows/ppw.md](references/workflows/ppw.md)：项目流程梳理工作流

## 最小使用示例

用户输入：

```text
@taizi 帮我规划一个跨前端、文档和部署的功能开发流程
```

期望行为：

1. `taizi` 识别请求并归一化标题、目标、约束
2. `zhongshu` 拆解方案、划分执行阶段、定义验收标准
3. `menxia` 在跨部门或高风险场景下进行审议
4. `shangshu` 根据标签派发到相应执行部门
5. 执行部门仅在各自职责范围内产出，并统一回传给 `shangshu`

## 设计目标

- 可移植：不依赖特定平台的全局配置文件
- 可治理：通过显式 handoff 图防止越权和角色混乱
- 可扩展：通过引用文件维护工作流、路由规则和任务卡 schema
- 可复用：适合作为独立 skill 包对外发布或集成到其他 Agent 体系

## 发布到 SkillsMP

如果你希望把这个 skill 公开分发给其他人，可以参考 [PUBLISHING.md](PUBLISHING.md)。

最低要求如下：

- 将仓库发布到公开 GitHub 仓库
- 保留根目录下的 `SKILL.md`
- 为 GitHub 仓库添加 topic：`claude-skills`
- 可选再添加 topic：`claude-code-skill`
- 等待 SkillsMP 周期性同步收录

当前仓库已附带 `MIT` 许可证，便于别人明确复用范围。
