import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>")
        return
    print(f"Got command: {sys.argv[1]}")

if __name__ == "__main__":
    main()