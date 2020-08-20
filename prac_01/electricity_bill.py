"""
CP1404/CP5632 - Practical
Practice - Electricity Bill Estimator
"""
# declare constants
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity Bill Estimator 2.0")

# get user input
tariff_choice = int(input("Which tariff? 11 or 31: "))

# error checking for tariff selection
while tariff_choice != 11 and tariff_choice != 31:
    print("Invalid tariff. Please choose 11 or 31: ")
    tariff_choice = int(input("Which tariff? 11 or 31: "))

# assign cents per kwh based on tariff
if tariff_choice == 11:
    cents_per_kwh = TARIFF_11
else:
    cents_per_kwh = TARIFF_31

# get user input for other variables
daily_usage_kwh = float(input("Enter daily use in kWh: "))
number_of_billing_days = int(input("Enter number of billing days: "))

# compute the estimated bill
estimated_bill = (cents_per_kwh * daily_usage_kwh * number_of_billing_days)
print("Estimated bill: ${:.2f}".format(estimated_bill))

# Version 1
# print("Electricity Bill Estimator")
# cents_per_kwh = float(input("Enter cents per kWh: "))
# daily_usage_kwh = float(input("Enter daily use in kWh: "))
# number_of_billing_days = int(input("Enter number of billing days: "))
# estimated_bill = (cents_per_kwh * daily_usage_kwh * number_of_billing_days)/100
# print("Estimated bill: ${:.2f}".format(estimated_bill))
