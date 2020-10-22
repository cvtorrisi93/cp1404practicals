"""
CP1404/CP5632 Practical - Christian Torrisi
Intermediate Exercise - Cleanup Files
"""

import os


def main():
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print(new_name)
            os.rename(os.path.join(directory_name, filename), os.path.join(directory_name, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""

    new_name = ""
    previous_character = ""
    for character in filename:
        if (character.isupper() or character == "(") and previous_character.isalpha():
            new_name += "_" + character
        elif (character.islower() and previous_character == " ") or previous_character == "(":
            new_name += character.upper()
        else:
            new_name += character
        previous_character = character

    return new_name.replace(" ", "_").replace(".T_X_T", ".txt")


main()
