######### Pokédex #############

# formatting long dictionaries with lots of key values and pairs

import os

def display_pokedex_title():
    os.system('cls')
    print("\t-----------------------------------------------------------------------------")
    print("\t--------------I am your Pokédex, you guide to Pokémon------------------")
    print("\t-----------------------------------------------------------------------------")

def get_user_choice():
    print("\n[1] View you current pokemon")
    print("[2] Input a new pokemon")
    print("[3] Exit the Pokédex (enter 'q')")
    return input("What would you like to do? ")

def show_current_pokemon():
    print("\nHere is the current pokemon:")
    for poke in pokemon:
        print(pokemon.title())


def get_new_pokemon():
    new_pokemon=input("\nWhat new pokemon would you like to add? ")
    if new_pokemon in pokemon:
        print("{old_pokemon} is already in the list".format(old_pokemon=new_pokemon.title()))
    else:
        pokemon.append(new_pokemon)
        print("{new_pokemon} has been added to the list.".format(new_pokemon=new_pokemon.title()))

######################



pokemon = []

choice = ''
display_pokedex_title()
while choice != 'q':

    choice = get_user_choice()

    display_pokedex_title()
    if choice == '1':
        show_current_pokemon(pokemon)
    elif choice == '2':
        get_new_pokemon(pokemon)
    elif choice == 'q':
        print("\nPokedex sleepmode.")
    else:
        print("\nPlease try a different input.\n")
