"""
CP1404/CP5632 - Practical - Christian Torrisi
Files - writing, reading, opening
"""

# 1 - creates/overwrites file
write_name = input("What is your name?: ")
my_name = open("name.txt", 'w')
print(write_name, file=my_name)
my_name.close()

# 2 - reads from file
my_name = open("name.txt", 'r')
read_name = my_name.read().strip()
print("Your name is", read_name)
my_name.close()

# 3 - read first two lines and adds together
my_numbers = open("numbers.txt", 'r')
first_number = int(my_numbers.readline())
second_number = int(my_numbers.readline())
my_total = first_number + second_number
print("Total is", my_total)
my_numbers.close()

# 4 - reads all lines and adds them
my_numbers = open("numbers.txt", 'r')
file_total = 0
for line in my_numbers:
    number = int(line)
    file_total += number
print("The total of all numbers in the file is", file_total)