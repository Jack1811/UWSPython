# Initialize an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task():
    new_task = input("Please input a new task: ")
    tasks.append(new_task)

# Function to view current tasks in the list
def view_tasks():
    if tasks == []:
        print("You have no tasks")
        return
    
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

# Function to remove a task from the list
def remove_task():
    if tasks == []:
        print("No valid tasks to remove")
        return
        
    task_removed = input("Which task do you wish to remove? ")  

    if task_removed not in tasks: 
        print("Not a valid task") 
        return
    
    tasks.remove(task_removed)

# Main program loop
while True:
    print("To-Do List Manager")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice: ")
 
    if choice == "1":
        add_task()
        print("Your new task list is:")
        view_tasks()
    elif choice == "2":
        print("Your tasks are:")
        view_tasks()
    elif choice == "3":
        remove_task()
        print("Your tasks are:")
        view_tasks()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")