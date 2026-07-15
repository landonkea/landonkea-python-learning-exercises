
tasks = []
def add_task(task_name):
    tasks.append(task_name)
def list_tasks():
    for task in tasks:
        print("- " + task)
add_task("Buy groceries")
add_task("Finish portfolio project")
add_task("Call the bank")
list_tasks()
