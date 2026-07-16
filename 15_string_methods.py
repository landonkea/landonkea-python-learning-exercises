

import json
import os


class Task:
    def __init__(self, name, done=False):
        self.name = name
        self.done = done

    def complete(self):
        self.done = True

    def uncomplete(self):
        self.done = False

    def to_dict(self):
        return {"name": self.name, "done": self.done}

    def display(self, index):
        status = "✓" if self.done else " "
        print(str(index + 1) + ". [" + status + "] " + self.name)


def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        data = [task.to_dict() for task in tasks]
        json.dump(data, file, indent=2)


def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            data = json.load(file)
            return [Task(item["name"], item["done"]) for item in data]
    return []


def get_valid_index(tasks, prompt):
    try:
        index = int(input(prompt)) - 1
        if index < 0 or index >= len(tasks):
            print("That task number doesn't exist.")
            return None
        return index
    except ValueError:
        print("That's not a valid number.")
        return None


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
        name = input("Task name: ").strip()
        if name == "":
            print("Task name can't be empty.")
        else:
            tasks.append(Task(name))
            save_tasks(tasks)
    elif choice == "2":
        for i in range(len(tasks)):
            tasks[i].display(i)
    elif choice == "3":
        for i in range(len(tasks)):
            tasks[i].display(i)
        index = get_valid_index(tasks, "Which task number to complete? ")
        if index is not None:
            tasks[index].complete()
            save_tasks(tasks)
    elif choice == "4":
        for i in range(len(tasks)):
            tasks[i].display(i)
        index = get_valid_index(tasks, "Which task number to mark incomplete? ")
        if index is not None:
            tasks[index].uncomplete()
            save_tasks(tasks)
    elif choice == "5":
        for i in range(len(tasks)):
            tasks[i].display(i)
        index = get_valid_index(tasks, "Which task number to edit? ")
        if index is not None:
            new_name = input("New name: ").strip()
            if new_name == "":
                print("Task name can't be empty.")
            else:
                tasks[index].name = new_name
                save_tasks(tasks)
    elif choice == "6":
        for i in range(len(tasks)):
            tasks[i].display(i)
        index = get_valid_index(tasks, "Which task number to delete? ")
        if index is not None:
            tasks.pop(index)
            save_tasks(tasks)
    elif choice == "7":
        break
    else:
        print("Invalid option, try again.")

