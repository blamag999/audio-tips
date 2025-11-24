#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
README_PATH = ROOT / "README.md"

EXCLUDE_DIRS = {".git", ".github", "__pycache__", ".vscode", ".idea", ".venv"}
EXCLUDE_FILES = {"README.md"}


def should_exclude(path: Path) -> bool:
    parts = path.parts
    if any(part in EXCLUDE_DIRS for part in parts):
        return True
    if path.name in EXCLUDE_FILES:
        return True
    return False


def scan_repo():
    files = []
    for p in sorted(ROOT.rglob("*")):
        if p.is_file() and not should_exclude(p):
            rel = p.relative_to(ROOT)
            files.append(rel)
    return files


def build_readme_content(files):
    lines = []

    # Header đơn giản
    lines.append("# Audio Tips Repository")
    lines.append("")
    lines.append("Tự động sinh README từ cấu trúc repo. Mỗi file bên dưới là một ghi chú / tài liệu trong repo.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Index toàn bộ repo")
    lines.append("")

    if not files:
        lines.append("_(Không tìm thấy file nào – repo đang trống hoặc cấu hình exclude quá chặt)_")
    else:
        for rel in files:
            path_str = rel.as_posix()
            name = rel.name
            # Hiển thị: tên file (đường dẫn)
            lines.append(f"- [{name}]({path_str})")

    lines.append("")
    lines.append("> README này được sinh tự động bằng script `generate_readme.py` (GitHub Actions). Không nên chỉnh sửa tay.")
    lines.append("")

    return "\n".join(lines)


def main():
    files = scan_repo()
    content = build_readme_content(files)
    README_PATH.write_text(content, encoding="utf-8")
    print("✅ README.md generated / updated")


if __name__ == "__main__":
    main()
