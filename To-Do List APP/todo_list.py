# To-Do List App

# Initialize an empty list to store tasks
tasks = []

# Function to display the menu
def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Exit")

# Function to display tasks
def view_tasks():
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "✔" if task['completed'] else "✘"
            print(f"{i}. {task['task']} [{status}]")

# Function to add a new task
def add_task():
    task_name = input("\nEnter the task: ")
    tasks.append({"task": task_name, "completed": False})
    print(f"Task '{task_name}' added to the list.")

# Function to mark a task as completed
def mark_task_completed():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to mark as completed: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]['completed'] = True
                print(f"Task '{tasks[task_num - 1]['task']}' marked as completed.")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

# Function to remove a task
def remove_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task['task']}' removed from the list.")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

# Main function to run the app
def main():
    print("Welcome to the To-Do List App!")
    while True:
        show_menu()
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                view_tasks()
            elif choice == 2:
                add_task()
            elif choice == 3:
                mark_task_completed()
            elif choice == 4:
                remove_task()
            elif choice == 5:
                print("Thank you for using the To-Do List App! Goodbye!")
                break
            else:
                print("Invalid choice! Please choose a valid option.")
        except ValueError:
            print("Please enter a valid number.")

# Run the program
if __name__ == "__main__":
    main()
