# pokemon center computer

print("\nThank you for choosing the Pokemon Center system. Please look through the options.")
# set initial value for choice other than quit
choice = ''
# menu will print options to user
while choice != 'q':
    print("\n[1] Enter 1 to deposit your pokemon.")
    print("[2] Enter 2 to withdraw your pokemon.")
    print("[3] Enter 3 to arrange your pokemon.")
    print("[4] Enter 4 to access your items.")
    # Ask for the user's choice
    choice = input("\nWhat would you like to do? ")
    if choice == '1':
        print("\nWhich pokemon would you like to deposit?\n")
    elif choice == '2':
        print("\nWhich pokemon would you like to withdraw?\n")
    elif choice == '3':
        print("\nWould you like to withdraw or deposit your pokemon?\n")
    elif choice == '4':
        print("\nWould you like to withdraw or deposit your items?\n")
    elif choice == 'q':
        print("\nThank you for using our systems.\n")
    else:
        print("\nPlease try another option.")
