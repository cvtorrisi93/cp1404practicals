"""
CP1404/CP5632 Practical - Christian Torrisi
List exercises
"""

USERNAMES = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


def main():
    numbers = get_numbers()
    print_number_outputs(numbers)

    username = input("Username: ")

    check_username_access(username)


def check_username_access(username):
    """Check if user input matches any element in USERNAMES list"""
    if username in USERNAMES:
        print("Access granted")
    else:
        print("Access denied")


def print_number_outputs(lst):
    print("The first number is {}".format(lst[1]))
    print("The last number is {}".format(lst[-1]))
    print("The smallest number is {}".format(min(lst)))
    print("The largest number is {}".format(max(lst)))
    print("The average of numbers is {}".format(sum(lst) / len(lst)))


def get_numbers(x=5):
    """Gets numbers based on above parameter from the user"""
    numbers = []
    for i in range(x):
        number = int(input("Number: "))
        numbers.append(number)
    return numbers


main()
