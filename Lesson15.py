# HOW TO JOIN STRINGS IN A LIST and
# define what I want in between the words--> " ,"
# while loop keeps asking to add to the list until you type "quit"

games = ['zelda', 'pokemon', 'kirby']
print(*games, sep=", ")
new_game = ''
while new_game != 'quit':
    new_game = input("Please add a game you like: ")
    if new_game != 'quit':
        games.append(new_game)
games_string = ', '.join(games)
print(f"We both like {games_string}.")
