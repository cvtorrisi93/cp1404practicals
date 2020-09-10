"""
CP1404/CP5632 Practical - Christian Torrisi
Intermediate Exercise - Programming Language Class
"""


class ProgrammingLanguage:
    """Representation of a ProgrammingLanguage object"""

    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialise a ProgrammingLanguage instance

        name:       string, name of the programming language
        typing:     string, static or dynamic typing
        reflection: boolean, whether the programming language reflects or not
        year:       int, year the programming language was first released
        """

        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Returns a string output for a ProgrammingLanguage object"""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                           self.year)

    def is_dynamic(self):
        """Check if the ProgrammingLanguage instance has dynamic typing"""
        return self.typing == "Dynamic"

