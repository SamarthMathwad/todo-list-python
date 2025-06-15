import json
import os

FILENAME = "tasks.json"

# Load tasks from JSON file
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

# Save tasks to JSON file
def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)

# Initialize tasks
tasks = load_tasks()

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print("✅ Task added!")

def view_tasks():
    if not tasks:
        print("📝 No tasks yet.")
        return
    for i, t in enumerate(tasks):
        status = "✅" if t["done"] else "❌"
        print(f"{i+1}. {t['task']} [{status}]")

def mark_done():
    view_tasks()
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            save_tasks(tasks)
            print("🎉 Task marked as done!")
        else:
            print("❗ Invalid task number.")
    except ValueError:
        print("❗ Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            save_tasks(tasks)
            print("🗑️ Task deleted!")
        else:
            print("❗ Invalid task number.")
    except ValueError:
        print("❗ Please enter a valid number.")

# App loop
while True:
    show_menu()
    choice = input("Choose an option (1–5): ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("👋 Exiting To-Do List App.")
        break
    else:
        print("❗ Invalid choice. Try again.")
