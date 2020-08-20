"""
CP1404/CP5632 - Practical
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

# get user input
sales = float(input("Enter sales: $"))

# while loop for error checking
while sales >= 0:
    # check which category the sales fits into
    if sales < 1000:
        sales_bonus = sales * .1
    else:
        sales_bonus = sales * .15
    # print and get user input again
    print("Your sales bonus is ${:.2f}".format(sales_bonus))
    sales = float(input("Enter sales: $ "))

print("Thank you for using the sales bonus calculator.")