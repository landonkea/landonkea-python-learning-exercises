# FILE: 04_list_loop.py
# PURPOSE: This exercise teaches two things at once: lists (collections of
#          items) and looping through a list. Instead of looping a fixed number
#          of times, we loop once per item in the list.

# Create a list of three names. A list is written with square brackets [],
# and items are separated by commas. This list is stored in the variable
# "names". Think of it like a shopping list — it holds multiple things in order.
names = ["LandonTheFirst", "LandonTheSecond", "LandonTheThird"]

# "for name in names" loops through each item in the "names" list, one at a
# time. On the first pass, "name" holds "LandonTheFirst". On the second pass,
# it holds "LandonTheSecond". On the third, "LandonTheThird".
# This is called a "for-each" loop — for each item in the list, do something.
for name in names:
    # Print a greeting for the current name. This line runs once per list item,
    # so it prints 3 greetings total — one for each name in the list.
    print("Hello, " + name + "!")
