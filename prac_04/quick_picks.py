"""
CP1404/CP5632 Practical - Christian Torrisi
Do-from-scratch - Quick Picks Exercise
"""

import random

NUMBERS = [i for i in range(1, 46)]


def main():
    """Asks the user how many quick picks they want to play then chooses 6 random numbers
    for the number of games they have chosen"""
    number_of_quick_picks = int(input("How many quick picks?: "))

    all_quick_picks = get_all_quick_picks(number_of_quick_picks)

    for quick_pick in all_quick_picks:
        for number in quick_pick:
            print("{:>2}".format(number), end=" ")
        print()


def get_all_quick_picks(number_of_quick_picks):
    """Generate a number of single quick pick 'games' based on the user input """
    all_quick_picks = []
    for i in range(number_of_quick_picks):
        all_quick_picks.append(get_single_quick_pick())

    return all_quick_picks


def get_single_quick_pick():
    """Chooses 6 unique random numbers from the numbers list for a single quick pick 'game'"""
    single_quick_pick = []
    while len(single_quick_pick) < 6:
        number = random.choice(NUMBERS)

        if number not in single_quick_pick:
            single_quick_pick.append(number)

        else:
            number = random.choice(NUMBERS)

    return single_quick_pick


main()
