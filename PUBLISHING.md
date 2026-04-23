# Publishing Guide

本文件用于把 `intake-governance` 整理成一个适合公开分发，并可被 SkillsMP 收录的 skill 仓库。

## 发布目标

目标不是把它发布成官方 OpenAI Skills 市场条目，而是把它做成一个可公开索引的 GitHub skill 仓库，供 SkillsMP 等第三方目录站点发现和展示。

## 当前仓库状态

当前仓库已经满足的条件：

- 根目录包含 `README.md` 与 `SKILL.md`
- `SKILL.md` 包含可读的 frontmatter
- skill 名称和描述已经明确
- 有首页总览文档 `README.md`，以及补充说明文档 `OVERVIEW.md`
- 已包含独立 workflow skills、`references/`、`scripts/` 和 `agents/openai.yaml`
- skill 依赖的 references 已经内置在仓库中

当前仍建议补齐的项：

- 公开 GitHub 仓库
- GitHub topics
- 发布后的收录验证

## SkillsMP 最小收录要求

按 SkillsMP 的公开说明，通常至少需要：

1. 一个公开 GitHub 仓库
2. 根目录存在 `SKILL.md`
3. `SKILL.md` 中带有清晰的名称与描述
4. GitHub 仓库添加 topic：
   - `claude-skills`
   - 或 `claude-code-skill`

建议两个都加，但最少应加 `claude-skills`。

## 推荐仓库设置

在 GitHub 仓库页面建议这样配置：

- Visibility: `Public`
- Description:
  `Portable multi-agent governance skill for role-based planning, review, dispatch, and execution.`
- Website:
  可留空，或填写 SkillsMP 页面地址
- Topics:
  - `claude-skills`
  - `claude-code-skill`
  - `multi-agent`
  - `agent-governance`
  - `workflow`
  - `orchestration`

## 当前 LICENSE

这个仓库当前使用 `MIT` 许可证，便于公开传播和二次复用。

常见选择：

- `MIT`
  最宽松，便于传播和复用
- `Apache-2.0`
  比 MIT 更正式，包含专利授权条款
- `CC-BY-4.0`
  更偏文档 / 内容共享，不太适合代码仓库主授权

如果后续你希望在授权条款上更强调专利授权和正式性，可以改为 `Apache-2.0`。

## 发布步骤

### 1. 推送到 GitHub

示例：

```bash
git remote add origin https://github.com/awfaups/intake-governance.git
git push -u origin main
```

### 2. 将仓库设为公开

在 GitHub 仓库设置页将仓库可见性改为 `Public`。

### 3. 添加 topics

在 GitHub 仓库首页右侧的 `About` 区域点击齿轮，添加：

- `claude-skills`
- `claude-code-skill`
- `multi-agent`
- `agent-governance`
- `workflow`

### 4. 检查默认展示内容

确认以下内容在仓库首页可直接看到：

- `README.md`
- `OVERVIEW.md`
- `SKILL.md`
- `references/`

## 推荐短英文简介

可直接用于 GitHub description、SkillsMP 展示文案或 release 摘要：

`Portable multi-agent governance skill for role-based planning, review, dispatch, and execution.`

### 5. 等待 SkillsMP 同步

SkillsMP 采用周期性同步，不是实时上架。发布后通常需要等待下一轮同步。

## 上线前自检清单

- [ ] 仓库为公开 GitHub 仓库
- [ ] `README.md` 能说明 skill 的用途、入口、安装与校验方式
- [ ] 根目录存在 `SKILL.md`
- [ ] `SKILL.md` frontmatter 至少包含 `name` 和 `description`
- [ ] `OVERVIEW.md` 能说明 skill 的用途、入口和目录结构
- [ ] skill 引用的文件都已提交
- [ ] GitHub topics 已添加
- [x] 已选择并提交 `LICENSE`

## 上线后验证

发布完成后，建议验证：

1. 访客未登录 GitHub 时是否能正常打开仓库
2. `README.md` 是否已展示最新英文/中文说明
3. 直接打开 `SKILL.md` 是否能看到正确的 frontmatter
4. `OVERVIEW.md` 是否清楚说明如何使用
5. SkillsMP 下一轮同步后是否能搜索到 `intake-governance`

## 建议的后续增强

为了提高公开收录后的可理解性，可以继续补充：

- 一个更短的英文版简介
- 示例 prompt 集合
- 版本发布说明
- skill 预览截图或流程图
