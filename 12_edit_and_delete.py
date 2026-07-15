
import json
import os

tasks = []

def add_task(name):
    task = {"name": name, "done": False}
    tasks.append(task)

def list_tasks():
    for i in range(len(tasks)):
        task = tasks[i]
        status = "✓" if task["done"] else " "
        print(str(i + 1) + ". [" + status + "] " + task["name"])

def complete_task(index):
    tasks[index]["done"] = True

def uncomplete_task(index):
    tasks[index]["done"] = False

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    return []

def edit_task(index, new_name):
    tasks[index]["name"] = new_name

def delete_task(index):
    tasks.pop(index)


tasks = load_tasks()

while True:
    print("\n1. Add task")
    print("2. List tasks")
    print("3. Mark task complete")
    print("4. Mark task incomplete")
    print("5. Edit task")
    print("6. Delete task")
    print("7. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Task name: ")
        add_task(name)
        save_tasks()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        list_tasks()
        index = int(input("Which task number to complete? ")) - 1
        complete_task(index)
        save_tasks()
    elif choice == "4":
        list_tasks()
        index = int(input("Which task number to mark incomplete? ")) - 1
        uncomplete_task(index)
        save_tasks()
    elif choice == "5":
        list_tasks()
        index = int(input("Which task number to edit? ")) - 1
        new_name = input("New name: ")
        edit_task(index, new_name)
        save_tasks()
    elif choice == "6":
        list_tasks()
        index = int(input("Which task number to delete? ")) - 1
        delete_task(index)
        save_tasks()
    elif choice == "7":
        break
    else:
        print("Invalid option, try again.")


