# FILE: 10_save_tasks.py
# PURPOSE: This exercise teaches file I/O (input/output) — saving data to a
#          file so it survives after the program ends. We use JSON, a common
#          text format that's easy for both humans and machines to read.

# import brings in code from Python's standard library. "json" lets us
# convert Python data to/from JSON text format.
import json

# Create an empty list to hold task dictionaries.
tasks = []

# Define a function to add a new task. Same as exercises 08-09.
def add_task(name):
    # Create a task dictionary with a name and a "done" status of False.
    task = {"name": name, "done": False}

    # Add the task to the list.
    tasks.append(task)

# Define a function to display all tasks. Same as before.
def list_tasks():
    # Loop through each task and print it with a checkbox.
    for task in tasks:
        # Show "✓" if done, " " if not — the ternary expression.
        status = "✓" if task["done"] else " "

        # Print the formatted task line.
        print("[" + status + "] " + task["name"])

# Define a function to mark a task complete by searching its name.
def complete_task(name):
    # Loop through all tasks to find the match.
    for task in tasks:
        # If this task's name matches, mark it done.
        if task["name"] == name:
            # Set done to True — this modifies the dictionary in place.
            task["done"] = True

# Define a NEW function to save all tasks to a file.
def save_tasks():
    # "with open(...)" opens a file safely. "w" means write mode — it creates
    # the file if it doesn't exist, or overwrites it if it does.
    # "as file" gives us a variable name to use for the opened file.
    # The "with" statement automatically closes the file when the block ends.
    with open("tasks.json", "w") as file:
        # json.dump() converts the Python list of dicts into JSON text
        # and writes it to the file. "tasks.json" will contain something like:
        # [{"name": "Buy groceries", "done": true}, ...]
        json.dump(tasks, file)

# Add three sample tasks.
add_task("Buy groceries")
add_task("Finish portfolio project")
add_task("Call the bank")

# Mark "Buy groceries" as complete.
complete_task("Buy groceries")

# Display all tasks on screen so the user can see them.
list_tasks()

# Save the tasks to "tasks.json" so they persist after the program closes.
save_tasks()
