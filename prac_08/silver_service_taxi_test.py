"""
CP1404/CP5632 Practical - Christian Torrisi
Intermediate - Silver Service Taxi (SST) testing
"""

from prac_08.silver_service_taxi import SilverServiceTaxi

hummer = SilverServiceTaxi("Hummer", 200, 2)
hummer.drive(18)
print(hummer)
print("${:.2f}".format(hummer.get_fare()))