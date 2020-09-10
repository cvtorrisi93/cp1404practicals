"""
CP1404/CP5632 Practical - Christian Torrisi
Do-from-Scratch - Guitars!.
"""

CURRENT_YEAR = 2020


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance.

        name: string, name of the guitar
        year: int, the year the guitar was released
        cost: float, the cost of the guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Returns a string output for the Guitar object"""
        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Gets the age of the guitar from the current year"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= 50
