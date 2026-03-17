# Beginner Guide

`imperial-agent-governance` 是一个面向多 Agent 协作场景的 skill 包。

它的作用不是“替你写业务代码”，而是给 Agent 提供一套明确的治理流程，让复杂任务按角色分工推进：

- `taizi`：接收请求、识别意图、决定进入哪条流程
- `zhongshu`：做规划、拆解任务、设计方案
- `menxia`：做风险审查、质量把关
- `shangshu`：负责派发、协调和汇总
- 六部执行角色：按职责完成具体工作

如果你是第一次接触这个 skill，可以把它理解成：

> 给 AI 一套“先理解、再规划、必要时审核、最后执行”的协作规则。

---

## 1. 适合谁用

适合以下场景：

- 你想让 Agent 按角色分工来处理复杂任务
- 你需要规划、审议、执行分层的流程
- 你在做多 Agent 编排、任务委派、工作流治理
- 你想用 `@taizi` 作为统一入口来驱动复杂任务

不适合以下场景：

- 只是问一个简单问题
- 只需要单步执行的小任务
- 不希望引入额外流程和角色分工

---

## 2. 安装前准备

在 Codex 环境里，skill 一般安装到：

```text
~/.codex/skills/
```

安装完成后，目录结构应类似：

```text
~/.codex/skills/imperial-agent-governance/
├── SKILL.md
├── README.md
├── BEGINNER_GUIDE.md
├── LICENSE
├── PUBLISHING.md
└── references/
```

---

## 3. 安装方法

### 方法一：本地复制安装

如果你已经拿到了这个仓库的本地目录，直接复制到 skills 目录：

```bash
mkdir -p ~/.codex/skills
cp -R /path/to/imperial-agent-governance ~/.codex/skills/imperial-agent-governance
```

把 `/path/to/imperial-agent-governance` 换成你本地实际路径。

### 方法二：从 GitHub 下载后安装

1. 打开仓库下载 zip，或克隆仓库
2. 解压后确认根目录里有 `SKILL.md`
3. 把整个目录放到 `~/.codex/skills/imperial-agent-governance`

例如：

```bash
git clone https://github.com/awfaups/imperial-agent-governance.git
mkdir -p ~/.codex/skills
cp -R imperial-agent-governance ~/.codex/skills/imperial-agent-governance
```

### 安装后必须做的事

重启 Codex。

如果不重启，新安装的 skill 往往不会立刻生效。

---

## 4. 安装成功怎么确认

确认目录存在：

```bash
ls ~/.codex/skills/imperial-agent-governance
```

如果能看到：

- `SKILL.md`
- `references/`

说明文件已经放对位置了。

---

## 5. 第一次怎么用

这个 skill 最重要的入口是：

```text
@taizi
```

你可以把它理解成“总入口指令”。

### 最简单的使用方式

直接在对话里写：

```text
@taizi 帮我规划一个多 Agent 协作方案
```

或者：

```text
@taizi 帮我把这个复杂需求拆成规划、审核、执行三层
```

### skill 会做什么

收到 `@taizi` 后，系统通常会按这个顺序处理：

1. 识别你的任务属于什么类型
2. 判断要走哪条内部流程
3. 生成结构化任务卡
4. 交给 `zhongshu` 做方案和拆解
5. 如果任务风险高，再交给 `menxia`
6. 最后由 `shangshu` 协调执行角色

---

## 6. 常见触发方式

### 通用入口

```text
@taizi
```

这是最推荐的入口。

### 工作流别名

如果你已经知道自己要走哪类流程，也可以使用这些别名：

- `@plan`：任务规划
- `@risk`：风险评估
- `@audit`：架构 / 代码审计
- `@refactor`：渐进式重构
- `@6A`：新增功能开发
- `@6AYH`：渐进式优化
- `@PPW`：项目流程梳理

如果你不确定用哪个，直接用 `@taizi` 就够了。

---

## 7. 新手推荐的提问模板

### 模板 1：让它帮你规划

```text
@taizi 我要做一个复杂功能，请帮我按多 Agent 模式拆解
```

### 模板 2：让它做角色分工

```text
@taizi 帮我设计一个包含规划、审核、执行三层的协作流程
```

### 模板 3：让它做治理型分析

```text
@taizi 帮我评估这个任务是否需要审议和风险闸门
```

### 模板 4：指定你关心的约束

```text
@taizi 帮我规划这个需求，要求包含风险控制、执行顺序和交付标准
```

---

## 8. 一个完整例子

你输入：

```text
@taizi 我要做一个跨前端、文档和部署的复杂需求，请按多 Agent 模式帮我规划
```

通常会发生：

1. `taizi` 先整理目标和约束
2. `zhongshu` 给出拆解方案和执行顺序
3. 因为这是跨多个职责域的任务，所以可能经过 `menxia`
4. `shangshu` 再根据标签把任务分配给不同执行角色

对你来说，最直观的变化是：

- 输出会更结构化
- 任务边界更清晰
- 复杂任务不容易一上来就乱做

---

## 9. 常见问题

### Q1：为什么我用了以后感觉“步骤变多了”？

因为这个 skill 的目标不是“最快回答一句话”，而是让复杂任务更可控。

如果任务本来就很简单，就不应该强行用它。

### Q2：为什么推荐用 `@taizi`，而不是直接叫别的角色？

因为这个 skill 的规则就是：

- 外部请求只能从 `taizi` 进入
- 不能跳过入口，直接点名 `zhongshu`、`menxia` 或执行角色

这能避免角色越权和流程混乱。

### Q3：什么时候会进入 `menxia` 审议？

一般是这些情况：

- 风险高
- 跨多个职责域
- 涉及安全、部署、权限
- 验收标准不清楚

### Q4：安装了但没生效怎么办？

先检查三件事：

1. skill 是否放在 `~/.codex/skills/imperial-agent-governance`
2. 根目录是否真的有 `SKILL.md`
3. 是否已经重启 Codex

---

## 10. 推荐阅读顺序

如果你想进一步理解这个 skill，建议按这个顺序看：

1. [README.md](README.md)
2. [SKILL.md](SKILL.md)
3. [references/role-permissions.md](references/role-permissions.md)
4. [references/workflow-routing.json](references/workflow-routing.json)

---

## 11. 一句话总结

如果你是新手，记住这一条就够了：

```text
安装到 ~/.codex/skills/imperial-agent-governance，重启 Codex，然后用 @taizi 开始。
```
