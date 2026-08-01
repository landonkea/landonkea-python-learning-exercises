# FILE: 14_error_handling.py
# PURPOSE: This exercise adds error handling to the task manager. It teaches
#          try/except — how to catch errors (like bad user input) instead of
#          letting the program crash. The get_valid_index() function is the
#          key new addition that safely handles invalid input.

# Import json for saving/loading tasks to a JSON file.
import json

# Import os to check if the tasks file exists before reading it.
import os


# Define the Task class — same as exercise 13.
class Task:
    # Constructor: runs when you create a new Task. Sets name and done status.
    def __init__(self, name, done=False):
        # Store the task name as an attribute on this object.
        self.name = name

        # Store the done status (defaults to False if not provided).
        self.done = done

    # Method to mark this task as complete.
    def complete(self):
        # Set done to True.
        self.done = True

    # Method to mark this task as incomplete.
    def uncomplete(self):
        # Set done back to False.
        self.done = False

    # Method to convert this Task to a plain dictionary for JSON saving.
    def to_dict(self):
        # Return a dict with the task's data.
        return {"name": self.name, "done": self.done}

    # Method to print this task with a number and checkbox.
    def display(self, index):
        # Choose "✓" or " " based on the done status.
        status = "✓" if self.done else " "

        # Print with 1-based numbering and the task name.
        print(str(index + 1) + ". [" + status + "] " + self.name)


# Function to save all Task objects to a JSON file.
def save_tasks(tasks):
    # Open the file in write mode (creates or overwrites).
    with open("tasks.json", "w") as file:
        # Convert each Task to a dict using a list comprehension, then save.
        data = [task.to_dict() for task in tasks]

        json.dump(data, file, indent=2)


# Function to load Task objects from a JSON file (or return empty list).
def load_tasks():
    # Check if the file exists on disk.
    if os.path.exists("tasks.json"):
        # Read the file and parse JSON.
        with open("tasks.json", "r") as file:
            data = json.load(file)

            # Recreate Task objects from the saved dictionaries.
            return [Task(item["name"], item["done"]) for item in data]

    # No file found — return an empty list.
    return []


# NEW FUNCTION: Safely get a valid task index from the user.
# This is the key addition in this exercise — it handles errors gracefully.
def get_valid_index(tasks, prompt):
    # "try" starts a block of code that might cause an error.
    # If an error happens, Python jumps to the "except" block instead of crashing.
    try:
        # Ask the user for a task number using the provided prompt text.
        # int() converts the text to a number. If the user types "abc",
        # int() will raise a ValueError — and Python jumps to the "except" block.
        index = int(input(prompt)) - 1  # Subtract 1 to convert to 0-based index.

        # Check if the index is out of range (negative or too high).
        # If the user types "99" but there are only 3 tasks, this catches it.
        if index < 0 or index >= len(tasks):
            # Print a friendly error message instead of crashing.
            print("That task number doesn't exist.")

            # Return None to signal "no valid index" to the caller.
            return None

        # The index is valid — return it.
        return index

    # "except ValueError" catches the specific error that happens when int()
    # receives text that isn't a number (like "abc" or "").
    except ValueError:
        # Print a friendly message instead of a scary error traceback.
        print("That's not a valid number.")

        # Explicitly return None to signal "no valid index" to the caller.
        # (Python functions return None automatically if they fall off the
        # end without a return, but writing it out makes the intent obvious
        # and matches the explicit "return index" above.)
        return None


# Load any previously saved tasks from the file.
tasks = load_tasks()

# Start the interactive menu loop.
while True:
    # Print the menu with all 7 options.
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
        # Add a new task.
        name = input("Task name: ")

        tasks.append(Task(name))

        save_tasks(tasks)

    elif choice == "2":
        # List all tasks with numbers.
        for i in range(len(tasks)):
            tasks[i].display(i)

    elif choice == "3":
        # Mark a task complete. Show list first.
        for i in range(len(tasks)):
            tasks[i].display(i)

        # Use get_valid_index() instead of raw int() — it handles bad input.
        # If the user types something invalid, we get None back.
        index = get_valid_index(tasks, "Which task number to complete? ")

        # Only proceed if we got a valid index (not None).
        if index is not None:
            # Mark the task complete and save.
            tasks[index].complete()

            save_tasks(tasks)

    elif choice == "4":
        # Mark a task incomplete. Show list first.
        for i in range(len(tasks)):
            tasks[i].display(i)

        # Use the safe input function to get a valid index.
        index = get_valid_index(tasks, "Which task number to mark incomplete? ")

        # Only proceed if the index is valid.
        if index is not None:
            tasks[index].uncomplete()

            save_tasks(tasks)

    elif choice == "5":
        # Edit a task name. Show list first.
        for i in range(len(tasks)):
            tasks[i].display(i)

        # Get a valid index safely.
        index = get_valid_index(tasks, "Which task number to edit? ")

        if index is not None:
            new_name = input("New name: ")

            # Update the name attribute directly on the Task object.
            tasks[index].name = new_name

            save_tasks(tasks)

    elif choice == "6":
        # Delete a task. Show list first.
        for i in range(len(tasks)):
            tasks[i].display(i)

        # Get a valid index safely.
        index = get_valid_index(tasks, "Which task number to delete? ")

        if index is not None:
            # Remove the task from the list entirely.
            tasks.pop(index)

            save_tasks(tasks)

    elif choice == "7":
        # Quit the program by breaking out of the while True loop.
        break

    else:
        # The user typed something that isn't 1-7.
        print("Invalid option, try again.")
