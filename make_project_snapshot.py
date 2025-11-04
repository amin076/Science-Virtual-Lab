"""
make_project_snapshot.py — extended version
Creates a JSON snapshot that includes file contents (for text/code files only),
while ignoring virtual environments, IDE configs, node_modules, and build artifacts.
"""

import os
import json
import hashlib
from datetime import datetime

# 🔹 Folders and files to ignore completely
IGNORE_LIST = {
    ".git", ".github", ".vscode", ".idea", "__pycache__", ".pytest_cache",
    ".mypy_cache", ".venv", "env", "venv", "build", "dist",
    "node_modules", ".next", "coverage", "logs", "tmp", "temp"
}

# 🔹 File extensions to skip (binary, large, or irrelevant)
SKIP_EXT = {
    ".log", ".sqlite", ".db", ".pyc", ".pyo", ".exe", ".dll", ".so", ".dylib",
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico", ".zip", ".rar", ".gz", ".tar",
    ".mp3", ".mp4", ".avi", ".mov", ".pdf", ".docx", ".xlsx"
}

# 🔹 Specific filenames to skip
SKIP_FILES = {
    "package-lock.json", "yarn.lock", "pnpm-lock.yaml",
    "Pipfile.lock", "poetry.lock", "requirements.txt", ".env"
}

# 🔹 Max text file size to include (in bytes)
MAX_SIZE = 100 * 1024  # 100 KB

def hash_file(path):
    """Return SHA1 hash of first 256KB of a file."""
    h = hashlib.sha1()
    with open(path, "rb") as f:
        h.update(f.read(256 * 1024))
    return h.hexdigest()

def read_file_content(path):
    """Read file content safely if text and small enough."""
    try:
        if os.path.getsize(path) > MAX_SIZE:
            return f"[Skipped: file too large > {MAX_SIZE} bytes]"
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"[Error reading file: {e}]"

def make_snapshot(root="."):
    """Walk project and collect metadata + content for text files."""
    snapshot = []
    for dirpath, dirnames, filenames in os.walk(root):
        # Skip ignored directories
        dirnames[:] = [d for d in dirnames if d not in IGNORE_LIST]
        for name in filenames:
            if name in SKIP_FILES:
                continue
            ext = os.path.splitext(name)[1]
            if ext in SKIP_EXT:
                continue
            path = os.path.join(dirpath, name)
            rel_path = os.path.relpath(path, root)
            try:
                snapshot.append({
                    "path": rel_path.replace("\\", "/"),
                    "size": os.path.getsize(path),
                    "sha1": hash_file(path),
                    "content": read_file_content(path)
                })
            except Exception as e:
                snapshot.append({
                    "path": rel_path.replace("\\", "/"),
                    "error": str(e)
                })
    return snapshot

def main():
    snapshot = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "files": make_snapshot(".")
    }
    with open("project_snapshot.json", "w", encoding="utf-8") as f:
        json.dump(snapshot, f, indent=2, ensure_ascii=False)
    print("✅ Clean and extended snapshot saved to project_snapshot.json")

if __name__ == "__main__":
    main()
