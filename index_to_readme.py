#!/usr/bin/env python3
from pathlib import Path
import re

README_PATH = Path("README.md")
INDEX_PATH = Path("INDEX.md")


def parse_index_items():
    """Parse các dòng dạng - [Title](file.md) từ INDEX.md."""
    items = []
    if INDEX_PATH.exists():
        text = INDEX_PATH.read_text(encoding="utf-8")
        pattern = re.compile(r"^\s*-\s*\[(?P<title>.+?)\]\((?P<link>.+?)\)\s*$")
        for line in text.splitlines():
            m = pattern.match(line)
            if m:
                items.append(
                    {
                        "title": m.group("title").strip(),
                        "link": m.group("link").strip(),
                    }
                )
    return items


def scan_fallback_items():
    """Nếu INDEX.md không parse được thì quét thẳng *.md trong root (trừ README/INDEX)."""
    items = []
    root = Path(".").resolve()
    for path in sorted(root.glob("*.md")):
        if path.name in ("README.md", "INDEX.md"):
            continue
        title = path.stem.replace("-", " ").replace("_", " ")
        title = re.sub(r"\s+", " ", title).strip().title()
        items.append({"title": title, "link": path.name})
    return items


def categorize_item(title, link):
    lt = title.lower()
    ln = link.lower()

    if "youtube" in lt or "youtube" in ln or "audio-advisor" in ln:
        return "youtube"
    if any(word in lt for word in ["setting", "monitor", "tv", "display", "sony", "lg"]):
        return "device"
    if any(word in lt for word in ["windows", "avr", "passthrough"]):
        return "system"
    return "other"


def build_readme_content(items):
    youtube = []
    device = []
    system = []
    other = []

    for item in items:
        cat = categorize_item(item["title"], item["link"])
        if cat == "youtube":
            youtube.append(item)
        elif cat == "device":
            device.append(item)
        elif cat == "system":
            system.append(item)
        else:
            other.append(item)

    lines = []

    # Tiêu đề
    lines.append("# 🎧 Audio Tips Repository")
    lines.append("")
    # Badge
    lines.append('<p align="center">')
    lines.append('  <a href="https://github.com/blamag999/audio-tips/stargazers">')
    lines.append('    <img src="https://img.shields.io/github/stars/blamag999/audio-tips?style=for-the-badge" alt="GitHub stars" />')
    lines.append("  </a>")
    lines.append('  <a href="https://github.com/blamag999/audio-tips/forks">')
    lines.append('    <img src="https://img.shields.io/github/forks/blamag999/audio-tips?style=for-the-badge" alt="GitHub forks" />')
    lines.append("  </a>")
    lines.append('  <a href="https://github.com/blamag999/audio-tips/blob/main/LICENSE">')
    lines.append('    <img src="https://img.shields.io/github/license/blamag999/audio-tips?style=for-the-badge" alt="License" />')
    lines.append("  </a>")
    lines.append("</p>")
    lines.append("")

    # Mô t
