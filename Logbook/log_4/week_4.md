# Session 4: Classes and Object

## Section 1: Python Classes

### Exercise 1: Creating Classes and Initialising Objects

Copies code into file lab_week_4.py and checked it runs as intended.
Then created a new TaskList with a new owner to ensure output of both owners.

```python
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
```

Output

```console
John
Jane
JACK
JOE
```

### Exercise 2: Adding Methods

Added code to TaskList class to allow for adding, removing and viewing tasks. Then added list_options method to allow user input and output.

```python
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
```

### Exercise 3: Testing functionality
Added name to TaskList and added some tasks in order to test functionality

```python
my_task_list = TaskList("Jack") 
my_task_list.tasks = ["Do Homework", "Do Laundry", "Go Shopping"] 
my_task_list.list_options() 
```

Output

```console
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Quit
Enter your choice: 1
Enter a task: Test1
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Quit
Enter your choice: 2
0. Do Homework
1. Do Laundry
2. Go Shopping
3. Test1
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Quit
Enter your choice: 3
Enter the index of the task to remove: 3
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Quit
Enter your choice: 2
0. Do Homework
1. Do Laundry
2. Go Shopping
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Quit
Enter your choice: 4
```

### Exercise 4: Composition

Defined the task class with attribute title and used the __init__ method to assign the attribute to the object

Then set the title to the ___str___ method in order to return the string representation of the object.

Tested code with new my_task_list.tasks value.

```python
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
```

Output

```console
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Quit
Enter your choice: 1
Enter a task: Test
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Quit
Enter your choice: 2
0. Task: Do Homework
1. Task: Do Laundry
2. Task: Go Shopping
3. Task: Test
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Quit
Enter your choice: 3
Enter the index of the task to remove: 3
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Quit
Enter your choice: 4
```

### Exercise 5: Developing the Task
Increased the scope of the Task List and allowed the user to edit the variables within the task list.

Task List now allows user to:
Add a task
View Tasks
Remove a task
Mark a task as completed
Change task title
Quit

Also outputs error message if invalid option is selected.

```python
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
```

Output

```console
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Change task title
6. Quit
Enter your choice: 1
Enter a task: Test
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Change task title
6. Quit
Enter your choice: 2
0. Task: Do Homework [To Do]
1. Task: Do Laundry [To Do]
2. Task: Go Shopping [To Do]
3. Task: Test [To Do]
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Change task title
6. Quit
Enter your choice: 4
Enter the index of the task to mark complete: 3
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Change task title
6. Quit
Enter your choice: 5
Enter the index of the task to rename: 3
Enter the new title: Test1
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Change task title
6. Quit
Enter your choice: 2
0. Task: Do Homework [To Do]
1. Task: Do Laundry [To Do]
2. Task: Go Shopping [To Do]
3. Task: Test1 [Complete]
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Change task title
6. Quit
Enter your choice: 3
Enter the index of the task to remove: 3
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Change task title
6. Quit
Enter your choice: 7
Invalid option
```

## Section 2: Python Libraries

### Exercise 1: Adding Dates

Imported datetime to Task List and altered the TaskList class to include a date created and a date due. 

Then created functionality to allow a user to change the due date of a task after creating it.

```python
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
```

Output

```console
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. Quit
Enter your choice: 1
Enter a task: Test
Enter a due date (YYYY-MM-DD): 2026-02-28

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. Quit
Enter your choice: 2
0. Task: Test [To Do] [Due: 2026-02-28]

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. Quit
Enter your choice: 4
Enter the index of the task to mark complete: 0

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. Quit
Enter your choice: 5
Enter the index of the task to edit: 0
Edit Task
1. Change title
2. Change due date
Choose an option: 1
Enter the new title: Test1

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. Quit
Enter your choice: 5
Enter the index of the task to edit: 0
Edit Task
1. Change title
2. Change due date
Choose an option: 2
Enter new due date (YYYY-MM-DD): 2026-03-01

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. Quit
Enter your choice: 2
0. Task: Test1 [Complete] [Due: 2026-03-01]

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. Quit
Enter your choice: 3
Enter the index of the task to remove: 0

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. Quit
Enter your choice: 2

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. Quit
Enter your choice: 6
```

