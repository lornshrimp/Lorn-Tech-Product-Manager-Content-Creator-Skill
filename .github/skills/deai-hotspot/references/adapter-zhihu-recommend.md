# 知乎推荐问题适配器

## 页面信息
- URL：`https://www.zhihu.com/creator/featured-question/recommend`
- 类型：知乎推荐问题
- 状态：✅ 验证可用（需登录）

## 操作步骤

1. 在浏览器中登录知乎账号
2. 打开 `https://www.zhihu.com/creator/featured-question/recommend`
3. 等待页面加载完成
4. 使用 Playwright `page.evaluate()` 从 DOM 中提取推荐问题列表

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
| 问题标题 | 推荐回答的问题 | AI时代更稀缺的是「提出好问题」还是「判断好答案」？ |
| 链接 | 问题页面 URL | `https://www.zhihu.com/question/xxx` |

## 输出格式

```markdown
# 知乎推荐问题 · {日期}

采集时间：{时间}

| 序号 | 问题标题 | 链接 |
| --- | --- | --- |
| 1 | xxx？ | [去回答](https://www.zhihu.com/question/xxx) |
```

## 注意事项

- **必须先在浏览器中登录知乎账号**

- 推荐问题返回的是平台根据用户兴趣推荐的待回答问题，**非热榜排名**
- a11y 快照（read_page）仅显示导航侧栏，主内容需使用 Playwright 从 DOM 提取
- 推荐问题的回答数、关注数等信息在 DOM 中不易结构化提取（多为动态渲染）
