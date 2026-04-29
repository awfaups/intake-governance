# Activation Examples

Use these examples to sanity-check triggering and classification behavior.

## Intake-first prompts

- `@intake 帮我把这个跨前后端发布流程拆成规划、评审和执行角色`
  - Expected mode: `generic_governance`
  - Expected activation: `通用治理工作流（GGW · Generic Governance Workflow）已激活`

- `@plan 请帮我做一个多 agent 的任务拆解和交接方案`
  - Expected handling: normalize to `intake`, then classify as `generic_governance` or `planning`

- `@risk 评估这次权限系统改造的发布风险，并决定是否要先过 review-gate`
  - Expected handling: normalize to `intake`, then classify as `generic_governance` or `risk_review`

## Workflow selection prompts

- `@6A 为订单后台新增一个退款详情页，并按工作流先出文档`
  - Expected mode: `6A`

- `@6AO 逐步优化这个首页组件，要求保留行为并控制回滚风险`
  - Expected mode: `6AO`

- `@PMW 先盘点这个项目的仓库、环境、流程和交接点`
  - Expected mode: `PMW`

- `@SDD 这次需求先走 spec-first，把规格、任务和验收链路定清楚`
  - Expected mode: `SDD`

- `@GGW 帮我把这个跨团队治理任务拆成规划、评审、派发和闭环`
  - Expected mode: `GGW`

## Natural-language prompts without aliases

- `我要从零开发一个管理后台模块，先按多角色流程推进`
  - Expected mode: `6A`

- `这个模块历史包袱很重，我想做渐进式重构和性能清理`
  - Expected mode: `6AO`

- `我现在连项目现状都不清楚，先把资产和流程摸清楚`
  - Expected mode: `PMW`

- `这次不要先写代码，先把规格、验收标准和任务拆解定下来`
  - Expected mode: `SDD`
