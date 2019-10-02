import os


# Greeter is a terminal application that lists the characters
#   and remembers fighters.


# FUNCTIONS

def display_title_bar():
    # Clears the terminal screen, and displays a title bar.
    os.system('cls')

    print("\t*****************************************************")
    print("\t***  SUPER SMASH BROTHERS - Choose your fighter!  ***")
    print("\t*****************************************************")


def get_user_choice():
    # Let users know what they can do.
    print("\n[1] Here are the unlocked fighters.")
    print("[2] Unlock a new character.")
    print("[q] Quit.")

    return input("What would you like to do? ")


def show_names():
    # Shows the names of everyone on the list
    print("\nHere are the current fighters:\n")
    for name in names:
        print(name.title())


def get_new_name():
    # Asks the user for a new name and stores the name.
    new_name = input("\nA new foe has appeared: ")
    names.append(new_name)
    print(f"\n{new_name.title()} has joined the battle!\n")


# MAIN PROGRAM

# Set up a loop where users can choose what they'd like to do.
names = []

choice = ''
display_title_bar()
while choice != 'q':

    choice = get_user_choice()

    # Respond to the user's choice.
    display_title_bar()
    if choice == '1':
        show_names()
    elif choice == '2':
        get_new_name()
    elif choice == 'q':
        print("\nThanks for playing.")
    else:
        print("\nI didn't understand that choice.\n")
