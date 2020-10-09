"""
CP1404/CP5632 Practical - Christian Torrisi
Intermediate - Taxi class
"""

from random import randint
from prac_08.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that that may be unreliable to drive."""

    def __init__(self, name, fuel, reliability):
        """Initialise a Unreliable Car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive a certain distance, or don't drive, based on the reliability"""
        if randint(0, 100) >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)

        return distance_driven
