# FILE: 09_mark_complete.py
# PURPOSE: This exercise adds the ability to mark a task as complete.
#          It teaches how to SEARCH through a list and UPDATE a specific item.
#          This is a common pattern: find something, then change it.

# Create an empty list to hold task dictionaries.
tasks = []

# Define a function to add a new task. Same as exercise 08.
def add_task(name):
    # Create a dictionary with "name" and "done" (starts as False).
    task = {"name": name, "done": False}

    # Append the new task dictionary to the tasks list.
    tasks.append(task)

# Define a function to display all tasks. Same as exercise 08.
def list_tasks():
    # Loop through each task in the list.
    for task in tasks:
        # Show "✓" if done, " " (space) if not done — the ternary trick.
        status = "✓" if task["done"] else " "

        # Print the task with a checkbox prefix.
        print("[" + status + "] " + task["name"])

# Define a NEW function to mark a task as complete by its name.
def complete_task(name):
    # Loop through every task in the list to find the matching one.
    for task in tasks:
        # Check if this task's name matches the name we're looking for.
        if task["name"] == name:
            # Set the "done" key to True. Since dictionaries are mutable,
            # this changes the actual task in the list — no need to re-add it.
            task["done"] = True

# Add three sample tasks.
add_task("Buy groceries")
add_task("Finish portfolio project")
add_task("Call the bank")

# Mark "Buy groceries" as complete. After this, its "done" value becomes True.
complete_task("Buy groceries")

# Display all tasks. "Buy groceries" should now show "[✓]" while the others show "[ ]".
list_tasks()
