# 知乎问题热榜适配器

## 页面信息
- URL：`https://www.zhihu.com/hot`
- 类型：知乎问题热榜
- 状态：✅ 验证可用（需登录）

## 操作步骤

1. **先确保在浏览器中已登录知乎账号**
2. 打开 `https://www.zhihu.com/hot` 页面
3. **先按 `End` 键滚动到底部**，确保所有条目（通常 50 条）已加载到 DOM 中
4. 再使用 `read_page` 读取页面内容提取数据
5. 如发现条目数不足，可再次按 `End` 键确认是否懒加载完成

## 提取字段

知乎热榜页面中，每个问题都是一个指向 `https://www.zhihu.com/question/{id}` 的链接。

实际提取示例：

| 字段 | 说明 | 示例 |
| --- | --- | --- |
| 排名 | 数字编号 | 1 |
| 问题标题 | 完整标题 | 如何看待 2026 年临床医学录取分数线下降？ |
| 热度 | 官方热度值 | 525 万 |
| 链接 | 问题页面 URL（用于回头答题） | `https://www.zhihu.com/question/123456789` |

## 提取链接的方式

使用 Playwright 从 DOM 中同时提取问题标题、热度和链接：

```javascript
return await page.evaluate(() => {
  const items = [];
  // 找到热榜容器中的所有问题链接
  const links = document.querySelectorAll('a[href*="/question/"]');
  const seen = new Set();
  links.forEach(a => {
    const title = a.textContent?.trim();
    const href = a.href;
    if (title && title.length > 6 && href && !seen.has(href)) {
      seen.add(href);
      items.push({ 标题: title, 链接: href });
    }
  });
  return items.slice(0, 50);
});
```

## 输出格式

```markdown
# 知乎问题热榜 · {日期}

采集时间：{时间}

| 排名 | 问题标题 | 热度 | 链接 |
| --- | --- | --- | --- |
| 1 | 如何看待……？ | 2168万 | [去回答](https://www.zhihu.com/question/xxx) |
```

## 注意事项

- **未登录时页面会重定向到 `/signin?next=%2Fhot`**，必须先在浏览器中登录

- 登录后页面正常加载，可直接使用 `read_page` 提取数据
- 排名 7 和 9 等位置会有"新"标签表示新上榜问题
- 热度值为知乎官方"万热度"单位（如 2168 万 = 21,680,000）
- 页面标题显示为"首页 - 知乎（含未读消息数）"
