# FILE: 06_return.py
# PURPOSE: This exercise teaches the difference between printing and returning.
#          A function can PRINT text to the screen (exercise 05) or RETURN a
#          value back to the code that called it. Returning is more flexible
#          because the caller decides what to do with the value.

# Define a function called "build_greeting" that takes one parameter, "name".
def build_greeting(name):
    # Check if the name matches "Landon".
    if name == "Landon":
        # "return" sends this text back to wherever the function was called.
        # It does NOT print it — it hands the string back like passing a note.
        return "Hey, it's you!"
    else:
        # For any other name, return a generic greeting string.
        return "Hello, " + name + "!"

# Call the function with "Landon" and store the returned value in "message".
# So "message" now holds the string "Hey, it's you!".
message = build_greeting("Landon")

# NOW we print the value. This shows the key difference: the function builds
# the greeting, and the calling code decides to print it.
print(message)

# Call the function again with a different name. This time "message2" holds
# "Hello, notLandon!".
message2 = build_greeting("notLandon")

# Print the second greeting.
print(message2)
