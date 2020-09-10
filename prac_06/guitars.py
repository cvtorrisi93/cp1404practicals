"""
CP1404/CP5632 Practical - Christian Torrisi
Do-from-Scratch - Guitars! - Play!.
"""

from prac_06.guitar import Guitar


def main():
    """'Play' Guitars program"""

    print("My Guitars!")

    guitars = []
    # name = input("Name: ")
    # while name != "":
    #     year = int(input("Year: "))
    #     cost = float(input("Cost: "))
    #     guitar = Guitar(name, year, cost)
    #     guitars.append(guitar)
    #     print("{} added.".format(guitar))
    #     name = input("Name: ")

    guitars.append(Guitar("Fender Stratocaster", 2014, 765.4))
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        print("Guitar {}: {} ({}), worth ${:.2f} {}".format(i, guitar.name, guitar.year, guitar.cost, vintage_string))


main()
