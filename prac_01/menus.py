"""
CP1404/CP5632 - Practical
Practice - Menus
"""

# define constant MENU
MENU = "(H)ello\n(G)oodbye\n(Q)uit"
# OR
# MENU = """(H)ello
# (G)oodbye
# (Q)uit"""

# get user input for name and menu choice
name = input("Enter name: ")
print(MENU)
choice = input(">>> ").upper()

# menu looping
while choice != "Q":
    if choice == "H":
        print("Hello ", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").upper()

print("Finished.")