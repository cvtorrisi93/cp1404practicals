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
    total_bill = 0

    print("Let's drive")
    print(MENU)
    menu_choice = input(">>>").lower()

    while menu_choice != "q":
        if menu_choice == "c":
            show_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
            print("Bill to date: ${:.2f}".format(total_bill))
        elif menu_choice == "d":
            current_taxi.start_fare()
            distance = int(input("Drive how far? "))
            current_taxi.drive(distance)
            current_bill = current_taxi.get_fare()
            total_bill += current_bill
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_bill))
            print("Bill to date: ${:.2f}".format(total_bill))
        else:
            print("Invalid choice")

        print(MENU)
        menu_choice = input(">>>").lower()

    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    show_taxis(taxis)


def show_taxis(taxis):
    """Show all taxis that are currently in the list"""
    for number, taxi in enumerate(taxis):
        print("{} - {}".format(number, taxi))


main()
