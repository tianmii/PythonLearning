# removing items by position

games = ['isaac', 'stardew valley', 'pokemon', 'kirby']
del games[1]
print(games)

#
games = ['torchlight', 'diablo', 'pokemon', 'fable']
games.remove('fable')
print(games)

games = ['torchlight', 'diablo', 'pokemon', 'fable', 'diablo']


def remove(value: str, items: list):
    for idx, item in enumerate(items):
        if item == value:
            del items[idx]
            return


############################################################
# x = filter(lambda x: x != 'diablo', games)
# gabe's fancy rewriting from scratch
x = [
    game for game in games
    if game != 'diablo'
]

y = []
for game in games:
    if game != 'diablo':
        y.append(game)

games.pop()

# remove("diablo", games)
print(games)
print(x)

##############################################
pokemon = ['gastly', 'lapras', 'jolteon']
first_pokemon = pokemon.pop(0)

print(first_pokemon)
print(pokemon)

# Famous people list
celebrity = ['nl', 'beartaffy', 'rocklee', 'josh']

last = celebrity.pop()

celebrity.remove('beartaffy')
del celebrity[1]

print("There are no famous people in my list.")
print(celebrity)

# slicing a list
nlss = ['nl', 'rocklee', 'josh', 'baer', 'pbg']
first_batch = nlss[0:4]
for nlss_one in first_batch:
    print(nlss_one.title())

# copied list
avengers = ['ironman', 'thor', 'captain', 'hulk', 'geralt', 'ciri']
copied_avengers = avengers[:]
print("the copied list:\n\t", copied_avengers)

# Remove first two users from copied list
del copied_avengers[4]
del copied_avengers[4]
print("\nTwo non-Avengers removed from copied list:\n\t", copied_avengers)

# The original list unaffected
print("\nThe original list:\n\t", avengers)

# Pokemon Unown
unown = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
first_group = unown[0:4]
for item in first_group:
    print(item)
middle_group = unown[4:6]
for x in middle_group:
    print(x)
last_group = unown[6:]
for y in last_group:
    print(y)

# Numerical lists
numba = [1, 2, 3, 4, 5, 6]
for numba in range(1, 4):
    print(numba)

# (start, end, steps between numbers)
# odd or even in steps of 2, etc...

for numba in range(2, 14, 2):
    print(numba)

# without manually typing out list
numbas = list(range(1, 12))
print(numbas)

################
# store the first million numbers in a list
numbas = list(range(1, 1000001))
# length of list
sentence = f"The list numbas has {str(len(numbas))} numbas in it."
print(sentence)
# shows last 10 numbers
# The expression: str(len(numbers)) takes the length
# of numbers list and turns into a string that can be printed
print("\nThe last 10 numbas in the list are:")
for numba in numbas[-10:]:
    print(numba)
########################

# min, max, sum functions
ages = [13, 18, 21, 45, 69]

youngest = min(ages)
oldest = max(ages)
total_years = sum(ages)
print(f"Our youngest reader is {youngest} years old")
print(f"Our oldest reader is {oldest} years old")
print(f"Together, we have {total_years} years worth of life experience.")

# First Twenty
first_20 = list(range(1, 21))
print(first_20)

wallets = [0.5, 3, 17, 34]
skinniest = min(wallets)
fattest = max(wallets)
total = sum(wallets)

print(f"The fattest wallet has ${skinniest} in it.")
print(f"The skinniest wallet has ${fattest} in it.")
print(f"All together, these wallets have ${total} in them.")
