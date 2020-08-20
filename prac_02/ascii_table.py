"""
CP1404/CP5632 - Practical - Christian Torrisi
Practice - ASCII Table
"""

LOWER_BOUND = 33
UPPER_BOUND = 127

character = input("Enter a character: ")
ascii_code = ord(character)

print("The ASCII code for {} is {}".format(character, ascii_code))

ascii_code = int(input("Enter a number between {} and {}: ".format(LOWER_BOUND, UPPER_BOUND)))
character = chr(ascii_code)

print("The character for {} is {}".format(ascii_code, character))

print("For future reference, here is a table of ASCII Codes and their characters")

# single column (for both)
for i in range(LOWER_BOUND, UPPER_BOUND):
    print("{:>3} is {}".format(i, chr(i)))

# user input columns
number_of_columns = int(input("How many columns would you like? "))

for i in range(LOWER_BOUND, UPPER_BOUND, number_of_columns):
    for j in range(number_of_columns):
        print("{:>3} is {}".format(i, chr(i)), end="  |  ")
        i += 1
        if i > UPPER_BOUND:
            break
    print()
