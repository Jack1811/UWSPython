#Session 3: Section 1

#Exercise 1: Creating Classes and Initialising Objects


#%%
class TaskList: 
    def __init__(self, owner): 
        self.owner = owner
        self.tasks = [] 

my_task_list = TaskList("John") 
print(my_task_list.owner) 

someone_else_task_list = TaskList("Jane") 
print(someone_else_task_list.owner) 

class TaskList: 
    def __init__(self, owner): 
        self.owner = owner.upper() 
        self.tasks = [] 

my_task_list = TaskList("Jack")
print(my_task_list.owner)

someone_else_task_list = TaskList("Joe")
print(someone_else_task_list.owner)
# %%

#Exercise 2: Adding Methods

class TaskList: 
    def __init__(self, owner): 
        self.owner = owner.upper()
        self.tasks = [] 
 
    def add_task(self, task): 
        self.tasks.append(task) 
 
    def remove_task(self, ix): 
        del self.tasks[ix]

    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")

    def list_options(self): 
        while True: 
            print("To-Do List Manager")
            print("1. Add a task") 
            print("2. View tasks") 
            print("3. Remove a task") 
            print("4. Quit") 
            
            choice = input("Enter your choice: ") 

            if choice == "1": 
                task = input("Enter a task: ") 
                self.add_task(task) 

            elif choice == "2": 
                self.view_tasks() 

            elif choice == "3": 
                ix = int(input("Enter the index of the task to remove: ")) 
                self.remove_task(ix) 

            elif choice == "4": 
                break

my_task_list = TaskList("Jack") 
# This part is just to test the functionality by adding some tasks to the list 
my_task_list.tasks = ["Do Homework", "Do Laundry", "Go Shopping"] 
my_task_list.list_options() 

# %%

#Exercise 4: Composition

class Task:
    def __init__(self, title):
        self.title = title
    def __str__(self): 
        return f"Task: {self.title}"

class TaskList: 
    def __init__(self, owner): 
        self.owner = owner.upper()
        self.tasks = [] 
 
    def add_task(self, task): 
        self.tasks.append(task) 
 
    def remove_task(self, ix): 
        del self.tasks[ix]

    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")

    def list_options(self): 
        while True: 
            print("To-Do List Manager")
            print("1. Add a task") 
            print("2. View tasks") 
            print("3. Remove a task") 
            print("4. Quit") 
            
            choice = input("Enter your choice: ") 

            if choice == "1": 
                title = input("Enter a task: ") 
                task = Task(title) 
                self.add_task(task) 

            elif choice == "2": 
                self.view_tasks() 

            elif choice == "3": 
                ix = int(input("Enter the index of the task to remove: ")) 
                self.remove_task(ix) 

            elif choice == "4": 
                break

my_task_list = TaskList("Jack") 
my_task_list.tasks = [Task("Do Homework"), Task("Do Laundry"), Task("Go Shopping")] 
my_task_list.list_options()



# %%

# Exercise 5

class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False
    
    def mark_completed (self):
        self.completed = True
    
    def change_title(self, new_title):
        self.title = new_title

    def __str__(self): 
        status = "Complete" if self.completed else "To Do"
        return f"Task: {self.title} [{status}]"

class TaskList: 
    def __init__(self, owner): 
        self.owner = owner.upper()
        self.tasks = [] 
 
    def add_task(self, task): 
        self.tasks.append(task) 
 
    def remove_task(self, ix): 
        del self.tasks[ix]


    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")

    def list_options(self): 
        while True: 
            print("To-Do List Manager")
            print("1. Add a task") 
            print("2. View tasks") 
            print("3. Remove a task") 
            print("4. Mark a task as completed")
            print("5. Change task title")
            print("6. Quit") 
            
            choice = input("Enter your choice: ") 

            if choice == "1": 
                title = input("Enter a task: ") 
                task = Task(title) 
                self.add_task(task) 

            elif choice == "2": 
                self.view_tasks() 

            elif choice == "3": 
                ix = int(input("Enter the index of the task to remove: ")) 
                self.remove_task(ix) 
            
            elif choice == "4":
                ix = int(input("Enter the index of the task to mark complete: ")) 
                self.tasks[ix].mark_completed() 

            elif choice == "5": 
                ix = int(input("Enter the index of the task to rename: "))
                new_title = input("Enter the new title: ")
                self.tasks[ix].change_title(new_title)

            elif choice == "6": 
                break
            
            else:
                print("Invalid option")
                return

my_task_list = TaskList("Jack") 
my_task_list.tasks = [Task("Do Homework"), Task("Do Laundry"), Task("Go Shopping")] 
my_task_list.list_options()

# %%
## Section 2: Python Libraries

#Exercise 1: Adding Dates
import datetime

class Task:
    def __init__(self, title, date_due):
        self.title = title
        self.completed = False
        self.date_created = datetime.datetime.now()
        self.date_due = date_due
    
    def mark_completed(self):
        self.completed = True
    
    def change_title(self, new_title):
        self.title = new_title

    def change_due_date(self, new_due_date):
        self.date_due = new_due_date

    def __str__(self):
        status = "Complete" if self.completed else "To Do"
        return f"Task: {self.title} [{status}] [Due: {self.date_due.date()}]"


class TaskList:
    def __init__(self, owner):
        self.owner = owner.upper()
        self.tasks = []
 
    def add_task(self, task):
        self.tasks.append(task)
 
    def remove_task(self, ix):
        del self.tasks[ix]

    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")

    def edit_task(self, ix):
        print("Edit Task")
        print("1. Change title")
        print("2. Change due date")
        choice = input("Choose an option: ")

        if choice == "1":
            new_title = input("Enter the new title: ")
            self.tasks[ix].change_title(new_title)
        elif choice == "2":
            new_date = input("Enter new due date (YYYY-MM-DD): ")
            date_obj = datetime.datetime.strptime(new_date, "%Y-%m-%d")
            self.tasks[ix].change_due_date(date_obj)
        else:
            print("Invalid option")

    def list_options(self):
        while True:
            print("\nTo-Do List Manager")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Mark a task as completed")
            print("5. Edit a task")
            print("6. Quit")
            
            choice = input("Enter your choice: ")

            if choice == "1":
                title = input("Enter a task: ")
                input_date = input("Enter a due date (YYYY-MM-DD): ")
                date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")
                task = Task(title, date_object)
                self.add_task(task)

            elif choice == "2":
                self.view_tasks()

            elif choice == "3":
                ix = int(input("Enter the index of the task to remove: "))
                self.remove_task(ix)

            elif choice == "4":
                ix = int(input("Enter the index of the task to mark complete: "))
                self.tasks[ix].mark_completed()

            elif choice == "5":
                ix = int(input("Enter the index of the task to edit: "))
                self.edit_task(ix)

            elif choice == "6":
                break

            else:
                print("Invalid option")
                return


my_task_list = TaskList("Jack")
my_task_list.list_options()
# %%
