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

        # if extension not in all_extensions:
        #     all_extensions.append(extension)
        #     os.mkdir(extension)
        # else:
        #     pass

        """ Method above (first attempt) only handles sorting once
            Method below handles sorting consistently"""
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass

        shutil.move(filename, extension + "/" + filename)


main()
