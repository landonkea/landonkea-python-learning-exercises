# FILE: 01-greet.py
# PURPOSE: This is the very first exercise. It asks the user for their name
#          and prints a greeting. It teaches the two most basic concepts:
#          getting input from a user and printing output to the screen.

# Ask the user to type their name. input() shows the text in quotes on screen,
# then waits for the user to press Enter. Whatever they type gets stored in
# the variable called "name". Think of a variable like a labeled box that holds
# a value, here the box is labeled "name" and it holds whatever the user typed.
name = input("What is your name? ")

# Print a greeting to the screen. The + signs join (concatenate) pieces of text
# together into one string. So if the user typed "Alice", this becomes
# "Hello, " + "Alice" + "!" which equals "Hello, Alice!".
# print() is a built-in Python function that displays text on the screen.
print("Hello, " + name + "!")
