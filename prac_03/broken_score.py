"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    # get user input
    score = float(input("Enter score: "))

    result = determine_score(score)

    print(result)

    result = determine_score(random.randint(0, 100))

    print(result)


def determine_score(score):
    """Computes the score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


main()
