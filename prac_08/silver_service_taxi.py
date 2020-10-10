"""
CP1404/CP5632 Practical - Christian Torrisi
Intermediate - Silver Service Taxi (SST) class
"""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that has fanciness"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SST instance, based on parent class Taxi"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string like a Taxi but with the flagfall cost included."""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Return the price for the Silver Service Taxi trip."""
        # return (self.price_per_km * self.current_fare_distance) + self.flagfall
        # More efficient solution below
        return self.flagfall + super().get_fare()
