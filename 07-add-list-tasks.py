# FILE: 07-add-list-tasks.py
# PURPOSE: This exercise starts building a real task manager. It teaches how
#          to create an empty list, add items to it with a function, and
#          display all items. This is where the project shifts from abstract
#          exercises to building something actually useful.

# Create an empty list. The square brackets [] with nothing inside mean
# "this list has zero items right now." We'll add items to it later.
# This list lives at the top level so all functions can access it.
tasks = []

# Define a function that takes one argument: the name of a task to add.
def add_task(task_name):
    # .append() is a list method that adds a new item to the END of the list.
    # So if tasks was ["Buy groceries"], after appending "Call the bank" it
    # becomes ["Buy groceries", "Call the bank"]. The list grows by one item.
    tasks.append(task_name)

# Define a function that takes NO arguments — it uses the "tasks" list directly.
def list_tasks():
    # Loop through each task in the "tasks" list. On each pass, the variable
    # "task" holds the current task name as a string.
    for task in tasks:
        # Print each task with a "- " prefix to make it look like a bullet list.
        # So "Buy groceries" prints as "- Buy groceries".
        print("- " + task)

# Add three tasks to the list by calling add_task() three times.
add_task("Buy groceries")        # tasks is now ["Buy groceries"]
add_task("Finish portfolio project")  # tasks is now ["Buy groceries", "Finish portfolio project"]
add_task("Call the bank")        # tasks now has all three items

# Call list_tasks() to display all the tasks on screen.
list_tasks()
