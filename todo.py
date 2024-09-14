# To-Do List Application

# Function to display the current tasks in the to-do list
def show_tasks(tasks):
    if len(tasks) == 0:
        print("Your to-do list is empty.")
    else:
        print("\nCurrent To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Function to add a new task to the to-do list


def add_task(tasks):
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f'"{task}" has been added to your to-do list.')

# Function to delete a task from the to-do list


def delete_task(tasks):
    show_tasks(tasks)
    task_number = int(input("Enter the number of the task to delete: "))
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f'"{removed_task}" has been removed from your to-do list.')
    else:
        print("Invalid task number.")

# Main program to run the to-do list manager


def todo_manager():
    tasks = []  # List to store tasks
    while True:
        print("\nOptions:")
        print("1. Show tasks")
        print("2. Add a task")
        print("3. Delete a task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Exiting the To-Do List Manager.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


# Run the To-Do List Manager
if __name__ == "__main__":
    todo_manager()
