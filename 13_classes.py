class Task:
    def __init__(self, name):
        self.name = name
        self.done = False

    def complete(self):
        self.done = True

    def uncomplete(self):
        self.done = False

    def display(self):
        status = "✓" if self.done else " "
        print("[" + status + "] " + self.name)


tasks = []

task1 = Task("Buy groceries")
task2 = Task("Finish portfolio project")

tasks.append(task1)
tasks.append(task2)

task1.complete()

for task in tasks:
    task.display()
