# FILE: 12_edit_and_delete.py
# PURPOSE: This exercise adds editing and deleting tasks to the menu app.
#          It teaches .pop() (removing list items) and dictionary key updates.
#          This is the most complete version of the plain-function task manager
#          before we move on to classes.

# Import json for file I/O (saving/loading tasks as JSON).
import json

# Import os so we can check if the tasks file exists before reading it.
import os

# Create an empty list to hold task dictionaries.
tasks = []

# Define a function to add a task to the list.
def add_task(name):
    # Create a dictionary with "name" and "done" (starts as False).
    task = {"name": name, "done": False}

    # Append it to the tasks list.
    tasks.append(task)

# Define a function to display all tasks with numbered lists and checkboxes.
def list_tasks():
    # Loop with index numbers using range(len(tasks)).
    for i in range(len(tasks)):
        # Get the task dictionary at position i.
        task = tasks[i]

        # Choose checkbox symbol based on the done status.
        status = "✓" if task["done"] else " "

        # Print with 1-based numbering. str() converts the number to text.
        print(str(i + 1) + ". [" + status + "] " + task["name"])

# Define a function to mark a task complete by its index.
def complete_task(index):
    # Set the "done" key to True for the task at the given position.
    tasks[index]["done"] = True

# Define a function to mark a task incomplete by its index.
def uncomplete_task(index):
    # Set the "done" key back to False for the task at the given position.
    tasks[index]["done"] = False

# Define a function to save all tasks to a JSON file.
def save_tasks():
    # Open "tasks.json" in write mode. "with" guarantees the file closes.
    with open("tasks.json", "w") as file:
        # Convert the tasks list to JSON and write it to the file.
        json.dump(tasks, file, indent=2)

# Define a function to load tasks from the JSON file if it exists.
def load_tasks():
    # Check if the file exists on disk before trying to open it.
    if os.path.exists("tasks.json"):
        # Open in read mode and parse the JSON back into a Python list.
        with open("tasks.json", "r") as file:
            return json.load(file)

    # No file found, return an empty list (fresh start).
    return []

# Define a NEW function to change the name of an existing task.
def edit_task(index, new_name):
    # Access the task at the given index and overwrite its "name" key
    # with the new name. This modifies the dictionary in place.
    tasks[index]["name"] = new_name

# Define a NEW function to remove a task from the list entirely.
def delete_task(index):
    # .pop(index) removes the item at the given position and shifts
    # everything after it down by one. The list gets one item shorter.
    tasks.pop(index)

# Load any previously saved tasks from the JSON file.
tasks = load_tasks()

# Start the infinite menu loop. This runs until the user picks "Quit".
while True:
    # Print a blank line and all 7 menu options.
    print("\n1. Add task")
    print("2. List tasks")
    print("3. Mark task complete")
    print("4. Mark task incomplete")
    print("5. Edit task")       # NEW option compared to exercise 11
    print("6. Delete task")     # NEW option compared to exercise 11
    print("7. Quit")

    # Get the user's choice as a string.
    choice = input("Choose an option: ")

    if choice == "1":
        # Add a new task: get the name, add it, save to file.
        name = input("Task name: ")

        add_task(name)

        save_tasks()

    elif choice == "2":
        # List all tasks with numbers and checkboxes.
        list_tasks()

    elif choice == "3":
        # Mark a task complete: show list, ask for number, mark done, save.
        list_tasks()

        # Convert user input to a 0-based index (user sees 1-based numbers).
        index = int(input("Which task number to complete? ")) - 1

        complete_task(index)

        save_tasks()

    elif choice == "4":
        # Mark a task incomplete: show list, ask for number, uncomplete, save.
        list_tasks()

        index = int(input("Which task number to mark incomplete? ")) - 1

        uncomplete_task(index)

        save_tasks()

    elif choice == "5":
        # Edit a task name: show list, ask for number, ask for new name, update, save.
        list_tasks()

        index = int(input("Which task number to edit? ")) - 1

        new_name = input("New name: ")  # Get the replacement name from the user.

        edit_task(index, new_name)  # Overwrite the old name with the new one.

        save_tasks()

    elif choice == "6":
        # Delete a task: show list, ask for number, remove from list, save.
        list_tasks()

        index = int(input("Which task number to delete? ")) - 1

        delete_task(index)  # Remove the task from the list entirely.

        save_tasks()

    elif choice == "7":
        # Quit: break exits the while True loop, ending the program.
        break

    else:
        # Invalid input: remind the user to pick a valid option.
        print("Invalid option, try again.")
