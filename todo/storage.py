import json
from pathlib import Path

STORAGE_FILE = Path("tasks.json")

def load_tasks():
    if not STORAGE_FILE.exists():
        return []
    with STORAGE_FILE.open(encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks):
    with STORAGE_FILE.open("w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)