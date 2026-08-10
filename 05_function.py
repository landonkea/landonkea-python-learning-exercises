# FILE: 05_function.py
# PURPOSE: This exercise teaches functions, reusable blocks of code that you
#          can call by name. Instead of writing the greeting logic over and over,
#          we put it inside a function and call it whenever we need it.

# "def" means "define a function." We're creating a function called "greet".
# The word "name" in parentheses is a "parameter", it's a placeholder that
# will be filled in with an actual value each time the function is called.
# Think of a function like a recipe: "name" is an ingredient you provide.
def greet(name):
    # Check if the name passed in is "LandonTheFirst".
    # This is the same if/else logic from exercise 02, but now it's inside
    # a reusable function instead of sitting at the top level of the script.
    if name == "LandonTheFirst":
        # Print the casual greeting if the name matches.
        print("Hey, it's you!")
    else:
        # Print the generic greeting for any other name.
        print("Hello, " + name + "!")

# Now we "call" (use) the greet function three times with different names.
# Each time, the name in parentheses is the "argument", the actual value
# that fills in the "name" parameter inside the function.
greet("LandonTheFirst")  # This will print "Hey, it's you!"
greet("LandonTheSecond")  # This will print "Hello, LandonTheSecond!"
greet("LandonTheThird")  # This will print "Hello, LandonTheThird!"
