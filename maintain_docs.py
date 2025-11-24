#!/usr/bin/env python3
import os
import re
from pathlib import Path

# ========== CẤU HÌNH CHUNG ==========
README_PATH = Path("README.md")
INDEX_PATH = Path("INDEX.md")

TOC_START = "<!-- TOC-START -->"
TOC_END = "<!-- TOC-END -->"

EXCLUDE_DIRS = {".git", ".github", "node_modules", "__pycache__", ".vscode", ".idea"}
EXCLUDE_FILES = {".DS_Store"}
# ====================================


# ================== PHẦN 1: TẠO INDEX.md ==================

def should_exclude(path: Path) -> bool:
    parts = path.parts
    if any(p in EXCLUDE_DIRS for p in parts):
        return True
    if path.name in EXCLUDE_FILES:
        return True
    return False


def scan_repo(root: Path):
    entries = []
    for path in sorted(root.rglob("*")):
        if should_exclude(path):
            continue
        if path.is_file():
            rel = path.relative_to(root)
            depth = len(rel.parts) - 1
            entries.append((rel, depth))
    return entries


def generate_tree(entries):
    lines = []
    for rel, depth in entries:
        indent = "  " * depth
        name = rel.name
        link = rel.as_posix()
        lines.append(f"{indent}- [{name}]({link})")
    return lines


def build_index_md(root: Path) -> str:
    entries = scan_repo(root)

    lines = []
    lines.append("# 📂 Repository Index\n")
    lines.append("Tự động sinh bởi `maintain_docs.py`.\n")
    lines.append("---\n")
    lines.extend(generate_tree(entries))

    return "\n".join(lines) + "\n"


def update_index():
    root = Path(".").resolve()
    content = build_index_md(root)
    INDEX_PATH.write_text(content, encoding="utf-8")
    print(f"✅ Đã cập nhật {INDEX_PATH.name}")


# ================== PHẦN 2: CẬP NHẬT TOC README ==================

def slugify(heading: str) -> str:
    """
    Tạo anchor giống GitHub:
    - chữ thường
    - bỏ ký tự đặc biệt
    - khoảng trắng -> dấu '-'
    """
    heading = heading.strip().lower()
    heading = re.sub(r"[^\w\s-]", "", heading)
    heading = re.sub(r"\s+", "-", heading)
    return heading


def extract_headings(text: str):
    """
    Lấy các heading từ README (##, ###, ####.
