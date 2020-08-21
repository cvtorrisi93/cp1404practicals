"""
CP1404/CP5632 - Practical
Scores program to determine what the score is based on value
"""

import random

MIN_SCORE = 0
MAX_SCORE = 100


def main():

    output_file = open("results.txt", 'w')

    number_of_scores = get_valid_integer("Enter a number of scores to generate: ")

    for i in range(number_of_scores):
        score = get_random_score()
        result = determine_score(score)
        print("{} is {}".format(score, result), file=output_file)


def get_random_score():
    """Produces a random int between the minimum and maximum score"""
    score = random.randint(MIN_SCORE, MAX_SCORE)
    return score


def get_valid_integer(prompt):
    """Get valid integer from user"""
    valid_input = False
    while not valid_input:
        try:
            number = int(input(prompt))
            valid_input = True
        except ValueError:
            print("Error: not a valid integer")
    return number


def determine_score(score):
    """Computes the score"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
