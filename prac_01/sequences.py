"""
CP1404/CP5632 - Practical
Extension - Menu-driven number sequence generator

Assumptions: Second number must be larger than the first number
"""

import math

print("Welcome to the menu-driven number sequence generator!")

# get user inputs
first_number = int(input("Please select the first number: "))
second_number = int(input("Please select the second number: "))

# error checking for assumption
while second_number <= first_number:
    print("Please choose a number larger than", first_number)
    second_number = int(input("Please select the second number: "))

# apply number variables to constant menu
MENU = f"""Please select from one of the options below:
    Show the (E)ven numbers from {first_number} to {second_number}
    Show the (O)dd numbers from {first_number} to {second_number}
    Show the (S)quare numbers from {first_number} to {second_number}
    (Q)uit"""

# get use input
print(MENU)
choice = input(">>> ").upper()

# error checking menu
while choice != "Q":
    if choice == "E":
        for i in range(first_number, second_number + 1, 1):
            if i % 2 == 0:
                print(i, end=' ')
    elif choice == "O":
        for i in range(first_number, second_number+1, 1):
            if i % 2 == 1:
                print(i, end=' ')
    elif choice == "S":
        for i in range(first_number, second_number + 1, 1):
            square_root = math.sqrt(i)
            if int(square_root + 0.5) ** 2 == i:
                print(i, end=' ')

    print("\n", MENU)
    choice = input(">>> ").upper()

print("Thank you for using the menu-driven number sequence generator.")