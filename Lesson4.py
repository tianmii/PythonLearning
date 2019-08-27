# First Neat List
# Store the values 'python', 'c', and 'java' in a list.
# Print a statement about each of these values, using their position in the list.
# Your statement could simply be, 'A nice programming language is value.'

game = 'zelda'
sentence = "I like the game {a}".format(
    a=game,
)

#
games = ['zelda', 'pokemon', 'kirby']
for word in games:
    print('I like the game {}, {}'.format(
        word, 1
    ))

# for word in games:
for word in ['zelda', 'pokemon', 'kirby']:
    print('I like the game {a}'.format(
        a=word.lower()
    ))

# messed up version
# for word in enumerate(['zelda', 'pokemon', 'kirby']):
# print('I like the game {a}'.format(
#     a = word.lower()
# ))


# how to loop based on enumerate function using for ___, in enumerate([strings]):
for idx, word in enumerate(['zelda', 'pokemon', 'kirby']):
    print('{number}. I like the game {a}'.format(
        a=word,
        number=idx
    ))

#
for idx, word in enumerate(['zelda', 'pokemon', 'kirby'], start=69):
    print('{number}. I like the game {a}'.format(
        a=word,
        number=idx
    ))

#
print()
for tup in enumerate(['zelda', 'pokemon', 'kirby']):
    print(tup)
    idx = tup[0]
    word = tup[1]
    print('{number}. I like the game {a}'.format(
        a=word,
        number=idx
    ))
print()

#
for idx, word, *_ in [('zelda', 5, 12), ('pokemon', 9, 14, 80, 100, 3333), ('kirby', 100, 200, 300)]:
    print('{number}. I like the game {a}.'.format(
        a=word,
        number=idx,
        # that=thing,
    ))

# different way of writing the list {} does not have to have a word in it
# as long as the format ordering is correct
for idx, word in enumerate(['zelda', 'pokemon', 'kirby']):
    print('{}. I like the game {}'.format(
        idx, word
    ))

#
for x, y in enumerate(['ciri', 'geralt', 'dandelion'], start=1):
    print('{} is the ranking of {}'.format(
        x, y.title()
    ))

#
people = ['link', 'zelda', 'sidon']
print('sidon' in people)
print('ganondorf' in people)

#
# people = ['link', 'sidon', 'zelda']
# people.append('epona')

# for people in enumerate(['link', 'sidon', 'zelda']):

dags = ['doge', 'shiba', 'pupper']
dags.append('gabe')
for dag in dags:
    print(dag.title() + "s are cool.")

####################################
####old example in lesson 3
for word in ['zelda', 'pokemon', 'kirby']:
    print('I like the game {a}'.format(
        a=word.lower()
    ))

game = 'zelda'
sentence = "I like the game {a}".format(
    a=game,
)

games = ['zelda', 'pokemon', 'kirby']
for word in games:
    print('I like the game {}, {}'.format(
        word, 1
    ))
#####################################
#####################################

# insert
people = ['bayonetta', 'ciri', 'zelda']
people.insert(1, 'aloy')
print(people)

######
# Defining an empty list

neopetusers = []

neopetusers.append('tammy')
neopetusers.append('gabe')
neopetusers.append('uma')

for username in neopetusers:
    print('Welcome to Neopets, {a}!'.format(
        a=username.title()
    ))

    # Some errors, but i figured out most of .format!
    # I forgot the last parentheses in line 137, was ")" originally
    # Spelled as "usermame".....

pokemons = ['gengar', 'jigglypuff', 'lapras', 'bulbasaur', 'alakazam', 'jolteon']
pokemons.sort()
for pokemon in pokemons:
    print(pokemon.title())

pokemans = ['garbagio', 'eggboi', 'mathis']
print(sorted(pokemans))
print(pokemans)
for pokeman in sorted(pokemans):
    print(pokeman.title())

# length of a list
horizon = ['aloy', 'rost', 'sylens', 'nora']
horizon_count = len(horizon)
print(horizon_count)
