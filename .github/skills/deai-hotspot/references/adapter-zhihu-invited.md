# 知乎邀请问题适配器

## 页面信息
- URL：`https://www.zhihu.com/creator/featured-question/invited`
- 类型：知乎邀请问题
- 状态：✅ 验证可用（需登录）

## 操作步骤

1. 在浏览器中登录知乎账号
2. 打开 `https://www.zhihu.com/creator/featured-question/invited`
3. 等待页面加载完成
4. 使用 Playwright `page.evaluate()` 从 DOM 中提取邀请问题列表

```javascript
// Playwright 提取代码
return await page.evaluate(() => {
  const results = [];
  const allText = document.body.innerText;
  const lines = allText.split('\n').filter(l => l.trim().length > 5);
  
  // 提取带回答数和关注数的问题条目
  const questionPattern = /(.{6,80}？)\s*(\d+)\s*回答\s*·\s*(\d[\d,]*)\s*关注/;
  for (const line of lines) {
    const match = line.match(questionPattern);
    if (match) {
      results.push({
        问题标题: match[1],
        回答数: match[2],
        关注数: match[3]
      });
    }
  }
  return results.slice(0, 20);
});
```

## 提取字段
| 字段 | 说明 | 示例 |
|------|------|------|
| 问题标题 | 邀请回答的问题标题 | 如何看待Kimi K3模型价格翻5倍？ |
| 回答数 | 当前已有回答数 | 53 |
| 关注数 | 关注该问题的人数 | 153 |

## 输出格式
```markdown
# 知乎邀请问题 · {日期}

采集时间：{时间}

| 序号 | 问题标题 | 回答数 | 关注数 |
| --- | --- | --- | --- |
| 1 | xxx？ | 53 | 153 |
```

## 注意事项
- **必须先在浏览器中登录知乎账号**
- 邀请问题是平台邀请当前用户回答的问题，**非热榜排名**，但可反映平台当前讨论方向
- a11y 快照仅显示导航侧栏，主内容需使用 Playwright DOM 提取
- 页面会混合展示"邀请回答"和"推荐问题"两个标签页的内容
