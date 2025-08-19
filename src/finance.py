import os

FILE_NAME = "tasks.txt"

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "[x]" if self.completed else "[ ]"
        return f"{status} {self.description}"

def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    completed_str, description = line.split(" ", 1)
                    completed = completed_str == "1"
                    tasks.append(Task(description, completed))
    return tasks

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            status = "1" if task.completed else "0"
            file.write(f"{status} {task.description}\n")

def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty!")
    else:
        print("\n--- Your Tasks ---")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    description = input("Enter the new task: ")
    new_task = Task(description)
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully.")

def mark_complete(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("Enter the number of the task to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1].completed = True
            save_tasks(tasks)
            print(f"Task {task_num} marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("Enter the number of the task to delete: "))
        if 1 <= task_num <= len(tasks):
            del tasks[task_num - 1]
            save_tasks(tasks)
            print(f"Task {task_num} deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List Application ---")
        print("1. View tasks")
        print("2. Add new task")
        print("3. Mark task as complete")
        print("4. Delete a task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
