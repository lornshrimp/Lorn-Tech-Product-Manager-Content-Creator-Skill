# 微博热搜榜适配器

## 页面信息
- URL：`https://weibo.com/hot/search`（浏览器登录后可用）
- 类型：微博热搜榜
- 状态：✅ 验证可用（需登录）

## 已知不可用的 URL（记录避免重复尝试）
- `https://weibo.com/ajax/side/hotSearch` — API 接口，返回 403（无论是否登录）
- `https://s.weibo.com/top/summary` — 重定向到 passport 登录页

## 操作步骤

1. 在浏览器中登录微博账号
2. 打开 `https://weibo.com/hot/search`
3. **等待页面加载完成**（约 3 秒）
4. 使用 Playwright `page.evaluate()` 从 DOM 中提取热搜列表

```javascript
// Playwright 提取代码
return await page.evaluate(() => {
  const items = document.querySelectorAll('[class*="Hot"] [class*="hot"] a, [class*="HotList"] [class*="item"]');
  // 或者用更通用的方式：
  const walker = document.createTreeWalker(document.body, 4, null, false);
  const texts = [];
  let node;
  while (node = walker.nextNode()) {
    const t = node.textContent.trim();
    if (t && t.length > 2 && t.length < 80) texts.push(t);
  }
  // 寻找排名编号后的词条和热度值
  const hotEntries = [];
  let foundSection = false;
  for (let i = 0; i < texts.length; i++) {
    if (texts[i] === '微博热搜' || texts[i].includes('热搜榜')) {
      foundSection = true; continue;
    }
    if (foundSection && /^[1-9]\d*$/.test(texts[i])) {
      hotEntries.push({
        排名: texts[i],
        词条: texts[i+1] || '',
        热度值: texts[i+2] || ''
      });
    }
    if (foundSection && hotEntries.length > 50) break;
  }
  return hotEntries;
});
```

## 提取字段
| 字段 | 说明 | 示例 |
|------|------|------|
| 词条 | 热搜话题名 | 某某某事件 |
| 热度值 | 实时热度数值 | 2,102,999 |
| 排名 | 当前排名 | 1 |

## 输出格式
```markdown
# 微博热搜榜 · {日期}

采集时间：{时间}

| 排名 | 词条 | 热度 |
| --- | --- | --- |
| 1 | xxx | 2,102,999 |
```

## 注意事项
- **必须先在浏览器中登录微博账号**，否则页面会重定向到登录页
- a11y 快照（read_page）可能无法显示热搜列表内容，建议始终使用 Playwright DOM 提取
- 热度值需转换为统一量纲用于融合榜单
