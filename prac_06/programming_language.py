"""
CP1404/CP5632 Practical - Christian Torrisi
Intermediate Exercise - Programming Language
"""


class ProgrammingLanguage:
    """Representation of a programming language object"""

    def __int__(self, name="", typing="", reflection=False, year=0):
        """Initialise a programming language instance

        name: string, name of the programming language
        typing: string, static or dynamic typing
        reflection: boolean
        year: int, year the programming language was first released
        """

        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        is_dynamic = False
        if self.typing:
            is_dynamic = True

        return is_dynamic
