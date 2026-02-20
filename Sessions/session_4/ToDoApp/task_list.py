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