## Section 3: Modularising
### Exercise 1: Restructuring

Created a new folder ToDoApp and copied over previously created code into new files tasks.py and task_list.py

Copied over the Task class into the tasks.py file and the TaskList class into the task_list.py file.

Added import statement to task_list.py in order to use Task class within.

tasks.py

```python
import datetime

class Task:

    def __init__(self, title, date_due):
        self.title: str = title
        self.completed: bool = False
        self.date_created: datetime.datetime = datetime.datetime.now()
        self.date_due: datetime.datetime = date_due

    def mark_completed(self):
        self.completed = True
    

    def change_title(self, new_title: str):
        self.title = new_title

    def change_due_date(self, new_due_date):
        self.date_due = new_due_date

    def __str__(self) -> str:
        status: str = "Complete" if self.completed else "To Do"
        return f"Task: {self.title} [{status}] [Due: {self.date_due.date()}]"
```

task_list.py

```python
import datetime
from tasks import Task


class TaskList:
    def __init__(self, owner: str):
        self.owner: str = owner.upper()
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
 
    def remove_task(self, ix: int):
        del self.tasks[ix]

    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")

    def edit_task(self, ix: int):
        print("Edit Task")
        print("1. Change title")
        print("2. Change due date")
        choice: str = input("Choose an option: ")
    
        if choice == "1":
            new_title: str = input("Enter the new title: ")
            self.tasks[ix].change_title(new_title)
        elif choice == "2":
            new_date: str = input("Enter new due date (YYYY-MM-DD): ")
            date_obj = datetime.datetime.strptime(new_date, "%Y-%m-%d")
            self.tasks[ix].change_due_date(date_obj)
        else:
            print("Invalid option")


```

### Exercise 2: Main()
Created main.py and created main() function to add functionality to the program.

Populated main.py with following code

```python
from tasklist import TaskList
from tasks import Task
import datetime
def main(): 
 task_list = TaskList("Jack") 
 task_list = propagate_task_list(task_list) 
 while True:
            print("\nTo-Do List Manager")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Mark a task as completed")
            print("5. Edit a task")
            print("6. Quit")
            
            choice:  = input("Enter your choice: ")

            if choice == "1":
                title:  = input("Enter a task: ")
                input_date:  = input("Enter a due date (YYYY-MM-DD): ")
                date_object: = datetime.datetime.strptime(input_date, "%Y-%m-%d")
                task = Task(title, date_object)
                task_list.add_task(task)

            elif choice == "2":
                task_list.view_tasks()

            elif choice == "3":
                ix = int(input("Enter the index of the task to remove: "))
                task_list.remove_task(ix)

            elif choice == "4":
                ix = int(input("Enter the index of the task to mark complete: "))
                task_list.tasks[ix].mark_completed()

            elif choice == "5":
                ix = int(input("Enter the index of the task to edit: "))
                task_list.edit_task(ix)

            elif choice == "6":
                break

            else:
                print("Invalid option")
                return

            
if __name__ == "__main__": 
 main()
```

Output
```console
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. Quit
Enter your choice: 1
Enter a task: Test
Enter a due date (YYYY-MM-DD): 2026-02-28

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. Quit
Enter your choice: 2
0. Task: Test [To Do] [Due: 2026-02-28]

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. Quit
Enter your choice: 4
Enter the index of the task to mark complete: 0

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. Quit
Enter your choice: 5
Enter the index of the task to edit: 0
Edit Task
1. Change title
2. Change due date
Choose an option: 1
Enter the new title: Test1

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. Quit
Enter your choice: 5
Enter the index of the task to edit: 0
Edit Task
1. Change title
2. Change due date
Choose an option: 2
Enter new due date (YYYY-MM-DD): 2026-03-01

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. Quit
Enter your choice: 2
0. Task: Test1 [Complete] [Due: 2026-03-01]

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. Quit
Enter your choice: 3
Enter the index of the task to remove: 0

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. Quit
Enter your choice: 2

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. Quit
Enter your choice: 6
```


