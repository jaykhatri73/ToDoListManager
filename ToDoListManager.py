# displays meanu for user input
def display_menu():
    print(". . . To-Do List Manager . . .")
    print("1. Add task")
    print("2. Mark task as completed")
    print("3. View all tasks")
    print("4. Exit")


# adding task to the list
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task added: {task}")

# to mark a task as completed


def mark_completed(tasks):
    if len(tasks) == 0:
        print("No tasks to mark as completed.")
        return

    # prining available tasks to choose from
    print("Current tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

    task_num = int(input("Enter the task number to mark as completed: "))
    if task_num < 1 or task_num > len(tasks):
        print("Invalid task number.")
        return

    # removing the selected task
    marked_task = tasks.pop(task_num - 1)
    print(f"Marked task '{marked_task}' as completed!")

    # printing updated list
    print(f"Updated Task List:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

# to view saved tasks


def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks.")
        return

    print("Current tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

# main function


def manager():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            mark_completed(tasks)
        elif choice == "3":
            view_tasks(tasks)
        elif choice == "4":
            print("Exiting Task Manager!")
            break
        else:
            print("Invalid choice. Please try again.")


manager()
