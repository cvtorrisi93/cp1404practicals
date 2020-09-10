"""
CP1404/CP5632 Practical - Christian Torrisi
Practice - Person class exercise.
"""


class Person:
    """Representation of a person object"""

    def __init__(self, first_name="", last_name="", age=0):
        """
        Initialise a Person instance

        first_name: string, first name of the Person
        last_name:  string, last name of the Person
        age:        int, age of the person
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return "{} {} ({})".format(self.first_name, self.last_name, self.age)

    def is_adult(self):
        return self.age >= 18