#### Task 2: Modularisation

Modularised the code further by adding extra code to main.py

```python
from task_list import TaskList
from tasks import Task
import datetime

def propagate_task_list(task_list: TaskList) -> TaskList: 
 task_list.add_task(Task("Buy groceries", datetime.now() - datetime.timedelta(days=4))) 
 task_list.add_task(Task("Do laundry", datetime.now() - datetime.timedelta(days=-2))) 
 task_list.add_task(Task("Clean room", datetime.now() + datetime.timedelta(days=-1))) 
 task_list.add_task(Task("Do homework", datetime.now() + datetime.timedelta(days=3))) 
 task_list.add_task(Task("Walk dog", datetime.now() + datetime.timedelta(days=5))) 
 task_list.add_task(Task("Do dishes", datetime.now() + datetime.timedelta(days=6))) 
 return task_list

def main(): 
 task_list = TaskList("Jack") 
 task_list = propagate_task_list(task_list) 
 while True:
            print("\nTo-Do List Manager")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Mark a task as completed")
            print("5. Edit a task")
            print("6. Quit")
            
            choice: str = input("Enter your choice: ")

            if choice == "1":
                title:  = input("Enter a task: ")
                input_date: = input("Enter a due date (YYYY-MM-DD): ")
                date_object: = datetime.datetime.strptime(input_date, "%Y-%m-%d")
                task = Task(title, date_object)
                task_list.add_task(task)

            elif choice == "2":
                task_list.view_tasks()

            elif choice == "3":
                ix = int(input("Enter the index of the task to remove: "))
                task_list.remove_task(ix)

            elif choice == "4":
                ix = int(input("Enter the index of the task to mark complete: "))
                task_list.tasks[ix].mark_completed()

            elif choice == "5":
                ix = int(input("Enter the index of the task to edit: "))
                task_list.edit_task(ix)

            elif choice == "6":
                break

            else:
                print("Invalid option")
                return

            
if __name__ == "__main__": 
 main()
```

Output

```console
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. Quit
Enter your choice: 2
0. Task: Buy groceries [To Do] [Due: 2026-02-23]
1. Task: Do laundry [To Do] [Due: 2026-03-01]
2. Task: Clean room [To Do] [Due: 2026-02-26]
3. Task: Do homework [To Do] [Due: 2026-03-02]
4. Task: Walk dog [To Do] [Due: 2026-03-04]
5. Task: Do dishes [To Do] [Due: 2026-03-05]

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. Quit
Enter your choice: 6
```

## Section 4: Type Checking and Documentation
### Exercise 1: Type Checking

Added type hints to all variables.

main.py

```python
from task_list import TaskList
from tasks import Task
import datetime

def propagate_task_list(task_list: TaskList) -> TaskList: 

 task_list.add_task(Task("Buy groceries", datetime.datetime.now() - datetime.timedelta(days=4))) 
 task_list.add_task(Task("Do laundry", datetime.datetime.now() - datetime.timedelta(days=-2))) 
 task_list.add_task(Task("Clean room", datetime.datetime.now() + datetime.timedelta(days=-1))) 
 task_list.add_task(Task("Do homework", datetime.datetime.now() + datetime.timedelta(days=3))) 
 task_list.add_task(Task("Walk dog", datetime.datetime.now() + datetime.timedelta(days=5))) 
 task_list.add_task(Task("Do dishes", datetime.datetime.now() + datetime.timedelta(days=6))) 
 return task_list

def main(): 
 task_list = TaskList("Jack") 
 task_list = propagate_task_list(task_list) 
 while True:
            print("\nTo-Do List Manager")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Mark a task as completed")
            print("5. Edit a task")
            print("6. Quit")
            
            choice: str = input("Enter your choice: ")

            if choice == "1":
                title: str = input("Enter a task: ")
                input_date: str = input("Enter a due date (YYYY-MM-DD): ")
                date_object: datetime.datetime = datetime.datetime.strptime(input_date, "%Y-%m-%d")
                task = Task(title, date_object)
                task_list.add_task(task)

            elif choice == "2":
                task_list.view_tasks()

            elif choice == "3":
                ix = int(input("Enter the index of the task to remove: "))
                task_list.remove_task(ix)

            elif choice == "4":
                ix = int(input("Enter the index of the task to mark complete: "))
                task_list.tasks[ix].mark_completed()

            elif choice == "5":
                ix = int(input("Enter the index of the task to edit: "))
                task_list.edit_task(ix)

            elif choice == "6":
                break

            else:
                print("Invalid option")
                return

            
if __name__ == "__main__": 
 main()
```

