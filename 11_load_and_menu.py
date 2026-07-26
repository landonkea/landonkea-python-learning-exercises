# FILE: 11_load_and_menu.py
# PURPOSE: This exercise brings everything together into an interactive menu
#          loop. The user can add, list, complete, and uncomplete tasks, and
#          the data loads from and saves to a file. This is a real usable app.

# Import the json module for reading/writing JSON files.
import json

# Import the os module so we can check if a file exists before trying to read it.
import os

# Create an empty list to hold task dictionaries.
tasks = []

# Define a function to add a task. Same pattern as before.
def add_task(name):
    # Create a task dictionary with name and done=False.
    task = {"name": name, "done": False}

    # Add it to the list.
    tasks.append(task)

# Define a function to display all tasks WITH NUMBERS so the user can pick one.
def list_tasks():
    # "range(len(tasks))" generates numbers from 0 to the length of the list minus 1.
    # This gives us an index number for each task, which we need for completing/editing.
    for i in range(len(tasks)):
        # Get the task at position "i" in the list.
        task = tasks[i]

        # Determine the checkbox symbol based on the done status.
        status = "✓" if task["done"] else " "

        # Print with a number prefix. "i + 1" makes numbering start at 1 instead of 0
        # (humans count from 1, computers count from 0). str() converts the number
        # to text so it can be joined with the rest of the string.
        print(str(i + 1) + ". [" + status + "] " + task["name"])

# Define a function to mark a task complete by its INDEX (position number).
def complete_task(index):
    # Access the task at the given index and set its "done" value to True.
    # This is faster than searching by name — we already know the position.
    tasks[index]["done"] = True

# Define a function to mark a task as NOT complete (undo a completion).
def uncomplete_task(index):
    # Access the task at the given index and set "done" back to False.
    tasks[index]["done"] = False

# Define a function to save all tasks to the JSON file.
def save_tasks():
    # Open "tasks.json" in write mode. "with" auto-closes the file when done.
    with open("tasks.json", "w") as file:
        # Dump the tasks list to the file. indent=2 makes the JSON readable
        # (pretty-printed with spaces) instead of one long squished line.
        json.dump(tasks, file, indent=2)

# Define a function to load tasks from the JSON file if it exists.
def load_tasks():
    # os.path.exists() checks if the file is on disk. If the file doesn't
    # exist yet (first time running), we skip reading and return an empty list.
    if os.path.exists("tasks.json"):
        # Open the file in read mode ("r") and load the JSON data back
        # into a Python list of dictionaries.
        with open("tasks.json", "r") as file:
            # json.load() reads JSON text and converts it back to Python data.
            return json.load(file)

    # If no file exists, return an empty list — we have no saved tasks yet.
    return []

# Load any previously saved tasks. If the file exists, tasks gets populated.
# If not, tasks stays as an empty list. This is why data survives between runs.
tasks = load_tasks()

# Start an infinite loop that shows the menu until the user chooses to quit.
# "while True" means "loop forever" — we'll use "break" to exit later.
while True:
    # Print the menu options. "\n" at the start adds a blank line for readability.
    print("\n1. Add task")
    print("2. List tasks")
    print("3. Mark task complete")
    print("4. Mark task incomplete")
    print("5. Quit")

    # Get the user's menu choice as text. input() always returns a string.
    choice = input("Choose an option: ")

    # Check which option the user picked using if/elif chain.
    if choice == "1":
        # Option 1: Add a new task.
        name = input("Task name: ")  # Ask for the task name.

        add_task(name)  # Add it to the list.

        save_tasks()  # Save immediately so it's not lost if the program crashes.

    elif choice == "2":
        # Option 2: List all tasks with numbers and checkboxes.
        list_tasks()

    elif choice == "3":
        # Option 3: Mark a task as complete.
        list_tasks()  # Show tasks first so the user can see the numbers.

        # Ask which task number. int() converts the text to a number.
        # We subtract 1 because lists start at 0 but we display from 1.
        index = int(input("Which task number to complete? ")) - 1

        complete_task(index)  # Mark that task done.

        save_tasks()  # Save to file immediately.

    elif choice == "4":
        # Option 4: Mark a task as incomplete (undo completion).
        list_tasks()  # Show the current task list.

        # Ask which task number and convert to a 0-based index.
        index = int(input("Which task number to mark incomplete? ")) - 1

        uncomplete_task(index)  # Set done back to False.

        save_tasks()  # Save to file.

    elif choice == "5":
        # Option 5: Quit the program. "break" exits the while True loop.
        break

    else:
        # If the user typed something other than 1-5, show an error message.
        print("Invalid option, try again.")
