"""
CP1404/CP5632 - Practical
Loops
"""

# 3.
# loops through odd numbers from 1 to 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a)
# loops through numbers from 0 to 100 in tens
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b)
# loops through each number from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# get user input
stars = int(input("Number of stars: "))
# loops through the input number and displays that number of stars in a row
for i in range(stars):
    print("*", end="")
print()

# d)
# get user input
stars = int(input("Number of stars: "))
# loops through the input number and displays the lops number of stars on each row
for i in range(1, stars +1):
    print("*" * i)

# Personal note: start at 1 so that there isn't an empty row at the top
