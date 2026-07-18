---
name: deai-adapt-toutiao
description: '将母稿改写为今日头条适配版本。使用时：需要将终稿改写为适合头条信息流读者的风格。短段落（每段≤3句）、开头必须设置钩子、高频小标题分割、快节奏口语化语气。'
user-invocable: true
---

# `deai-adapt-toutiao` — 头条改写

## Strategy
| 维度 | 适配方式 |
|------|----------|
| 标题风格 | 数字钩子、冲突式、悬念式 |
| 语气倾向 | 快节奏、直接、口语化 |
| 段落特征 | 短段落，每段 1-3 句，高频小标题 |
| 改写重点 | 缩短段落，开头必须有钩子，增加小标题分割 |
| 结尾引导 | 引导关注 + 收藏 |

## Input
- `drafts/{选题名}/终稿.md`

## Output
- `drafts/{选题名}/头条/文章.md`

## Reference
- 人设基线：`.github/instructions/persona-product-manager-shrimp.instructions.md`
