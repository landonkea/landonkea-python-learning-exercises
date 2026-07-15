tasks = []

def add_task(name):
    task = {"name": name, "done": False}
    tasks.append(task)

def list_tasks():
    for task in tasks:
        status = "✓" if task["done"] else " "
        print("[" + status + "] " + task["name"])

add_task("Buy groceries")
add_task("Finish portfolio project")
add_task("Call the bank")

list_tasks()
