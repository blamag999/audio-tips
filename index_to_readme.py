#!/usr/bin/env python3
from pathlib import Path

README = Path("README.md")
INDEX = Path("INDEX.md")

START = "<!-- INDEX-START -->"
END = "<!-- INDEX-END -->"


def main():
    if not README.exists():
        raise SystemExit("❌ README.md not found")

    if not INDEX.exists():
        raise SystemExit("❌ INDEX.md not found")

    readme_text = README.read_text(encoding="utf-8")
    index_text = INDEX.read_text(encoding="utf-8")

    if START not in readme_text or END not in readme_text:
        raise SystemExit("❌ Marker not found in README.md")

    start_pos = readme_text.index(START) + len(START)
    end_pos = readme_text.index(END)

    before = readme_text[:start_pos]
    after = readme_text[end_pos:]

    # Optional: chỉ lấy phần sau tiêu đề của INDEX.md
    index_lines = index_text.splitlines()
    filtered = []
    started = False

    for line in index_lines:
        if line.strip().startswith("---"):
            started = True
            continue
        if started:
            filtered.append(line)

    index_block = "\n\n" + "\n".join(filtered).strip() + "\n\n"

    new_readme = before + index_block + END + after
    README.write_text(new_readme, encoding="utf-8")

    print("✅ README.md updated from INDEX.md")


if __name__ == "__main__":
    main()
