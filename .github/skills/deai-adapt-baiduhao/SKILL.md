---
name: deai-adapt-baiduhao
description: '将母稿改写为百家号适配版本。使用时：需要将终稿改写成适合百度搜索流量的资讯风格。高信息密度、多用列表和数据、中立客观语气、减少第一人称情绪表达。'
user-invocable: true
---

# `deai-adapt-baiduhao` — 百家号改写

## Strategy
| 维度 | 适配方式 |
|------|----------|
| 标题风格 | 关键词前置、资讯体 |
| 语气倾向 | 中立客观，减少第一人称 |
| 段落特征 | 信息点密集，多用列表和分段 |
| 改写重点 | 信息密度高，多用列表和数据，减少个人情绪 |
| 结尾引导 | 自然收束，引导相关阅读 |

## Input
- `drafts/{选题名}/终稿.md`

## Output
- `drafts/{选题名}/百家号/文章.md`

## Reference
- 人设基线：`.github/instructions/persona-product-manager-shrimp.instructions.md`
