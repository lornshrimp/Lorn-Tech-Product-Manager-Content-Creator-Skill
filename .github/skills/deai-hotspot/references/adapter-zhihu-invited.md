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
// Playwright 提取代码（含链接）
return await page.evaluate(() => {
  const results = [];
  const links = document.querySelectorAll('a[href*="question"]');
  links.forEach(a => {
    const text = a.textContent?.trim();
    const href = a.href;
    if (text && text.length > 8 && text.includes('？')) {
      results.push({ 问题标题: text, 链接: href });
    }
  });
  // 按链接去重
  const seen = new Set();
  return results.filter(r => {
    if (seen.has(r.链接)) return false;
    seen.add(r.链接);
    return true;
  }).slice(0, 20);
});
```

## 提取字段
| 字段 | 说明 | 示例 |
| --- | --- | --- |
| 问题标题 | 邀请回答的问题标题 | 如何看待Kimi K3模型价格翻5倍？ |
| 链接 | 问题页面 URL（用于回头答题） | `https://www.zhihu.com/question/xxx` |

## 输出格式

```markdown
# 知乎邀请问题 · {日期}

采集时间：{时间}

| 序号 | 问题标题 | 链接 |
| --- | --- | --- |
| 1 | xxx？ | [去回答](https://www.zhihu.com/question/xxx) |
```

## 注意事项

- **必须先在浏览器中登录知乎账号**
- 邀请问题是平台邀请当前用户回答的问题，**非热榜排名**，但可反映平台当前讨论方向
- a11y 快照仅显示导航侧栏，主内容需使用 Playwright DOM 提取
- 页面会混合展示"邀请回答"和"推荐问题"两个标签页的内容
