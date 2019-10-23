# Addition calculator
# 2 numbers adds them, print out a sentence showing 2 numbers
# call function with three times, with a different name each time


# def numbers1(args):
#     pass
#
#
# def add2nums_print(message, numbers_int1, numbers_int2):
#     print(message.format(numsum=sum(numbers1)))
#     print(message.format(numsum=sum(numbers2)))
#
#
# numbers = [2.5, 3, 4, 6, 7.5]
# numbers2 = [2, 4, 8, 7, 23]
# add2nums_print(f"The sum is {numsum}.", numbers, numbers2)


def sum_num(x, y):
    print(f"{x} + {y} = {x + y}")


sum_num(4, 6)
sum_num(5, 7)

# Testing with vim
# If statements
print()
desserts = ['waffles', 'donuts', 'speculoos', 'mochi']
fav_dessert = 'speculoos'

for dessert in desserts:
    if dessert == fav_dessert:
        print(f"{dessert.title()} is my favorite dessert!")
    else:
        print(f"I like {dessert.title()} dessert.")

print()
games = ['planet robobot', 'pokemon x', 'link between worlds']
fav_game = 'link between worlds'
for game in games:
    if game == fav_game:
        print(f"{game.title()} is my favorite game!")
    else:
        print(f"{game.title()} is a good game.")

# Simple if statements with len()
print()
cats = ['tomo', 'ryuka', 'scuba', 'maru']

if len(cats) > 3:
    print("Wow, that's a lot of cats!")

# if else
print()
icecreams = ['cinnamon', 'mint', 'hazelnut', 'pistachio']

if len(icecreams) > 5:
    print("Wow that's a lot of flavors!")
else:
    print("Okay that's a reasonable amount of flavors.")

flavors = ['cinnamon', 'milk', 'black sesame', 'cinnamon', 'hazelnut']

if len(flavors) >= 5:
    print("You can start an icecream shoppe!")
elif len(flavors) >= 3:
    print("Wow, lots of flavors!")
else:
    print("Okay, that's not too many flavors.")

stranger = ["el", "mike", "will", "dustin", "lucas", "max"]

if len(stranger) >= 5:
    print("There are way too many characters now.")
elif len(stranger) >= 2:
    print("That's not a lot of buddies.")
else:
    print("Okay that's an okay amount of characters.")

stranger = ["el", "mike"]

if len(stranger) >= 5:
    print("There are way too many characters now.")
elif len(stranger) >= 1:
    print("That's an okay amount of characters.")
else:
    print("There's not a lot of buddies.")

print()
# True & False values
# Any non-zero or non-empty value is TRUE
if 0:
    print("It's true.")
else:
    print("It's false.")

# Negative numbers are not zero
if -193:
    print("It's true.")
else:
    print("It's false.")

# Empty string evaluates as false
if '':
    print("It's true.")
else:
    print("It's false.")

# Any other string including a space is true
if ' ':
    print("It's true.")
else:
    print("It's false.")

# None is special object in python, evaluates as false
if None:
    print("It's true.")
else:
    print("It's false.")

#
print()
horizon = ["aloy", "rost", "sylens"]
donezo = False
while not donezo:
    new_horizon = input("People in Gaia database:")
    if new_horizon == "link":
        donezo = True
    else:
        horizon.append(new_horizon)
        print(horizon)
