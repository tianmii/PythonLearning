# List comprehension
# Collapsing longer code into a more compact style

### Version 1 ###
# empty list to hold all numbers
squares = []
# Go through first 10 numbers, square, and add to list
for number in range(1, 11):
    squares.append(number ** 2)
# show that our list is correct
for square in squares:
    print(square)

# ------- Version 2 ---------
# Collapse 3 lines of code into 1
# Store the first 10 square numbers into a list
squares = [number ** 2 for number in range(1, 11)]
# Show that our list is correct
for square in squares:
    print(square)

games = ['horizon', 'witcher', 'skyrim']
great_games = []
for game in games:
    great_games.append(game.title())

    # for great_games


def transform(x):
    if not x % 2:
        return x * 3

    return None


print()
y = list(range(10))

print([
    transform(x)
    for x in y
    if transform(x) is not None
])

z = []
for x in y:
    t = transform(x)
    if t is not None:
        z.append(t)
print(z)

# ------------List comprehension-----------
# empty list that will hold square number
squares = []
# Go through first 9 numbers, square them,
# and add them to list
for numba in range(1, 10):
    new_squr = numba ** 2
    squares.append(new_squr)
    # Show list is correct
    for squr in squares:
        print(squr)

# -----------Collapse first 3 lines---------------
# Store first 9 squares in a list
# CAN BE TRANSLATED AS:
# squares = [raise numba to the second power,
# for each numba in the range 1-10]
squares = [numba ** 2 for numba in range(1, 10)]
# Show list is correct
for squr in squares:
    print(squr)

evens = []
for numba in range(1, 9):
    evens.append(numba * 2)
for even in evens:
    print(even)

tiger_mom = ['ocelot', 'leopard', 'lynx']
MAAA = [
    "{} the bad!".format(tiger.title())
    for tiger in tiger_mom
]

for x in MAAA:
    print("Hi, {}".format(x))
