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