tasks.py

```python
import datetime

class Task:
    def __init__(self, title, date_due):
        self.title: str = title
        self.completed: bool = False
        self.date_created: datetime.datetime = datetime.datetime.now()
        self.date_due: datetime.datetime = date_due


    def mark_completed(self):
        self.completed = True
    
    def change_title(self, new_title: str):
        self.title = new_title

    def change_due_date(self, new_due_date):
        self.date_due = new_due_date

    def __str__(self) -> str:
        status: str = "Complete" if self.completed else "To Do"
        return f"Task: {self.title} [{status}] [Due: {self.date_due.date()}]"
```

task_list.py

```python
import datetime
from tasks import Task


class TaskList:
    def __init__(self, owner: str):
        self.owner: str = owner.upper()
        self.tasks = []
 

    def add_task(self, task):
        self.tasks.append(task)


 
    def remove_task(self, ix: int):
        del self.tasks[ix]


    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")

    
    def edit_task(self, ix: int):
        print("Edit Task")
        print("1. Change title")
        print("2. Change due date")
        choice: str = input("Choose an option: ")
    
        if choice == "1":
            new_title: str = input("Enter the new title: ")
            self.tasks[ix].change_title(new_title)
        elif choice == "2":
            new_date: str = input("Enter new due date (YYYY-MM-DD): ")
            date_obj = datetime.datetime.strptime(new_date, "%Y-%m-%d")
            self.tasks[ix].change_due_date(date_obj)
        else:
            print("Invalid option")


```

### Exercise 2: Docstrings and Comments

Added docstrings to all classes, functions and methods within the code to describe them.

main.py
```python
from task_list import TaskList
from tasks import Task
import datetime

def propagate_task_list(task_list: TaskList) -> TaskList: 
 """Propagates a task list with some sample tasks.
 Args: task_list (TaskList): Task list to propagate.
 Returns: TaskList: The propagated task list.
 """ 
 task_list.add_task(Task("Buy groceries", datetime.datetime.now() - datetime.timedelta(days=4))) 
 task_list.add_task(Task("Do laundry", datetime.datetime.now() - datetime.timedelta(days=-2))) 
 task_list.add_task(Task("Clean room", datetime.datetime.now() + datetime.timedelta(days=-1))) 
 task_list.add_task(Task("Do homework", datetime.datetime.now() + datetime.timedelta(days=3))) 
 task_list.add_task(Task("Walk dog", datetime.datetime.now() + datetime.timedelta(days=5))) 
 task_list.add_task(Task("Do dishes", datetime.datetime.now() + datetime.timedelta(days=6))) 
 return task_list

def main(): 
 task_list = TaskList("Jack") 
 task_list = propagate_task_list(task_list) 
 while True:
            print("\nTo-Do List Manager")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Mark a task as completed")
            print("5. Edit a task")
            print("6. Quit")
            
            choice: str = input("Enter your choice: ")

            if choice == "1":
                title: str = input("Enter a task: ")
                input_date: str = input("Enter a due date (YYYY-MM-DD): ")
                date_object: datetime.datetime = datetime.datetime.strptime(input_date, "%Y-%m-%d")
                task = Task(title, date_object)
                task_list.add_task(task)

            elif choice == "2":
                task_list.view_tasks()

            elif choice == "3":
                ix = int(input("Enter the index of the task to remove: "))
                task_list.remove_task(ix)

            elif choice == "4":
                ix = int(input("Enter the index of the task to mark complete: "))
                task_list.tasks[ix].mark_completed()

            elif choice == "5":
                ix = int(input("Enter the index of the task to edit: "))
                task_list.edit_task(ix)

            elif choice == "6":
                break

            else:
                print("Invalid option")
                return

            
if __name__ == "__main__": 
 main()



```

