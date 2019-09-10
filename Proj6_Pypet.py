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
    "name": "JoJo",
    "hungry": True,
    "weight": 4.1,
    "age": 1,
    "photo": "(ㅇㅅㅇ)"
}

print("\n")
print("Hello {cat_name}".format(cat_name=cat["name"]))
print(cat["photo"])
print(cat)


# function is a block of reusable code to perform a single action
# "hungry" attribute is set to False when no longer hungry
def feed(pet):
    pet["hungry"] = False
    pet["weight"] = pet["weight"] + 1


feed(cat)
print("\nYou fed {cat_name}".format(cat_name=cat["name"]))
print(cat)


