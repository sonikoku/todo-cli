import sys
from todo.commands import add_task

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <command> [args]")
        return
    cmd = sys.argv[1]
    if cmd == "add":
        if len(sys.argv) < 3:
            print("Need title: python main.py add 'купить хлеб'")
            return
        add_task(sys.argv[2])
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()