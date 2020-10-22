"""
CP1404/CP5632 Practical - Christian Torrisi
Do-from-scratch - Sort Files Exercise Version 1
"""

import os
import shutil


def main():
    os.chdir('FilesToSort')
    all_extensions = []
    for filename in os.listdir('.'):

        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]

        if extension not in all_extensions:
            folder_choice = input("What category would you like to sort the {} files into? ".format(extension))
            all_extensions.append(extension)
            try:
                os.mkdir(folder_choice)
            except FileExistsError:
                pass
        else:
            pass

        shutil.move(filename, folder_choice + "/" + filename)


main()
