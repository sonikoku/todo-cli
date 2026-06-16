from .storage import load_tasks, save_tasks

def add_task(title):
    tasks = load_tasks()
    new_id = max((t["id"] for t in tasks), default=0) + 1
    tasks.append({"id": new_id, "title": title, "done": False})
    save_tasks(tasks)
    print(f"[{new_id}] Добавлена: {title}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Список пуст")
        return
    for t in tasks:
        mark = "[x]" if t["done"] else "[ ]"
        print(f"{mark} {t['id']:>3}. {t['title']}")