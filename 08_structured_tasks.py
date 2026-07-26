# FILE: 08_structured_tasks.py
# PURPOSE: This exercise upgrades the task list from plain strings to
#          dictionaries. Each task is now a dict with a "name" and a "done"
#          status. This teaches how dictionaries let you attach multiple
#          pieces of info to one item — a foundation for real apps.

# Create an empty list to hold all tasks. Each task will be a dictionary.
tasks = []

# Define a function that takes a task name and creates a task dictionary.
def add_task(name):
    # Create a dictionary with two keys: "name" holds the task text,
    # and "done" starts as False (the task is not yet complete).
    # Dictionaries use curly braces {} and key-value pairs separated by colons.
    task = {"name": name, "done": False}

    # Add the new task dictionary to the tasks list.
    tasks.append(task)

# Define a function to display all tasks with their completion status.
def list_tasks():
    # Loop through each task dictionary in the list.
    for task in tasks:
        # Use a ternary expression: if task["done"] is True, status = "✓".
        # Otherwise status = " " (a space). The ✓ shows the task is complete.
        # This is a compact if/else written on one line.
        status = "✓" if task["done"] else " "

        # Print each task with a checkbox: "[✓] Buy groceries" or "[ ] Call bank".
        # task["name"] accesses the value stored under the "name" key.
        print("[" + status + "] " + task["name"])

# Add three sample tasks. Each becomes a dictionary like {"name": "...", "done": False}.
add_task("Buy groceries")
add_task("Finish portfolio project")
add_task("Call the bank")

# Display all tasks. They should all show "[ ]" since none are marked done yet.
list_tasks()
