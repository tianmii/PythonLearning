# Terminal app

import os
from typing import List

def display_title_bar():
    os.system('cls')
    print("\t----------------------------------------------------------")
    print("\t-------------Welcome to your Steam Wishlist---------------")
    print("\t----------------------------------------------------------")


def get_user_choice():
    print('\n[1] The current wishlist.')
    print('[2] Please enter a new game you would like to add.')
    print('[q] Exit the Wishlist')
#Forgot to add a return/got confused at line 43
    return input("\nWhat would you like to do? ")

# WHEN THERE ARE VARIABLES, pass in the data in the () or else it won't be able to run independently
# Need to be clear and [not make it globals ()]
# games: List[str] is so that games is clear what it is. Do not see it until main program
def show_games(games: List[str]):
    print("\nHere is the current list:")
    for game in games:
        print(game.title())

def get_new_game(games: List[str]):
    new_game = input("\nWhat new addition would you like to add: ")
    if new_game in games:
        print("\n{old} is already in the list.".format(old=new_game.title()))
    else:
        games.append(new_game)
        print("{new} has been added.".format(new=new_game.title()))




#################

games = []

choice = ''
display_title_bar()
while choice != 'q':

    choice = get_user_choice()

    display_title_bar()
    if choice == '1':
        show_games(games)
    elif choice == '2':
        get_new_game(games)
    elif choice == 'q':
        print("\nThank you for shopping on Steam.")
    else:
        print("\nPlease try a different input.\n")