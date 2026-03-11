import os
import subprocess

DOCS_DIR = "docs"
README_FILE = "README.md"

def get_created_date(file):
    cmd = [
        "git",
        "log",
        "--diff-filter=A",
        "--follow",
        "--format=%aI",
        "-1",
        file,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip()

docs = []

for root, dirs, files in os.walk(DOCS_DIR):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(root, file)
            date = get_created_date(path)
            docs.append((date, path))

docs.sort(reverse=True)

content = "# 📚 Repository Documents\n\n"
content += "Danh sách tài liệu được sắp xếp theo ngày tạo.\n\n"

for date, path in docs:
    name = os.path.basename(path)
    content += f"- {date[:10]} - [{name}]({path})\n"

with open(README_FILE, "w", encoding="utf-8") as f:
    f.write(content)
