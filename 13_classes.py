# FILE: 13_classes.py
# PURPOSE: This exercise rewrites the task manager using a CLASS. A class is
#          a blueprint that bundles data (attributes) and behavior (methods)
#          together. Instead of passing dictionaries around, we create Task
#          objects that know how to display, complete, and convert themselves.
#          This is the start of Object-Oriented Programming (OOP).

# Import json for saving/loading tasks to a file.
import json

# Import os so we can check if the tasks file exists before reading it.
import os


# Define a class called "Task". A class is like a cookie cutter — it defines
# the shape of every Task object we create. The name "Task" is capitalized
# by Python convention for class names.
class Task:
    # "__init__" is a special method called a "constructor." It runs automatically
    # whenever you create a new Task object. "self" refers to the new object being
    # created. "name" and "done" are the values you pass in when creating it.
    # done=False means if you don't specify done, it defaults to False.
    def __init__(self, name, done=False):
        # Store the name as an attribute on this specific Task object.
        # "self.name" means "the name attribute belonging to THIS object."
        self.name = name

        # Store the done status. Each Task object has its own done value.
        self.done = done

    # Define a method (function inside a class) to mark this task complete.
    # "self" refers to the specific task object this method is called on.
    def complete(self):
        # Set THIS task's done status to True.
        self.done = True

    # Define a method to mark this task as NOT complete.
    def uncomplete(self):
        # Set THIS task's done status back to False.
        self.done = False

    # Define a method that converts this Task object into a plain dictionary.
    # This is needed so we can save it to a JSON file (JSON can't store objects).
    def to_dict(self):
        # Return a dictionary with the same data. This bridges between
        # our fancy Task objects and the simple dicts that JSON understands.
        return {"name": self.name, "done": self.done}

    # Define a method to print this task with a number and checkbox.
    # "index" is the position in the list (0-based), used for numbering.
    def display(self, index):
        # Choose the checkbox symbol based on completion status.
        status = "✓" if self.done else " "

        # Print with 1-based numbering (index + 1) and the task name.
        print(str(index + 1) + ". [" + status + "] " + self.name)


# Define a standalone function to save the list of Task objects to a file.
def save_tasks(tasks):
    # Open "tasks.json" in write mode. "with" auto-closes the file.
    with open("tasks.json", "w") as file:
        # Convert each Task object to a dictionary using a list comprehension.
        # A list comprehension is a compact way to loop and transform: it says
        # "for each task in the list, call task.to_dict() and collect the results."
        data = [task.to_dict() for task in tasks]

        # Write the list of dictionaries to the file as JSON.
        json.dump(data, file, indent=2)


# Define a standalone function to load tasks from a JSON file.
def load_tasks():
    # Check if the file exists before trying to read it.
    if os.path.exists("tasks.json"):
        # Open in read mode and parse the JSON.
        with open("tasks.json", "r") as file:
            # Read the JSON data (a list of dictionaries).
            data = json.load(file)

            # Convert each dictionary BACK into a Task object using a list
            # comprehension. This recreates the objects from saved data.
            # item["name"] gets the name, item["done"] gets the done status.
            return [Task(item["name"], item["done"]) for item in data]

    # No file found — return an empty list.
    return []


# Load previously saved tasks (or start fresh if no file exists).
tasks = load_tasks()

# Start the interactive menu loop.
while True:
    # Print a blank line and all 7 menu options.
    print("\n1. Add task")
    print("2. List tasks")
    print("3. Mark task complete")
    print("4. Mark task incomplete")
    print("5. Edit task")
    print("6. Delete task")
    print("7. Quit")

    # Get the user's menu choice.
    choice = input("Choose an option: ")

    if choice == "1":
        # Add a new task: get the name, create a Task object, save.
        name = input("Task name: ")

        # Create a new Task object and append it directly to the list.
        # This replaces the old add_task() function — the class handles it now.
        tasks.append(Task(name))

        save_tasks(tasks)

    elif choice == "2":
        # List all tasks: loop with index and call each task's display() method.
        for i in range(len(tasks)):
            # Each Task object knows how to display itself via its display() method.
            tasks[i].display(i)

    elif choice == "3":
        # Mark a task complete: show list, ask for number, call complete() method.
        for i in range(len(tasks)):
            tasks[i].display(i)

        # Get a valid task number from the user (1-based) and convert to 0-based.
        index = int(input("Which task number to complete? ")) - 1

        # Call the complete() method on the specific Task object.
        tasks[index].complete()

        save_tasks(tasks)

    elif choice == "4":
        # Mark a task incomplete: show list, ask for number, call uncomplete().
        for i in range(len(tasks)):
            tasks[i].display(i)

        index = int(input("Which task number to mark incomplete? ")) - 1

        # Call the uncomplete() method on the specific Task object.
        tasks[index].uncomplete()

        save_tasks(tasks)

    elif choice == "5":
        # Edit a task name: show list, ask for number, set new name directly.
        for i in range(len(tasks)):
            tasks[i].display(i)

        index = int(input("Which task number to edit? ")) - 1

        new_name = input("New name: ")

        # Directly overwrite the "name" attribute on the Task object.
        tasks[index].name = new_name

        save_tasks(tasks)

    elif choice == "6":
        # Delete a task: show list, ask for number, remove from list.
        for i in range(len(tasks)):
            tasks[i].display(i)

        index = int(input("Which task number to delete? ")) - 1

        # .pop() removes the Task object at the given index from the list.
        tasks.pop(index)

        save_tasks(tasks)

    elif choice == "7":
        # Quit: break exits the loop and ends the program.
        break

    else:
        # Invalid option: remind the user to pick a valid number.
        print("Invalid option, try again.")
