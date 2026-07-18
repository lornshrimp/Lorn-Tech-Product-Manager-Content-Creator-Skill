---
name: deai-hotspot
description: '从多个平台采集热点话题（微博、百度、知乎问题热榜、知乎推荐问题、知乎邀请问题、知乎想法话题、头条、B站、抖音）。使用时：需要获取今日热点榜单作为选题依据。跨来源去重、热度归一化，输出融合排名。'
user-invocable: true
---

# `deai-hotspot` — 热点采集

## When to Use
- 需要了解当前各平台的热点话题
- 为选题分析提供数据基础

## Input
- 用户指定来源类型（默认全量采集所有平台）

## Output
- `hotspot/榜单/{日期}-{来源}.md`（各来源原始榜单）
- `hotspot/榜单/{日期}-融合榜单.md`（跨平台聚合后的 TOP 榜单）

## Procedure

### 1. 确定采集来源
用户可指定，默认全量。支持来源：

| 来源 | 适配器文件 |
|------|-----------|
| 微博热搜榜 | `./references/adapter-weibo.md` |
| 百度热搜榜 | `./references/adapter-baidu.md` |
| 知乎问题热榜 | `./references/adapter-zhihu-q.md` |
| 知乎问题热榜 | `./references/adapter-zhihu-q.md` |
| 知乎推荐问题 | `./references/adapter-zhihu-recommend.md` |
| 知乎邀请问题 | `./references/adapter-zhihu-invited.md` |
| 知乎想法话题 | `./references/adapter-zhihu-idea.md` |
| 知乎想法热榜 | `./references/adapter-zhihu-p.md` |
| 头条热榜 | `./references/adapter-toutiao.md` |
| B站热门 | `./references/adapter-bilibili.md` |
| 抖音热点 | `./references/adapter-douyin.md` |

### 2. 按来源采集
对每个来源，按对应适配器说明访问页面、提取字段、标准化输出。

### 3. 执行融合

```text
① 读取当日所有 {来源}.md 文件
② 对标题做模糊相似度匹配（>0.80 视为同一热点）
③ 合并热度值（不同来源量纲归一化后加权平均）
④ 按融合热度排序，去重后输出 TOP 20
⑤ 标注"覆盖来源数"（如"微博+知乎"双平台上榜）
```

### 4. 输出文件

输出原始榜单（各来源独立文件）和融合榜单（聚合文件）。

融合榜单格式：

```markdown
# 融合热点榜单 · {日期}

采集来源：微博热搜 + 百度热搜 + 知乎问题热榜 + 头条热榜
采集时间：{时间}

## TOP 20 跨平台热点

| 排名 | 热点标题 | 融合热度 | 覆盖来源 | 时效性 | 最佳切入点 |
|------|----------|----------|----------|--------|-----------|
| 1 | xxx | 92.5 | 微博+百度+知乎 | 2h内 | 深度分析 |

## 各平台独立 TOP 10 速览
### 微博热搜榜
...(简略引用)

### 知乎问题热榜
...(简略引用)
```

## Calling Examples
```text
@deai-hotspot                   全量采集所有来源
@deai-hotspot 只采知乎问题热榜  仅采集知乎
@deai-hotspot 采微博和百度      指定来源
```
