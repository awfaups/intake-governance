# Beginner Guide 中文版

> 这份文档给人看，不作为模型入口说明。

## 1. 这个 skill 是做什么的

`intake-governance` 是一个面向多 Agent 协作场景的 skill 包。

它的作用不是“替你写业务代码”，而是给 Agent 提供一套明确的治理流程，让复杂任务按角色分工推进：

- `intake`：接收请求、识别意图、决定进入哪条流程
- `planner`：做规划、拆解任务、设计方案
- `review-gate`：做风险审查、质量把关
- `orchestrator`：负责派发、协调和汇总
- 执行角色：按职责完成具体工作

当前仓库除了主 skill，还拆出了 4 个独立 workflow skill：

- `workflow-6a`
- `workflow-6ayh`
- `workflow-ppw`
- `workflow-sdd`

如果你第一次接触它，可以把它理解成：

> 给 AI 一套“先理解、再规划、必要时审核、最后执行”的协作规则。

## 2. 适合谁用

适合以下场景：

- 你想让 Agent 按角色分工来处理复杂任务
- 你需要规划、审议、执行分层的流程
- 你在做多 Agent 编排、任务委派、工作流治理
- 你想用 `@intake` 作为统一入口来驱动复杂任务

不适合以下场景：

- 只是问一个简单问题
- 只需要单步执行的小任务
- 不希望引入额外流程和角色分工

## 3. 安装位置

在 Codex 环境里，skill 一般安装到：

```text
~/.codex/skills/
```

安装完成后，目录结构应类似：

```text
~/.codex/skills/intake-governance/
├── README.md
├── SKILL.md
├── OVERVIEW.md
├── OVERVIEW.zh-CN.md
├── BEGINNER_GUIDE.md
├── BEGINNER_GUIDE.zh-CN.md
├── LICENSE
├── PUBLISHING.md
├── agents/
├── references/
├── scripts/
└── skills/
```

## 4. 安装方法

### 方法一：本地复制安装

```bash
mkdir -p ~/.codex/skills
cp -R /path/to/intake-governance ~/.codex/skills/intake-governance
```

把 `/path/to/intake-governance` 换成你本地实际路径。

### 方法二：从 GitHub 下载后安装

```bash
git clone https://github.com/awfaups/intake-governance.git
mkdir -p ~/.codex/skills
cp -R intake-governance ~/.codex/skills/intake-governance
```

安装后必须重启 Codex，不然新安装的 skill 往往不会立刻生效。

## 5. 安装成功怎么确认

执行：

```bash
ls ~/.codex/skills/intake-governance
```

如果能看到：

- `SKILL.md`
- `references/`
- `skills/`

说明文件已经放对位置了。

## 6. 第一次怎么用

这个 skill 最重要的入口是：

```text
@intake
```

最简单的使用方式：

```text
@intake 帮我规划一个多 Agent 协作方案
```

或者：

```text
@intake 帮我把这个复杂需求拆成规划、审核、执行三层
```

## 7. 它会怎么工作

收到 `@intake` 后，系统通常会按这个顺序处理：

1. 识别你的任务属于什么类型
2. 判断要走哪条内部流程
3. 生成结构化任务卡
4. 把 workflow 文档写到你当前打开项目根目录下的 `docs/` 目录
5. 先把文档包输出给你确认
6. 你明确确认后，才由 `orchestrator` 协调代码生成或代码修改

最新的门禁要求是：

- `6A`、`6AYH`、`PPW`、`SDD` 都要先输出工作流文档包
- 文档目录格式统一为 `docs/YYYY_MM_DD_中文任务名_vN/`
- 涉及代码修改时，文档必须写清楚文件路径、行号范围、修改前代码片段和修改后代码片段
- 用户确认前，`user_confirmation.status` 必须保持 `pending`
- 没有确认前，不得派发 `engineering`，也不得生成或修改代码

这里的 `docs/` 指的是你当前 IDE 里正在处理的那个项目根目录，不是这个 skill 包安装目录。

对于 `SDD`，当前细化后的内部阶段顺序是：

`Init -> Explore -> Propose -> Spec -> Plan -> Design -> Atomize -> Approve -> Execute -> Verify -> Archive`

但你仍然不需要从外部直接进入这些阶段。它们是 `@intake` 驱动的 SDD 工作流内部细节层。

## 8. 常见触发方式

### 通用入口

```text
@intake
```

### 工作流别名

- `@plan`：任务规划
- `@risk`：风险评估
- `@audit`：架构 / 代码审计
- `@refactor`：渐进式重构
- `@6A`：新增功能开发
- `@6AYH`：渐进式优化
- `@PPW`：项目流程梳理
- `@sdd`：规格驱动开发

如果你想让它更稳定地跑 `SDD`，可以把规格文档按这个模板生成：

- [references/templates/01_SPEC.template.md](references/templates/01_SPEC.template.md)

对于非简单的 SDD 任务，也可以补充这些支持文档：

- `00_INIT_CONTEXT_项目接入.md`
- `00_EXPLORE_现状分析.md`
- `00_PROPOSE_变更提案.md`
- `09_ARCHIVE_归档记录.md`

如果你不确定用哪个，直接用 `@intake` 就够了。

## 9. 新手推荐的提问模板

### 模板 1：让它帮你规划

```text
@intake 我要做一个复杂功能，请帮我按多 Agent 模式拆解
```

### 模板 2：让它做角色分工

```text
@intake 帮我设计一个包含规划、审核、执行三层的协作流程
```

### 模板 3：让它做治理型分析

```text
@intake 帮我评估这个任务是否需要审议和风险闸门
```

### 模板 4：指定你关心的约束

```text
@intake 帮我规划这个需求，要求包含风险控制、执行顺序和交付标准
```

## 10. 常见问题

### 为什么感觉步骤变多了

因为这个 skill 的目标不是“最快回答一句话”，而是让复杂任务更可控。

如果任务本来就很简单，就不应该强行用它。

### 为什么推荐用 `@intake`

因为这套规则要求：

- 外部请求只能从 `intake` 进入
- 不能跳过入口，直接点名 `planner`、`review-gate` 或执行角色

这样可以避免角色越权和流程混乱。

### 什么时候会进入 `review-gate`

一般是这些情况：

- 风险高
- 跨多个职责域
- 涉及安全、部署、权限
- 验收标准不清楚

### 安装了但没生效怎么办

先检查三件事：

1. skill 是否放在 `~/.codex/skills/intake-governance`
2. 根目录是否真的有 `SKILL.md`
3. 是否已经重启 Codex

## 11. 推荐阅读顺序

建议按这个顺序看：

1. [OVERVIEW.zh-CN.md](OVERVIEW.zh-CN.md)
2. [OVERVIEW.md](OVERVIEW.md)
3. [role-permissions.md](references/role-permissions.md)
4. [workflow-routing.json](references/workflow-routing.json)

## 12. 一句话总结

如果你是新手，记住这一条就够了：

> 复杂任务先找 `@intake`，简单任务别强行走多 Agent。
