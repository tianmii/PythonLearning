for i in range(3):
    print("hello JoJo!")

# print()
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# guess = input("pick a number 1 - 10: ")
# if guess in numbers:
#     print("You won!")
# else:
#     print("You lose.")

"""
Data Type - Dictionary

Dictionaries rules:
Strings can be a dict key
Tuple can be a dict key
List cannot be a dict key
Dictionary cannot be a dict key
"""
print()
gon_dict = {
    "Name": "Gon Freecs",
    "Address": "Whale Island",
    "Business": "Hunter"
}

print(gon_dict)
print()

print(gon_dict["Name"])
print(gon_dict["Address"])
print(gon_dict["Business"])
print()

# Dictionaries are mutable (keys are immutable)
# Adding new key-value pairs
gon_dict["City"] = "Yorknew"
print(gon_dict["City"])
# Using the "in" keyword to see if key is in a dict
print("Name" in gon_dict)
print(gon_dict)

# Empty Dictionary
hunter_dict = {}
hunter_dict["1st hunter"] = "gon"
hunter_dict["2nd hunter"] = "kurapika"
print(hunter_dict)

"""
Dictionary Methods:
- keys() method
- values() method
- items() method
also, pop(), copy(), clear(), but less used 
"""
# methods for the object, in this case:
# key method is hunter_dict.keys by adding a "." after the object "hunter_dict"
print()
print(hunter_dict.keys())
print(gon_dict.keys())

# value method
print(gon_dict.values())
print()
# tuple in item method
print(gon_dict.items())

"""
Data Type - Tuples
Tuples are containers that stores objects in specific ways
Tuples are immutable, containers cannot change
Items in a tuple cannot be modified, added to, or have items removed
Useful for values that never change: geographic coordinates of a city
Tuples can be used as keys for dictionaries
"""
print()
# notice it's not using [], where the objects are mutable
dallas_coordinates = ("N 32.794", "W -96.765")
print(dallas_coordinates)
# prints without the (' ')
print(dallas_coordinates[0])
# True or False
print("N 32.794" in dallas_coordinates)
print("N 32.794" not in dallas_coordinates)
print()
# slicing
print(dallas_coordinates[0:])
print(dallas_coordinates[:1])
print(dallas_coordinates[1:2])

# TypeError: 'tuple' object does not support item assignment
# dallas_coordinates[0] = "N 29.206"
# print(dallas_coordinates)
print()
one_value_tuple = (23,)
print(one_value_tuple)
