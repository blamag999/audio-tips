#!/usr/bin/env python3
import os
from pathlib import Path

# ========== CẤU HÌNH ==========
OUTPUT_FILE = "INDEX.md"
EXCLUDE_DIRS = {".git", ".github", "node_modules", "__pycache__", ".vscode"}
EXCLUDE_FILES = {".DS_Store"}
MAX_DEPTH = 10
# ==============================

def should_exclude(path: Path):
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
        line = f"{indent}- [{name}]({link})"
        lines.append(line)
    return lines

def main():
    root = Path(".").resolve()
    entries = scan_repo(root)

    lines = []
    lines.append("# 📂 Repository Index\n")
    lines.append("Tự động sinh bởi `generate_repo_index.py`\n")
    lines.append("---\n")
    lines.extend(generate_tree(entries))

    output = "\n".join(lines)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"✅ Đã tạo {OUTPUT_FILE} thành công!")

if __name__ == "__main__":
    main()