tasks.py
```python
import datetime

class Task:
    """
    Represents a single task with a title, due date, and completion status

    Attributes:
        title (str): Name of task
        completed (bool): Whether the task is completed
        date_created (datetime): Timestamp when task was created
        date_due (datetime): Due date of task
    """
    def __init__(self, title, date_due):
        self.title: str = title
        self.completed: bool = False
        self.date_created: datetime.datetime = datetime.datetime.now()
        self.date_due: datetime.datetime = date_due
    
    """
    Marks task as complete
    """

    def mark_completed(self):
        self.completed = True
    
    """
    Updates title of task

    Args:
        new_title (str): New title of task
    """

    def change_title(self, new_title: str):
        self.title = new_title


    """
    Updates due date of task
    Args:
        new_due_date (datetime): Task's new due date 
    """
    def change_due_date(self, new_due_date):
        self.date_due = new_due_date

    def __str__(self) -> str:
        status: str = "Complete" if self.completed else "To Do"
        return f"Task: {self.title} [{status}] [Due: {self.date_due.date()}]"
```

task_list.py

```python
import datetime
from tasks import Task


class TaskList:
    """
    Collection of task objects belonging to an owner

    Attributes:
    owner (str): Name of the task list owner, stored uppercase
    tasks (list): List of task objects
    """
    def __init__(self, owner: str):
        self.owner: str = owner.upper()
        self.tasks = []
 
    """
    Adds a new task object

    Args:
        task (Task): the task to be added
    """
    def add_task(self, task):
        self.tasks.append(task)

    """
    Removes a task from the list by its index

    Args:
        ix (int): The index of the task to remove
    """
 
    def remove_task(self, ix: int):
        del self.tasks[ix]

    """
    Prints every task with a number at the start to display its index
    """
    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")

    """
    Allows user to edit task via its index

    Args:
        ix (int): The index of the task to edit
    """

    def edit_task(self, ix: int):
        print("Edit Task")
        print("1. Change title")
        print("2. Change due date")
        choice: str = input("Choose an option: ")
    
        if choice == "1":
            new_title: str = input("Enter the new title: ")
            self.tasks[ix].change_title(new_title)
        elif choice == "2":
            new_date: str = input("Enter new due date (YYYY-MM-DD): ")
            date_obj = datetime.datetime.strptime(new_date, "%Y-%m-%d")
            self.tasks[ix].change_due_date(date_obj)
        else:
            print("Invalid option")

```

## Section 5: Portfolio

### Exercise 1

Moved ToDoApp into new folder and continued work.

Added string description attribute to Task class, allowed to be passed as a parameter within the __init__ method.

Added method change_description to allow user to change the description

Changed the __str__ method to include description

Changed main() function to allow user to change description.

main.py
```python
from task_list import TaskList
from tasks import Task
import datetime

def propagate_task_list(task_list: TaskList) -> TaskList: 
 """Propagates a task list with some sample tasks.
 Args: task_list (TaskList): Task list to propagate.
 Returns: TaskList: The propagated task list.
 """ 
 task_list.add_task(Task("Buy groceries", datetime.datetime.now() - datetime.timedelta(days=4))) 
 task_list.add_task(Task("Do laundry", datetime.datetime.now() - datetime.timedelta(days=-2))) 
 task_list.add_task(Task("Clean room", datetime.datetime.now() + datetime.timedelta(days=-1))) 
 task_list.add_task(Task("Do homework", datetime.datetime.now() + datetime.timedelta(days=3))) 
 task_list.add_task(Task("Walk dog", datetime.datetime.now() + datetime.timedelta(days=5))) 
 task_list.add_task(Task("Do dishes", datetime.datetime.now() + datetime.timedelta(days=6))) 
 return task_list

def main(): 
 task_list = TaskList("Jack") 
 task_list = propagate_task_list(task_list) 
 while True:
            print("\nTo-Do List Manager")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Mark a task as completed")
            print("5. Edit a task")
            print("6. Quit")
            
            choice: str = input("Enter your choice: ")

            if choice == "1":
                title: str = input("Enter a task: ")
                input_date: str = input("Enter a due date (YYYY-MM-DD): ")
                date_object: datetime.datetime = datetime.datetime.strptime(input_date, "%Y-%m-%d")
                task = Task(title, date_object)
                task_list.add_task(task)

            elif choice == "2":
                task_list.view_tasks()

            elif choice == "3":
                ix = int(input("Enter the index of the task to remove: "))
                task_list.remove_task(ix)

            elif choice == "4":
                ix = int(input("Enter the index of the task to mark complete: "))
                task_list.tasks[ix].mark_completed()

            elif choice == "5":
                ix = int(input("Enter the index of the task to edit: "))
                task_list.edit_task(ix)

            elif choice == "6":
                break

            else:
                print("Invalid option")
                return

            
if __name__ == "__main__": 
 main()



```

