"""
CP1404/CP5632 Practical - Christian Torrisi
List exercises
"""


def main():
    numbers = get_numbers()
    print_number_outputs(numbers)


def print_number_outputs(lst):
    print("The first number is {}".format(lst[1]))
    print("The last number is {}".format(lst[-1]))
    print("The smallest number is {}".format(min(lst)))
    print("The largest number is {}".format(max(lst)))
    print("The average of numbers is {}".format(sum(lst) / len(lst)))


def get_numbers():
    """Gets 5 number from the user"""
    numbers = []
    for i in range(5):
        number = int(input("Number: "))
        numbers.append(number)
    return numbers


main()
