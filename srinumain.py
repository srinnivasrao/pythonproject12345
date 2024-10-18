import json

# Task class definition
class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.title} - {self.description} [{self.category}] - {status}"


# Functions to save and load tasks from a JSON file
def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4)


def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as f:
            return [Task(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []


# Functions to handle user interactions
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    category = input("Enter task category (e.g., Work, Personal, Urgent): ")
    new_task = Task(title, description, category)
    tasks.append(new_task)
    print(f"Task '{title}' added successfully.\n")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print("\n")


def mark_task_completed(tasks):
    if not tasks:
        print("No tasks available to mark as completed.")
        return
    view_tasks(tasks)
    task_num = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num].mark_completed()
        print(f"Task '{tasks[task_num].title}' marked as completed.\n")
    else:
        print("Invalid task number.\n")


def delete_task(tasks):
    if not tasks:
        print("No tasks available to delete.")
        return
    view_tasks(tasks)
    task_num = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        deleted_task = tasks.pop(task_num)
        print(f"Task '{deleted_task.title}' deleted successfully.\n")
    else:
        print("Invalid task number.\n")


# Main application logic
def main():
    tasks = load_tasks()
    while True:
        print("\n--- Personal To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Save and Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting the application.")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")


if __name__ == '__main__':
    main()
