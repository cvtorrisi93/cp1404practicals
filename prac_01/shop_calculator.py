"""
CP1404/CP5632 - Practical
Do-from-scratch - Shop Calculator
"""

# declare variable
total_cost = 0

# get user input
number_of_items = int(input("Number of items: "))

# error checking loop
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

# for loop for number of items chosen
for i in range(number_of_items):
    # get each item cost
    single_item_cost = float(input("Price of item: "))
    # add item cost to the total
    total_cost += single_item_cost

# add discount if necessary
if total_cost > 100:
    total_cost *= 0.9

print("Total price for {} items is ${:.2f}".format(number_of_items, total_cost))
