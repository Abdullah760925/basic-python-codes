# todo_list_app.py

tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print("📝 Task added!\n")

def view_tasks():
    if not tasks:
        print("📭 No tasks found.\n")
        return

    print("\nYour To-Do List:")
    for i, t in enumerate(tasks, start=1):
        status = "✅" if t["done"] else "❌"
        print(f"{i}. {t['task']} [{status}]")
    print()

def mark_done():
    view_tasks()
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("✅ Task marked as done.\n")
        else:
            print("❌ Invalid task number.\n")
    except:
        print("❌ Please enter a valid number.\n")

def delete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("🗑️ Task deleted.\n")
        else:
            print("❌ Invalid task number.\n")
    except:
        print("❌ Please enter a valid number.\n")

def main():
    while True:
        print("==== To-Do List App ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Thanks for using To-Do App ✅")
            break
        else:
            print("❌ Invalid option.\n")

main()
