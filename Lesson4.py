# First Neat List
# Store the values 'python', 'c', and 'java' in a list.
# Print a statement about each of these values, using their position in the list.
# Your statement could simply be, 'A nice programming language is value.'

game = 'zelda'
sentence = f"I like the game {game}"
print()
#
games = ['zelda', 'pokemon', 'kirby']
for word in games:
    print(f"I like the game {word}, {1}")
print()
# for word in games:
for word in ['zelda', 'pokemon', 'kirby']:
    print(f'I like the game {word.lower()}')
print()
# messed up version
# for word in enumerate(['zelda', 'pokemon', 'kirby']):
# print('I like the game {a}'.format(
#     a = word.lower()
# ))


# how to loop based on enumerate function using for ___, in enumerate([strings]):
for idx, word in enumerate(['zelda', 'pokemon', 'kirby']):
    print(f'{idx}. I like the game {word}')
print()
#
for idx, word in enumerate(['zelda', 'pokemon', 'kirby'], start=12):
    print(f'{idx}. I like the game {word}')

#
print()
for tup in enumerate(['zelda', 'pokemon', 'kirby']):
    print(tup)
    idx = tup[0]
    word = tup[1]
    print(f'{idx}. I like the game {word}')
print()

#
for idx, word, *_ in [('zelda', 5, 12), ('pokemon', 9, 14, 80, 100, 3333), ('kirby', 100, 200, 300)]:
    print(f'{idx}. I like the game {word}.')
    # that=thing,

print()
# different way of writing the list {} does not have to have a word in it
# as long as the format ordering is correct
for idx, word in enumerate(['zelda', 'pokemon', 'kirby']):
    print(f"{idx}. I like the game {word}")
print()
#
for num, name in enumerate(['ciri', 'geralt', 'dandelion'], start=1):
    print(f'{num} is the ranking of {name.title()}')
print()
#
people = ['link', 'zelda', 'sidon']
print('sidon' in people)
print('ganondorf' in people)
print()
#
# people = ['link', 'sidon', 'zelda']
# people.append('epona')

# for people in enumerate(['link', 'sidon', 'zelda']):

dags = ['doge', 'shiba', 'pupper']
dags.append('moonmoon')
for dag in dags:
    print(f"{dag.title()}s are cool.")
print()
#



# insert
people = ['bayonetta', 'ciri', 'zelda']
people.insert(1, 'aloy')
print(people)
print()
######
# Defining an empty list

neopetusers = []

neopetusers.append('kristin')
neopetusers.append('jenna')
neopetusers.append('yolanda')

for username in neopetusers:
    print(f'Welcome to Neopets, {username.title()}!')
print()
# Some errors, but i figured out most of .format!
# I forgot the last parentheses in line 137, was ")" originally
# Spelled as "usermame".....

pokemons = ['gengar', 'jigglypuff', 'lapras', 'bulbasaur', 'alakazam', 'jolteon']
pokemons.sort()
for pokemon in pokemons:
    print(pokemon.title())
print()

pokemans = ['charizard', 'squirtle', 'skitty']
print(sorted(pokemans))
print(pokemans)
for pokeman in sorted(pokemans):
    print(pokeman.title())
print()

# length of a list
horizon = ['aloy', 'rost', 'sylens', 'nora']
horizon_count = len(horizon)
print(horizon_count)
