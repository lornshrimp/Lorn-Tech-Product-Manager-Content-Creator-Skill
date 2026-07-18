---
name: deai-adapt-zhihu
description: '将母稿改写为知乎适配版本。使用时：需要将审核通过的终稿改写为适合知乎平台风格的文章。增加分析深度、补充数据引用、使用提问式标题、以开放式讨论结尾。'
user-invocable: true
---

# `deai-adapt-zhihu` — 知乎改写

## Strategy
| 维度 | 适配方式 |
|------|----------|
| 标题风格 | 提问句、观点式标题（"如何看待…？"） |
| 语气倾向 | 理性专业，第一人称但不过度个人化 |
| 段落特征 | 中等长度，允许 5-8 句深度论证段 |
| 改写重点 | 增加分析深度，补充数据引用 |
| 结尾引导 | 开放式提问，引导评论区讨论 |

## Input
- `drafts/{选题名}/终稿.md`（母稿）

## Output
- `drafts/{选题名}/知乎/文章.md`

## Reference
- 人设基线：`.github/instructions/persona-product-manager-shrimp.instructions.md`
