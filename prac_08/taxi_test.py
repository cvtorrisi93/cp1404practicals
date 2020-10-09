"""
CP1404/CP5632 Practical - Christian Torrisi
Walkthrough - Test Taxi
"""

from prac_08.taxi import Taxi

prius_01 = Taxi("Prius 1", 100, 1.23)

prius_01.drive(40)

print(prius_01)
print("Current fare is $", prius_01.get_fare())

prius_01.start_fare()

print(prius_01)
print("Current fare is $", prius_01.get_fare())
