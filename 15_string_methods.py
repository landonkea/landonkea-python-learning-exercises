# FILE: 15_string_methods.py
# PURPOSE: This exercise adds input validation using string methods. It teaches
#          .strip() (removing whitespace) and how to prevent empty task names.
#          This is the most polished version of the task manager, it has
#          error handling, input validation, and clean code structure.

# Import json for saving/loading tasks to a JSON file.
import json

# Import os to check if the tasks file exists before reading it.
import os


# Define the Task class, same as exercises 13 and 14.
class Task:
    # Constructor: creates a new Task with a name and done status.
    def __init__(self, name, done=False):
        # Store the task name on this object.
        self.name = name

        # Store the done status (defaults to False).
        self.done = done

    # Method to mark this task as complete.
    def complete(self):
        # Set done to True.
        self.done = True

    # Method to mark this task as incomplete.
    def uncomplete(self):
        # Set done back to False.
        self.done = False

    # Method to convert this Task to a dictionary for JSON saving.
    def to_dict(self):
        # Return a plain dict with name and done.
        return {"name": self.name, "done": self.done}

    # Method to print this task with a number and checkbox.
    def display(self, index):
        # Choose checkbox based on done status.
        status = "✓" if self.done else " "

        # Print formatted with 1-based number.
        print(str(index + 1) + ". [" + status + "] " + self.name)


# Function to save all Task objects to a JSON file.
def save_tasks(tasks):
    # Open "tasks.json" in write mode (creates or overwrites).
    with open("tasks.json", "w") as file:
        # Convert each Task to a dict and save as JSON with pretty formatting.
        data = [task.to_dict() for task in tasks]

        json.dump(data, file, indent=2)


# Function to load Task objects from a JSON file.
def load_tasks():
    # Check if the file exists before reading.
    if os.path.exists("tasks.json"):
        # Open in read mode and parse JSON back to Python data.
        with open("tasks.json", "r") as file:
            data = json.load(file)

            # Recreate Task objects from the saved list of dicts.
            return [Task(item["name"], item["done"]) for item in data]

    # No file exists, return an empty list.
    return []


# Function to clean up a raw task name typed by the user. Shared by both the
# "add task" and "edit task" menu options so the same rule (strip whitespace,
# reject blank names) only has to be written once.
def clean_task_name(text):
    # Remove leading/trailing whitespace first, same reason as the inline
    # .strip() calls used to: a name of "  " should count as empty.
    cleaned = text.strip()

    if cleaned == "":
        # Nothing left after stripping, signal "invalid" the same way
        # get_valid_index does: return None and let the caller print the message.
        return None

    return cleaned


# Function to safely get a valid task index from user input (same as exercise 14).
def get_valid_index(tasks, prompt):
    # Try to convert user input to a valid index. Catch errors if input is bad.
    try:
        # Ask for input and convert to int. Subtract 1 for 0-based indexing.
        index = int(input(prompt)) - 1

        # Check if the index is within the valid range of the list.
        if index < 0 or index >= len(tasks):
            # Index is out of bounds, tell the user and return None.
            print("That task number doesn't exist.")

            return None

        # Valid index, return it.
        return index

    # Catch the error that happens when the user types non-numeric text.
    except ValueError:
        # Tell the user their input wasn't a valid number.
        print("That's not a valid number.")

        # Explicitly return None to signal failure. (Python would return
        # None automatically here anyway, but spelling it out makes the
        # intent clear and matches the explicit "return index" above.)
        return None


# Only run the interactive menu when this file is executed directly
# (e.g. `python 15_string_methods.py`), not when it's imported as a module
# for testing. Without this guard, importing the file to test clean_task_name(),
# Task, save_tasks(), etc. would immediately start the menu loop and block
# waiting for keyboard input.
if __name__ == "__main__":
    # Load any previously saved tasks from the JSON file.
    tasks = load_tasks()

    # Start the interactive menu loop, runs forever until user picks Quit.
    while True:
        # Print the menu options.
        print("\n1. Add task")
        print("2. List tasks")
        print("3. Mark task complete")
        print("4. Mark task incomplete")
        print("5. Edit task")
        print("6. Delete task")
        print("7. Quit")

        # Get the user's menu choice as a string.
        choice = input("Choose an option: ")

        if choice == "1":
            # Add a new task. NEW: uses clean_task_name() to strip whitespace and
            # reject blank input, instead of a plain .strip() call, so "  " (just
            # spaces) can't sneak in as an invisible task name.
            name = clean_task_name(input("Task name: "))

            if name is None:  # clean_task_name() returns None for blank input.
                print("Task name can't be empty.")
            else:
                # The name is valid, create the Task and save.
                tasks.append(Task(name))

                save_tasks(tasks)

        elif choice == "2":
            # List all tasks with numbers and checkboxes.
            for i in range(len(tasks)):
                tasks[i].display(i)

        elif choice == "3":
            # Mark a task complete. Show list, get valid index, mark done, save.
            for i in range(len(tasks)):
                tasks[i].display(i)

            # Use safe input handling, returns None if input is bad.
            index = get_valid_index(tasks, "Which task number to complete? ")

            if index is not None:
                tasks[index].complete()

                save_tasks(tasks)

        elif choice == "4":
            # Mark a task incomplete. Show list, get valid index, uncomplete, save.
            for i in range(len(tasks)):
                tasks[i].display(i)

            index = get_valid_index(tasks, "Which task number to mark incomplete? ")

            if index is not None:
                tasks[index].uncomplete()

                save_tasks(tasks)

        elif choice == "5":
            # Edit a task name. Show list, get valid index, get new name, update, save.
            for i in range(len(tasks)):
                tasks[i].display(i)

            index = get_valid_index(tasks, "Which task number to edit? ")

            if index is not None:
                new_name = clean_task_name(input("New name: "))

                if new_name is None:  # Reject empty names after stripping.
                    print("Task name can't be empty.")
                else:
                    # Update the task's name attribute directly.
                    tasks[index].name = new_name

                    save_tasks(tasks)

        elif choice == "6":
            # Delete a task. Show list, get valid index, remove from list, save.
            for i in range(len(tasks)):
                tasks[i].display(i)

            index = get_valid_index(tasks, "Which task number to delete? ")

            if index is not None:
                # Remove the task at the given index from the list.
                tasks.pop(index)

                save_tasks(tasks)

        elif choice == "7":
            # Quit: break exits the while True loop, ending the program.
            break

        else:
            # Invalid menu choice, remind the user.
            print("Invalid option, try again.")
