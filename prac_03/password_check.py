"""
CP1404/CP5632 - Practical - Christian Torrisi
Written practice - Password to Asterisk
"""

def main():
    MIN_LENGTH = 8

    password = get_password()

    while len(password) < MIN_LENGTH:
        password = input("Error! Enter your password of 5 or more characters: ")

    convert_password(password)


def convert_password(password):
    """Prints an asterisk for each character in a password"""
    for character in password:
        print("*", end="")


def get_password():
    """Gets user input for the password"""
    password = input("Enter your password: ")
    return password


main()
