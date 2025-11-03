"""
make_project_snapshot.py
Generates a JSON snapshot of the current project structure.
This helps Chatty understand the existing files and folders.
"""

import os
import json
import hashlib
from datetime import datetime

IGNORE_LIST = {
    "node_modules", ".git", ".next", "dist", "build", "coverage",
    "__pycache__", ".venv", ".mypy_cache", ".pytest_cache"
}

IGNORE_EXT = {".log", ".sqlite", ".pyc"}

def hash_file(path):
    """Return SHA1 hash of the first 256KB of a file."""
    h = hashlib.sha1()
    with open(path, "rb") as f:
        h.update(f.read(256 * 1024))
    return h.hexdigest()

def make_snapshot(root="."):
    """Walk through the project and collect file metadata."""
    snapshot = []
    for dirpath, dirnames, filenames in os.walk(root):
        # Skip ignored directories
        dirnames[:] = [d for d in dirnames if d not in IGNORE_LIST]
        for name in filenames:
            ext = os.path.splitext(name)[1]
            if ext in IGNORE_EXT:
                continue
            path = os.path.join(dirpath, name)
            rel_path = os.path.relpath(path, root)
            try:
                size = os.path.getsize(path)
                snapshot.append({
                    "path": rel_path.replace("\\", "/"),
                    "size": size,
                    "sha1": hash_file(path)
                })
            except Exception as e:
                print(f"⚠️ Skipped {rel_path}: {e}")
    return snapshot

def main():
    snapshot = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "files": make_snapshot(".")
    }
    with open("project_snapshot.json", "w", encoding="utf-8") as f:
        json.dump(snapshot, f, indent=2)
    print("✅ Snapshot saved to project_snapshot.json")

if __name__ == "__main__":
    main()
