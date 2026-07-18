---
name: deai-adapt-csdn
description: '将母稿改写为 CSDN/掘金适配版本。使用时：需要将终稿改写成适合技术从业者阅读的风格。突出方法论和实操步骤、减少抒情、结构化排版、以收藏和评论引导结尾。'
user-invocable: true
---

# `deai-adapt-csdn` — CSDN/掘金改写

## Strategy
| 维度 | 适配方式 |
|------|----------|
| 标题风格 | 方法论式、步骤式 |
| 语气倾向 | 专业、简明、实操导向 |
| 段落特征 | 结构化，多用代码/流程图/列表 |
| 改写重点 | 突出方法论和实操，减少抒情，增加技术细节 |
| 结尾引导 | 引导收藏 + 评论交流 |

## Input
- `drafts/{选题名}/终稿.md`

## Output
- `drafts/{选题名}/CSDN/文章.md`

## Reference
- 人设基线：`.github/instructions/persona-product-manager-shrimp.instructions.md`
