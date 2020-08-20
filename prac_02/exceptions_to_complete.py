"""
CP1404/CP5632 - Practical - Christian Torrisi
Exceptions To Complete
"""

finished = False
result = 0
while not finished:
    try:
        # get input, if valid then exit loop
        result = int(input("Please enter the result: "))
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)