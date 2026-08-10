# FILE: 02_conditional.py
# PURPOSE: This exercise builds on the greeting by adding a conditional check.
#          It teaches "if/else", the idea that a program can make decisions
#          based on what the user types.

# Ask the user for their name, just like in exercise 01.
# The name they type is stored in the "name" variable.
name = input("What is your name? ")

# Check if the name the user typed is exactly "Landon".
# == is the "equal to" comparison operator, it checks if two things match.
# If the user typed "Landon", this condition is True and the next indented
# line runs. If they typed anything else, Python skips to the "else" block.
if name == "Landon":
    # This line only runs when the name IS "Landon". It prints a casual
    # personalized greeting. The indented lines below "if" are the "body"
    # of the if-statement, Python knows they belong to the if because of
    # the indentation (extra spaces at the start of the line).
    print("Hey, it's you!")
else:
    # The "else" block runs when the condition above is False, meaning the
    # user typed something other than "Landon". It prints a generic greeting
    # using the same string concatenation (+) we learned in exercise 01.
    print("Hello, " + name + "!")
