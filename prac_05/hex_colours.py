"""
CP1404/CP5632 Practical - Christian Torrisi
Hex Colours - Look up the hex code of a particular colour
"""

COLOUR_TO_HEX = {"aliceblue": "#f0f8ff", "blue1": "#0000ff", "blue2": "#0000ee", "blue4": "#00008b",
                 "blueviolet": "#8a2be2", "cadetblue": "#5f9ea0", "cadetblue1": " #98f5ff", "cadetblue2": "#8ee5ee",
                 "cadetblue3": "#7ac5cd", "cadetblue4": "#53868b"}

colour_name = input("Please enter a colour: ").lower()

while colour_name != "":
    if colour_name in COLOUR_TO_HEX:
        print("{} is {}".format(colour_name, COLOUR_TO_HEX[colour_name]))
    else:
        print("invalid colour name")
    colour_name = input("Please enter a colour: ").lower()