tasks.py
```python
import datetime

class Task:
    """
    Represents a single task with a title, due date, and completion status

    Attributes:
        title (str): Name of task
        completed (bool): Whether the task is completed
        date_created (datetime): Timestamp when task was created
        date_due (datetime): Due date of task
    """
    def __init__(self, title, date_due, description=""):
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.date_created: datetime.datetime = datetime.datetime.now()
        self.date_due: datetime.datetime = date_due
    
    """
    Marks task as complete
    """

    def mark_completed(self):
        self.completed = True
    
    """
    Updates title of task

    Args:
        new_title (str): New title of task
    """

    def change_title(self, new_title: str):
        self.title = new_title


    """
    Updates due date of task
    Args:
        new_due_date (datetime): Task's new due date 
    """
    def change_due_date(self, new_due_date):
        self.date_due = new_due_date
        
    def change_description(self, new_description: str):
        self.description = new_description

    def __str__(self) -> str:
        status: str = "Complete" if self.completed else "To Do"
        desc_part = f"\n Description: {self.description}" if self.description else ""
        return f"Task: {self.title} [{status}] [Due: {self.date_due.date()}]{desc_part}"
```

task_list.py
```python
import datetime
from tasks import Task


class TaskList:
    """
    Collection of task objects belonging to an owner

    Attributes:
    owner (str): Name of the task list owner, stored uppercase
    tasks (list): List of task objects
    """
    def __init__(self, owner: str):
        self.owner: str = owner.upper()
        self.tasks = []
 
    """
    Adds a new task object

    Args:
        task (Task): the task to be added
    """
    def add_task(self, task):
        self.tasks.append(task)

    """
    Removes a task from the list by its index

    Args:
        ix (int): The index of the task to remove
    """
 
    def remove_task(self, ix: int):
        del self.tasks[ix]

    """
    Prints every task with a number at the start to display its index
    """
    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")

    """
    Allows user to edit task via its index

    Args:
        ix (int): The index of the task to edit
    """

    def edit_task(self, ix: int):
        print("Edit Task")
        print("1. Change title")
        print("2. Change due date")
        print("3. Change description")
        choice: str = input("Choose an option: ")
    
        if choice == "1":
            new_title: str = input("Enter the new title: ")
            self.tasks[ix].change_title(new_title)
        elif choice == "2":
            new_date: str = input("Enter new due date (YYYY-MM-DD): ")
            date_obj = datetime.datetime.strptime(new_date, "%Y-%m-%d")
            self.tasks[ix].change_due_date(date_obj)
        elif choice == "3":
            new_description: str = input("Enter a new description or leave blank to clear: ")
            self.tasks[ix].change_description(new_description)
        else:
            print("Invalid option")

```

