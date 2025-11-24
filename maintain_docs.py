#!/usr/bin/env python3
from pathlib import Path
import re

# Đường dẫn root repo và file INDEX
ROOT = Path(__file__).resolve().parent
INDEX_PATH = ROOT / "INDEX.md"

# Loại trừ một số thư mục / file
EXCLUDE_DIRS = {".git", ".github", "__pycache__", ".vscode", ".idea"}
EXCLUDE_FILES = {"INDEX.md", "README.md"}


def should_exclude(path: Path) -> bool:
    # Loại trừ theo thư mục
    if any(part in EXCLUDE_DIRS for part in path.parts):
        return True
    # Loại trừ file cụ thể
    if path.name in EXCLUDE_FILES:
        return True
    return False


def scan_markdown_files():
    """Quét toàn bộ file .md trong repo (trừ README.md, INDEX.md, .github, v.v.)."""
    files = []
    for p in sorted(ROOT.rglob("*.md")):
        if should_exclude(p):
            continue
        rel = p.relative_to(ROOT)
        files.append(rel)
    return files


def prettify_title(path: Path) -> str:
    """
    Tạo title đẹp từ tên file:
    - Giữ nguyên nếu file đã có khoảng trắng (ví dụ: 'Settings for LG 27UP600 Monitor.md')
    - Với tên dạng slug (có '-' hoặc '_'): chuyển thành Title Case
    - Bỏ hậu tố 'YouTube' nếu có
    """
    name = path.stem  # bỏ .md

    # Nếu tên file có khoảng trắng -> có vẻ đã là title rồi
    if " " in name:
        title = name.replace("_", " ").strip()
    else:
        # Dạng slug: thay '-' và '_' bằng khoảng trắng
        title = re.sub(r"[-_]+", " ", name).strip()
        # Title Case
        title = title.title()

    # Một số cleanup nhẹ
    title = title.replace(" Youtube", " YouTube")
    title = title.replace(" Avr", " AVR")

    return title


def build_index_md(files):
    lines = []
    lines.append("# 📂 Audio Tips – Index\n")
    lines.append("Danh sách tất cả các file markdown trong repo.\n")
    lines.append("---\n")

    for rel in files:
        title = prettify_title(rel)
        link = rel.as_posix()
        lines.append(f"- [{title}]({link})")

    return "\n".join(lines) + "\n"


def main():
    md_files = scan_markdown_files()
    content = build_index_md(md_files)
    INDEX_PATH.write_text(content, encoding="utf-8")
    print("✅ INDEX.md updated")


if __name__ == "__main__":
    main()
