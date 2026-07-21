"""
将 文章创作 中 2022年及之前的 .docx 文章转换为 .md 并保存到 my-articles/
"""
import os
import re
import sys
from datetime import datetime
from pathlib import Path

try:
    from docx import Document
except ImportError:
    print("请先安装 python-docx: pip install python-docx")
    sys.exit(1)

SRC_ROOT = Path(r"D:\Users\lorns\OneDrive\第二职业\产品经理独孤虾\文章创作")
DST_ROOT = Path(r"D:\Users\lorns\OneDrive\第二职业\产品经理独孤虾\互联网产品经理自媒体\my-articles")
CUTOFF = datetime(2022, 12, 31, 23, 59, 59)

# 跳过目录（书籍、非文章内容）
SKIP_DIRS = {
    "互联网广告平台产品分析、设计与实现",  # 书籍，体量太大
    ".notebook", "assets", "tmp",
}

# 主题映射：目录名 → 文章主题标签
TOPIC_MAP = {
    "产品技术": ["产品技术", "广告技术"],
    "小说创作": ["小说"],
    "理财投资": ["理财", "投资"],
    "自媒体新闻": ["自媒体", "AI"],
    "政治经济类": ["政治经济", "社会分析"],
    "研报解读": ["研报", "行业分析"],
    "终稿": ["行业观察"],
}

def docx_to_markdown(docx_path):
    """将 .docx 文件转换为纯文本 Markdown（保留段落结构）"""
    try:
        doc = Document(str(docx_path))
    except Exception as e:
        return f"[转换失败: {e}]"

    lines = []
    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue
        # 判断是否为标题（通过段落样式）
        style_name = para.style.name.lower() if para.style else ""
        if "heading" in style_name or "标题" in style_name:
            level = 1
            for ch in style_name:
                if ch.isdigit():
                    level = min(int(ch), 6)
                    break
            lines.append(f"\n{'#' * level} {text}\n")
        else:
            lines.append(text)
    return "\n\n".join(lines)


def extract_date_from_filename(name):
    """尝试从文件名中提取日期"""
    # 匹配 YYYYMMDD 或 YYYY-MM-DD
    m = re.search(r'(\d{4})[-_]?(\d{2})[-_]?(\d{2})', name)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    return None


def safe_filename(name):
    """将文件名中的非法字符替换掉"""
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    name = name.strip()
    return name


def convert_all():
    total = 0
    success = 0
    skipped = 0

    for docx_path in SRC_ROOT.rglob("*.docx"):
        # 检查是否在跳过目录中
        rel_parts = docx_path.relative_to(SRC_ROOT).parts
        if any(p in SKIP_DIRS for p in rel_parts):
            print(f"  [跳过目录] {docx_path.name}")
            skipped += 1
            continue

        # 检查修改时间
        mtime = datetime.fromtimestamp(docx_path.stat().st_mtime)
        if mtime > CUTOFF:
            print(f"  [跳过时间] {docx_path.name} ({mtime.date()})")
            skipped += 1
            continue

        total += 1
        print(f"\n--- 处理: {docx_path.relative_to(SRC_ROOT)} ---")

        # 提取日期
        date_str = extract_date_from_filename(docx_path.stem)
        if not date_str:
            date_str = mtime.strftime("%Y-%m-%d")
            print(f"  [注意] 文件名未识别日期，使用修改日期: {date_str}")

        # 确定话题标签
        parent_dir = docx_path.parent.name
        topic = TOPIC_MAP.get(parent_dir, ["行业观察"])

        # 转换内容
        content = docx_to_markdown(docx_path)
        if content.startswith("[转换失败"):
            print(f"  [失败] {content}")
            continue

        word_count = len(content.replace("\n", ""))

        # 构建 YAML front matter
        title = docx_path.stem
        yaml_front = f"""---
date: {date_str}
platform: personal
topic: {topic}
word_count: {word_count}
source: {parent_dir}
---

"""
        md_content = yaml_front + content

        # 目标文件名
        safe_title = safe_filename(title)
        if len(safe_title) > 80:
            safe_title = safe_title[:80]
        md_filename = f"{date_str}-{safe_title}.md"
        md_path = DST_ROOT / md_filename

        # 避免覆盖
        counter = 1
        while md_path.exists():
            md_path = DST_ROOT / f"{date_str}-{safe_title}_{counter}.md"
            counter += 1

        md_path.write_text(md_content, encoding="utf-8")
        print(f"  [成功] -> {md_path.name} ({word_count}字)")
        success += 1

    print(f"\n===== 完成 ===== ")
    print(f"总计: {total}, 成功: {success}, 跳过: {skipped}")
    print(f"输出目录: {DST_ROOT}")


if __name__ == "__main__":
    convert_all()
