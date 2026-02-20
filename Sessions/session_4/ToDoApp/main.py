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


