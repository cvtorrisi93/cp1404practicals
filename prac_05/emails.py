"""
CP1404/CP5632 Practical - Christian Torrisi
Do-from-scratch - Gets a users emails and names and stores them in a dictionary
"""


def main():

    email_to_name = {}
    email = input("What is your email address?\n>>> ")

    while email != "":
        email_to_name[email] = get_name(email)
        check_name = input("Is your name {}? (Y/n) ".format(email_to_name[email])).upper()
        if check_name == "Y" or check_name == "":
            email = input("What is your email address?\n>>> ")
        else:
            email_to_name[email] = input("Name: ")
            email = input("What is your email address?\n>>> ")

    for email, name in email_to_name.items():
        print("{} ({})".format(name, email))


def get_name(email):
    parts = email.split("@")[0].split(".")
    name = " ".join(parts).title()
    return name


main()