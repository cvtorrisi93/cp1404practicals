"""
CP1404/CP5632 Practical - Christian Torrisi
Do-from-Scratch - Guitars! - Test!.
"""

from prac_06.guitar import Guitar


def main():
    gibson_l5_ces = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 10000.009)

    print("{} get_age() - Expected 98. Got {}".format(gibson_l5_ces.name, gibson_l5_ces.get_age()))
    print("{} get_age() - Expected 7. Got {}".format(another_guitar.name, another_guitar.get_age()))
    print("{} is_vintage() - Expected True. Got {}".format(gibson_l5_ces.name, gibson_l5_ces.is_vintage()))
    print("{} is_vintage() - Expected False. Got {}".format(another_guitar.name, another_guitar.is_vintage()))


main()