Output
```console
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. Quit
Enter your choice: 1
Enter a task: Test
Enter a due date (YYYY-MM-DD): 2026-02-28
Enter a description (optional): New Test

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. Quit
Enter your choice: 2
0. Task: Buy groceries [To Do] [Due: 2026-02-23]
1. Task: Do laundry [To Do] [Due: 2026-03-01]
2. Task: Clean room [To Do] [Due: 2026-02-26]
3. Task: Do homework [To Do] [Due: 2026-03-02]
4. Task: Walk dog [To Do] [Due: 2026-03-04]
5. Task: Do dishes [To Do] [Due: 2026-03-05]
6. Task: Test [To Do] [Due: 2026-02-28]
 Description: New Test

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. Quit
Enter your choice: 5
Enter the index of the task to edit: 6
Edit Task
1. Change title
2. Change due date
3. Change description
Choose an option: 1
Enter the new title: Test1

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. Quit
Enter your choice: 5
Enter the index of the task to edit: 6
Edit Task
1. Change title
2. Change due date
3. Change description
Choose an option: 3
Enter a new description or leave blank to clear: New Testing

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. Quit
Enter your choice: 2
0. Task: Buy groceries [To Do] [Due: 2026-02-23]
1. Task: Do laundry [To Do] [Due: 2026-03-01]
2. Task: Clean room [To Do] [Due: 2026-02-26]
3. Task: Do homework [To Do] [Due: 2026-03-02]
4. Task: Walk dog [To Do] [Due: 2026-03-04]
5. Task: Do dishes [To Do] [Due: 2026-03-05]
6. Task: Test1 [To Do] [Due: 2026-02-28]
 Description: New Testing

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. Quit
Enter your choice: 5
Enter the index of the task to edit: 6
Edit Task
1. Change title
2. Change due date
3. Change description
Choose an option: 2
Enter new due date (YYYY-MM-DD): 2026-03-01

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. Quit
Enter your choice: 2
0. Task: Buy groceries [To Do] [Due: 2026-02-23]
1. Task: Do laundry [To Do] [Due: 2026-03-01]
2. Task: Clean room [To Do] [Due: 2026-02-26]
3. Task: Do homework [To Do] [Due: 2026-03-02]
4. Task: Walk dog [To Do] [Due: 2026-03-04]
5. Task: Do dishes [To Do] [Due: 2026-03-05]
6. Task: Test1 [To Do] [Due: 2026-03-01]
 Description: New Testing

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. Quit
Enter your choice: 6
```

### Exercise 2
Copied previous code into a new folder and continued.

Added view_overdue_tasks that prints all overdue tasks based on the current date

Changed main() function to allow user to view all overdue tasks

main.py
```python
from task_list import TaskList
from tasks import Task
import datetime

def propagate_task_list(task_list: TaskList) -> TaskList: 
 """Propagates a task list with some sample tasks.
 Args: task_list (TaskList): Task list to propagate.
 Returns: TaskList: The propagated task list.
 """ 
 task_list.add_task(Task("Buy groceries", datetime.datetime.now() - datetime.timedelta(days=4))) 
 task_list.add_task(Task("Do laundry", datetime.datetime.now() - datetime.timedelta(days=-2))) 
 task_list.add_task(Task("Clean room", datetime.datetime.now() + datetime.timedelta(days=-1))) 
 task_list.add_task(Task("Do homework", datetime.datetime.now() + datetime.timedelta(days=3))) 
 task_list.add_task(Task("Walk dog", datetime.datetime.now() + datetime.timedelta(days=5))) 
 task_list.add_task(Task("Do dishes", datetime.datetime.now() + datetime.timedelta(days=6))) 
 return task_list

def main(): 
 task_list = TaskList("Jack") 
 task_list = propagate_task_list(task_list) 
 while True:
            print("\nTo-Do List Manager")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Mark a task as completed")
            print("5. Edit a task")
            print("6. View overdue tasks")
            print("7. Quit")
            
            choice: str = input("Enter your choice: ")

            if choice == "1":
                title: str = input("Enter a task: ")
                input_date: str = input("Enter a due date (YYYY-MM-DD): ")
                date_object: datetime.datetime = datetime.datetime.strptime(input_date, "%Y-%m-%d")
                description: str = input("Enter a description (optional): ")
                
                task = Task(title, date_object, description)
                task_list.add_task(task)

            elif choice == "2":
                task_list.view_tasks()

            elif choice == "3":
                ix = int(input("Enter the index of the task to remove: "))
                task_list.remove_task(ix)

            elif choice == "4":
                ix = int(input("Enter the index of the task to mark complete: "))
                task_list.tasks[ix].mark_completed()

            elif choice == "5":
                ix = int(input("Enter the index of the task to edit: "))
                task_list.edit_task(ix)
                
            elif choice == "6":
                task_list.view_overdue_tasks()

            elif choice == "7":
                break

            else:
                print("Invalid option")
                return

            
if __name__ == "__main__": 
 main()

```

