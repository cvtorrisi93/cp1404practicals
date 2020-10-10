"""
CP1404/CP5632 Practical - Christian Torrisi
Do-from-scratch - Taxi Simulator
"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None

    print("Let's drive")
    print(MENU)
    menu_choice = input(">>>").lower()

    while menu_choice != "q":
        if menu_choice == "c":
            show_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
        elif menu_choice == "d":
            pass



def show_taxis(taxis):
    for number, taxi in enumerate(taxis):
        print("{} - {}".format(number, taxi))


main()
