"""
CP1404/CP5632 Practical - Christian Torrisi
Using dictionaries
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()


def get_code_max_length():
    codes = [code for code in CODE_TO_NAME]
    max_length = len(max(codes, key=len))
    return max_length


max_code_length = get_code_max_length()

for code, name in CODE_TO_NAME.items():
    print("{:{max_code_length}} is {}".format(code, name, max_code_length=max_code_length))