tasks.py
```python
import datetime

class Task:
    """
    Represents a single task with a title, due date, and completion status

    Attributes:
        title (str): Name of task
        completed (bool): Whether the task is completed
        date_created (datetime): Timestamp when task was created
        date_due (datetime): Due date of task
    """
    def __init__(self, title, date_due, description=""):
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.date_created: datetime.datetime = datetime.datetime.now()
        self.date_due: datetime.datetime = date_due
    
    """
    Marks task as complete
    """

    def mark_completed(self):
        self.completed = True
    
    """
    Updates title of task

    Args:
        new_title (str): New title of task
    """

    def change_title(self, new_title: str):
        self.title = new_title


    """
    Updates due date of task
    Args:
        new_due_date (datetime): Task's new due date 
    """
    def change_due_date(self, new_due_date):
        self.date_due = new_due_date
        
    def change_description(self, new_description: str):
        self.description = new_description

    def __str__(self) -> str:
        status: str = "Complete" if self.completed else "To Do"
        desc_part = f"\n Description: {self.description}" if self.description else ""
        return f"Task: {self.title} [{status}] [Due: {self.date_due.date()}]{desc_part}"
```

task_list.py

```python
import datetime
from tasks import Task


class TaskList:
    """
    Collection of task objects belonging to an owner

    Attributes:
    owner (str): Name of the task list owner, stored uppercase
    tasks (list): List of task objects
    """
    def __init__(self, owner: str):
        self.owner: str = owner.upper()
        self.tasks = []
 
    """
    Adds a new task object

    Args:
        task (Task): the task to be added
    """
    def add_task(self, task):
        self.tasks.append(task)

    """
    Removes a task from the list by its index

    Args:
        ix (int): The index of the task to remove
    """
 
    def remove_task(self, ix: int):
        del self.tasks[ix]

    """
    Prints every task with a number at the start to display its index
    """
    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")
            
    """
    Finds overdue tasks and displays them
    """
            
    def view_overdue_tasks(self):
        today = datetime.datetime.now()
        
        print("\nOverdue Tasks:")
        found = False
        
        for i, task in enumerate(self.tasks):
            if not task.completed and task.date_due < today:
                print(f"{i}. {task}")
                found = True
        
        if not found:
            print("No overdue tasks")

    """
    Allows user to edit task via its index

    Args:
        ix (int): The index of the task to edit
    """

    def edit_task(self, ix: int):
        print("Edit Task")
        print("1. Change title")
        print("2. Change due date")
        print("3. Change description")
        choice: str = input("Choose an option: ")
    
        if choice == "1":
            new_title: str = input("Enter the new title: ")
            self.tasks[ix].change_title(new_title)
        elif choice == "2":
            new_date: str = input("Enter new due date (YYYY-MM-DD): ")
            date_obj = datetime.datetime.strptime(new_date, "%Y-%m-%d")
            self.tasks[ix].change_due_date(date_obj)
        elif choice == "3":
            new_description: str = input("Enter a new description or leave blank to clear: ")
            self.tasks[ix].change_description(new_description)
        else:
            print("Invalid option")


```

Output (current date 2026-02-27)

```console
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. View overdue tasks
7. Quit
Enter your choice: 1
Enter a task: Test1
Enter a due date (YYYY-MM-DD): 2025-02-21
Enter a description (optional): Overdue 

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. View overdue tasks
7. Quit
Enter your choice: 6

Overdue Tasks:
0. Task: Buy groceries [To Do] [Due: 2026-02-23]
2. Task: Clean room [To Do] [Due: 2026-02-26]
6. Task: Test1 [To Do] [Due: 2025-02-21]
 Description: Overdue

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. View overdue tasks
7. Quit
Enter your choice: 7
```