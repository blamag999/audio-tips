#!/usr/bin/env python3
import re
from pathlib import Path

README_PATH = Path("README.md")
INDEX_PATH = Path("INDEX.md")

TOC_START = "<!-- TOC-START -->"
TOC_END = "<!-- TOC-END -->"

EXCLUDE_DIRS = {".git", ".github", "node_modules", "__pycache__", ".vscode", ".idea"}
EXCLUDE_FILES = {".DS_Store"}


# ================== PHẦN 1: GENERATE INDEX.md ==================

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


def build_index_md(root: Path):
    entries = scan_repo(root)
    lines = []
    lines.append("# 📂 Repository Index\n")
    lines.append("Tự động sinh bởi maintain_docs.py\n")
    lines.append("---\n")

    for rel, depth in entries:
        indent = "  " * depth
        name = rel.name
        link = rel.as_posix()
        lines.append(f"{indent}- [{name}]({link})")

    return "\n".join(lines) + "\n"


def update_index():
    root = Path(".").resolve()
    content = build_index_md(root)
    INDEX_PATH.write_text(content, encoding="utf-8")
    print("✅ INDEX.md updated")


# ================== PHẦN 2: GENERATE README TOC ==================

def slugify(text: str):
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text


def extract_headings(text: str):
    headings = []
    for line in text.splitlines():
        m = re.match(r"^(#{2,6})\s+(.*)", line)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            if title and not title.startswith("<"):
                headings.append((level, title))
    return headings


def build_toc(headings):
    lines = []
    lines.append("## Mục lục\n")

    for level, title in headings:
        indent = "  " * (level - 2)
        anchor = slugify(title)
        lines.append(f"{indent}- [{title}](#{anchor})")

    return "\n".join(lines) + "\n"


def update_readme_toc():
    if not README_PATH.exists():
        raise SystemExit("README.md not found")

    text = README_PATH.read_text(encoding="utf-8")

    if TOC_START not in text or TOC_END not in text:
        raise SystemExit("TOC markers not found")

    start_idx = text.index(TOC_START) + len(TOC_START)
    end_idx = text.index(TOC_END)

    before = text[:start_idx].rstrip()
    after = text[end_idx:]

    headings = extract_headings(text)
    toc_md = "\n\n" + build_toc(headings) + "\n"

    new_text = before + toc_md + TOC_END + after
    README_PATH.write_text(new_text, encoding="utf-8")

    print("✅ README TOC updated")


# ================== MAIN ==================

def main():
    update_index()
    update_readme_toc()
    print("🎉 Done!")


if __name__ == "__main__":
    main()
