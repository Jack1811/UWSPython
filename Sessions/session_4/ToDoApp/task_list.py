import datetime
from tasks import Task

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

