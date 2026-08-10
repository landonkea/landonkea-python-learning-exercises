# FILE: 03_loop.py
# PURPOSE: This exercise teaches loops, the ability to repeat an action
#          multiple times without writing the same line over and over.

# Ask the user for their name. Same as exercises 01 and 02.
name = input("What is your name? ")

# "for i in range(3)" creates a loop that runs exactly 3 times.
# range(3) generates the numbers 0, 1, 2 (three numbers total).
# Each time through the loop, the variable "i" holds the current number.
# We don't actually use "i" in this example, we just need the loop to
# repeat 3 times. This is like saying "do this 3 times."
for i in range(3):
    # This line runs once per loop iteration, so it prints 3 greetings total.
    # Imagine telling someone "say hello 3 times", this is the "say hello" part.
    print("Hello, " + name + "!")
