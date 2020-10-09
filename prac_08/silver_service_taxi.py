"""
CP1404/CP5632 Practical - Christian Torrisi
Intermediate - Silver Service Taxi (SST) class
"""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that has fanciness"""
    flagfall = 4.50

    def __int__(self, name, fuel, fanciness):
        """Initialise a SST instance, based on parent class Taxi"""
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness

