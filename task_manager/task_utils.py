from task_manager.validation import (validate_task_title, validate_task_description, validate_due_date)



def add_task(tasks, title, description,due_date):
    if not validate_task_title(title):
        print("invalid title.")
        return
    
    if not validate_task_description(description):
        print("invalid description.")
        return
    
    if not validate_due_date(due_date):
        print("invalid due date. use YYY-MM_DD")
        return
    task = {
        "title": title,
        "description": description, 
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully")
    
def mark_task_as_complete(tasks,task_number):
    if 1 <= task_number <= len(tasks):
     
        tasks[task_number -1]["completed"] = True 
        print("Task marked as complete")
    else:
        print("Task not found")

def view_pending_tasks(tasks):
    found = False
    for task in tasks:
        if not task["completed"]:
            found = True

            print("Title:", task["title"])
            print("Description:", task["description"])
            print("Due Date:", task["due_date"])

    if not found:
        print("No pending tasks.")
def calculate_progress(tasks):
    if len(tasks) == 0:
        return 0

    completed_tasks = 0

    for task in tasks:
        if task["completed"]:
            completed_tasks += 1

    progress = (completed_tasks / len(tasks)) * 100

    return progress