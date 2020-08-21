"""
CP1404/CP5632 - Practical
Scores program to determine what the score is based on value
"""


def main():



def get_valid_integer():
    """Get valid integer from user"""
    valid_input = False
    while not valid_input:
        try:
            number = int(input("Enter a score:"))
            valid_input = True
        except ValueError:
            print("Error: not a valid integer")
    return number



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