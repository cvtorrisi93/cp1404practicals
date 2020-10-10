"""
CP1404/CP5632 Practical - Christian Torrisi
Intermediate - Silver Service Taxi (SST) testing
"""

from prac_08.silver_service_taxi import SilverServiceTaxi

hummer = SilverServiceTaxi("Hummer", 200, 4)
hummer.drive(123)
print(hummer)
print("$", hummer.get_fare())