"""
CP1404/CP5632 Practical - Christian Torrisi
Data file -> lists program
"""

import csv

FILENAME = "subject_data.txt"


def main():
    data = get_data()

    # NOTE: function in assignment can be used for formatting length of "columns"
    for subject in data:
        print("{} is taught by {:12} and has {:3} students".format(subject[0], subject[1], subject[2]))


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_data = []
    with open(FILENAME) as input_file:
        data = csv.reader(input_file, delimiter=',')
        # For each row in the csv, store it as a list inside a list and
        # change the string value of number of students to an integer
        for row in data:
            row[2] = int(row[2])
            subject_data.append(row)

    input_file.close()

    return subject_data


main()
