"""
CP1404/CP5632 Practical - Christian Torrisi
Practice - Person class exercise - List X number of people.
"""

from prac_06.person import Person
from operator import attrgetter


def main():
    """Input x number of people into a list and sort by age"""

    people = []
    number_of_people = get_valid_positive_integer("How many people will be added to the list? ")
    get_list_of_people(number_of_people, people)

    first_name_max_length = get_max_length(people, "first_name", 10)

    last_name_max_length = get_max_length(people, "last_name", 9)

    print("{:{first_name_max_length}} | {:{last_name_max_length}} | {}"
          .format("First Name", "Last Name", "Age", first_name_max_length=first_name_max_length,
                  last_name_max_length=last_name_max_length, ))

    people.sort(key=attrgetter("age"))

    for person in people:
        adult_string = "(minor)"
        if person.is_adult():
            adult_string = "(adult)"
        print(
            "{:{first_name_max_length}} | {:{last_name_max_length}} | {:>3}} {}"
                .format(person.first_name, person.last_name, person.age, adult_string,
                        first_name_max_length=first_name_max_length,
                        last_name_max_length=last_name_max_length))


def get_max_length(people, attribute, header_length):
    """Get max length of an attribute from a list of objects"""
    attributes = []
    for person in people:
        attributes.append(str(person.__getattribute__(attribute)))
    max_length = len(max(attributes, key=len))
    if max_length < header_length:
        max_length = header_length
    return max_length


def get_list_of_people(number_of_people, people):
    """Create a list of Person objects"""
    for i in range(number_of_people):
        first_name = get_valid_string("First name: ")
        last_name = get_valid_string("Last_name: ")
        age = get_valid_positive_integer("Age: ")
        person_to_add = Person(first_name, last_name, age)
        people.append(person_to_add)
        print(person_to_add, "added to the list.")
    return people


def get_valid_string(prompt):
    """Get a valid string from user (not blank)"""
    string = input(prompt)
    while string == "":
        print("Input can not be blank")
        string = input(prompt)
    return string


def get_valid_positive_integer(prompt):
    """Get a valid positive integer from user (0 not included) """
    valid_input = False
    while not valid_input:
        try:
            number = int(input(prompt))
            while number <= 0:
                print("Number must be > 0")
                number = int(input(prompt))
            valid_input = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return number


main()
