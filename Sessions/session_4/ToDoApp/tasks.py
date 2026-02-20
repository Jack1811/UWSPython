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