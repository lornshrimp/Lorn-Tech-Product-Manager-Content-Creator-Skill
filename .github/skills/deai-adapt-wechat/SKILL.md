---
name: deai-adapt-wechat
description: '将母稿改写为微信公众号适配版本。使用时：需要将终稿改写为适合公众号订阅粉丝阅读的风格。强化个人叙事、多用"我"的视角、故事化开头、增加互动引导（在看/转发/关注）。'
user-invocable: true
---

# `deai-adapt-wechat` — 公众号改写

## Strategy
| 维度 | 适配方式 |
|------|----------|
| 标题风格 | 悬念式、故事钩子式 |
| 语气倾向 | 亲切个人，像朋友聊天 |
| 段落特征 | 中短段落，适合手机阅读 |
| 改写重点 | 强化个人叙事，多用"我"的视角，增加互动引导 |
| 结尾引导 | 引导在看+转发+关注 |

## Input
- `drafts/{选题名}/终稿.md`

## Output
- `drafts/{选题名}/公众号/文章.md`

## Reference
- 人设基线：`.github/instructions/persona-product-manager-shrimp.instructions.md`
