tasks = []

def add_task(name):
    task = {"name": name, "done": False}
    tasks.append(task)

def list_tasks():
    for task in tasks:
        status = "✓" if task["done"] else " "
        print("[" + status + "] " + task["name"])

def complete_task(name):
    for task in tasks:
        if task["name"] == name:
            task["done"] = True

add_task("Buy groceries")
add_task("Finish portfolio project")
add_task("Call the bank")

complete_task("Buy groceries")

list_tasks()
