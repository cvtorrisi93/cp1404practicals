"""
CP1404/CP5632 Practical - Christian Torrisi
Using dictionaries
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}


def main():

    print(CODE_TO_NAME)

    state_code = input("Enter short state: ").upper()
    while state_code != "":
        if state_code in CODE_TO_NAME:
            print(state_code, "is", CODE_TO_NAME[state_code])
        else:
            print("Invalid short state")
        state_code = input("Enter short state: ").upper()

    max_code_length = get_code_max_length()

    for state_short, state_long in CODE_TO_NAME.items():
        print("{:{max_code_length}} is {}".format(state_short, state_long, max_code_length=max_code_length))


def get_code_max_length():
    states_short = list(CODE_TO_NAME.keys())
    max_length = len(max(states_short, key=len))
    return max_length


main()
