#Terminal Apps
# Greeter



###### FUNCTION
# Repeated code, introducing a function instead of writing it again in for name in name
def display_title_bar():
    # Clear screen before listing names

    print("\t*******************************************")
    print("\t*** Greeter - Hello old and new friends!***")
    print("\t*******************************************")

def get_user_choice():
    #Let users know what they can do
    print("\n[1] See a list of characters.")
    print("[2] Tell me about someone new.")
    print("[q] Quit.")

    return input("What would you like to do? ")

def show_names():
        print("\nHere are the characters I know.\n")
        for name in names:
            print(name.title())
def get_new_name():
        new_name = input("\nPlease tell me this person's name: ")
        names.append(new_name)
        print("\nI can't wait to meet {new}!\n".format(new=new_name.title()))
#### MAIN PROGRAM

# Set up loop where users can choose what they'd like to do
names = []
choice = ''
##### add this call to the function
display_title_bar()

# != means not equal to
while choice != 'q':
    display_title_bar()

    choice = get_user_choice()

    # Respond to user's choice
    # Call to the function again or nothing happens
    display_title_bar()

    if choice == '1':
        show_names()
    elif choice == '2':
        get_new_name()
    elif choice == 'q':
        print("\nThanks for playing. Bye.\n")
    else:
        print("\nI didn't understand that choice.\n")