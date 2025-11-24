#!/usr/bin/env python3
import re
from pathlib import Path

README_PATH = Path("README.md")
TOC_START = "<!-- TOC-START -->"
TOC_END = "<!-- TOC-END -->"


def slugify(heading: str) -> str:
    """
    Tạo anchor giống GitHub:
    - lowercase
    - bỏ ký tự đặc biệt
    - thay khoảng trắng bằng dấu -
    """
    heading = heading.strip().lower()
    heading = re.sub(r"[^\w\s-]", "", heading)  # bỏ ký tự lạ
    heading = re.sub(r"\s+", "-", heading)      # space -> -
    return heading


def extract_headings(text: str):
    """
    Lấy các heading từ README (##, ###, ####...).
    Bỏ qua heading cấp 1 (# ...) vì thường là title repo.
    """
    headings = []
    for line in text.splitlines():
        match = re.match(r"^(#{2,6})\s+(.*)", line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            if title and not title.startswith("<"):
                headings.append((level, title))
    return headings


def build_toc(headings):
    lines = ["## Mục lục\n"]
    prev_level = 2

    for level, title in headings:
        indent = "  " * (level - 2)
        anchor = slugify(title)
        lines.append(f"{indent}- [{title}](#{anchor})")

    return "\n".join(lines) + "\n"


def update_readme():
    if not README_PATH.exists():
        raise SystemExit("Không tìm thấy README.md")

    text = README_PATH.read_text(encoding="utf-8")

    if TOC_START not in text or TOC_END not in text:
        raise SystemExit("Không tìm thấy marker TOC trong README.md")

    start_idx = text.index(TOC_START) + len(TOC_START)
    end_idx = text.index(TOC_END)

    before = text[:start_idx].rstrip()
    after = text[end_idx:]

    headings = extract_headings(text)
    toc_md = "\n\n" + build_toc(headings) + "\n"

    new_text = before + toc_md + TOC_END + after

    README_PATH.write_text(new_text, encoding="utf-8")
    print("✅ README.md đã được cập nhật TOC.")


if __name__ == "__main__":
    update_readme()
