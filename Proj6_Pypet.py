# Pypet
# Tamogotchi like game

print("Welcome to Pypet")

# string, has ""
# name = "JoJo"
# # integer b/c whole number, no ""
# age = 1
# # float b/c decimals, no ""
# weight = 4.1
# # Boolean, no ""
# hungry = True
# # string
# photo = "(ㅇㅅㅇ)"

# concatenated or linked together string and variable
# print(f"\nHello {name}")
# print(photo)

# dictionaries
# tell to store different variables that have different values
# each lines contains a cattribute
# attribute has key (name, weight, etc)
# attribute has value (JoJo, True, 4.1, etc)

cat = {
    'name': 'JoJo',
    'hungry': True,
    'weight': 4.1,
    'age': 1,
    'photo': '(ㅇㅅㅇ)'
}


# function is a block of reusable code to perform a single action
# "hungry" attribute is set to False when no longer hungry
def feed(pet):
    if pet['hungry']:
        pet['hungry'] = False
        pet['weight'] = pet['weight'] + 1
        print(f"\nYou fed {cat['name']}")
    else:
        print(f"\n{cat['name']} is not hungry")


print(f"\nHello {cat['name']}")
print(f"{cat['photo']}")
feed(cat)
print(f"\n{cat}")

# if pypet is not hungry, take into account the hungry variable
# is set to True or False with if statement
# if pypet is hungry, program will set hungry variable to False
# and increase weight
