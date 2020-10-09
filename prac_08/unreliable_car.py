"""
CP1404/CP5632 Practical - Christian Torrisi
Walkthrough - Taxi class
"""

from random import randint
from prac_08.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that that may be unreliable to drive."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        number = randint(0, 100)
        if number < self.reliability:
            distance_driven = super().drive(distance)
            print(number, " ", distance_driven)
        else:
            distance_driven = super().drive(0)
            print(number, " ", distance_driven)

        return distance_driven
