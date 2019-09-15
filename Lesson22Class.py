# classes
# combing info and behavior


class Rocket:
    # get rocket stimulates a rocket ship for a game
    # _init_() method sets the values for any parameters that need to be defined when an object is first created
    # rocket class stores two pieces of info so far, can't do anything at the moment
    # (self) is a syntax to to allow you to access a variable from anywhere else in this class
    def __init__(self):
        # Each rocket has an (x,y) position
        self.x = 0
        self.y = 0

    # Need to add this so it can do something
    def move_up(self):
        # increment the y-position of the rocket
        self.y += 1


# code has not created rocket until this point
# to actually use a class create variable my_rocket, set it = to name of class Rocket(): with empty parenthesis
# access object's variables or methods, give the name of the object and use "dot notation" to access the variable/method
# y value of my_rocket, you use my_rocket.y
# To use move_up() method on my_rocket

my_rocket = Rocket()
print("Rocket altitude:", my_rocket.y)

my_rocket.move_up()
print("Rocket altitude:", my_rocket.y)

my_rocket.move_up()
print("Rocket altitude:", my_rocket.y)


# all objects are capable of the same behavior, but each object's particular action do not affect any other objects
# here we make a fleet of rockets
# DO NOT INCLUDE () for class unless it has a parent class-> class rocket(missile): so missile is the parent
# class needs to uppercase


class Ship:

    def __init__(self):
        self.x = 0
        self.y = 0

    def move_up(self):
        self.y += 1


# create a fleet of 4 rockets, store them in a list
# my_ships = []
# for x in range(0, 4):
#    new_ship = Ship()
#    my_ships.append(new_ship)

# list comprehension in one line
my_ships = [Ship() for x in range(0, 4)]

# moves 1st and 4th ship
my_ships[0].move_up()
my_ships[3].move_up
# show each ship is separate object
for ship in my_ships:
    print("Ship altitude:", ship.y)


# -------------------- LESSON TIME ---------------------------
# object oriented programming allows you to build reusable blocks of code called CLASSES
# gabe says "class Rocket(object):" is the old format Python 2, now it's included in "class Rocket:"
# CLASS is a body of code that defines the attributes and behaviors
# to accurately model something you need for your program
# ATTRIBUTE os a piece of info; variable that is part of a class
# BEHAVIOR is defined within the class. These are made up of METHODS, which are functions defined for the class
# OBJECT is a particular instance of a class. Will have certain set of values for all attributes(variables)
# in the class. You can have multiple objects for any one class

# _init_() method is a built in function that is called automatically when you create an object from your class
# this method allows to set all relevant attributes set to proper values when object is created from class,
# before object is used. This case, method initializes x and y values of Rocket/Ship to 0

# "self" keyword refers to current object that you are working with. When you are writing a class
# it lets you refer to certain attributes from any other part of the class
# basically all methods need the self object as their first argument

# METHOD is a function part of a class, it can:
# Accept positional arguments, keyword arguments, arbitrary list of argument values,
# arbitrary dictionary of arguments or any combo of these
# Each method has to accept one argument default, the value "self"
# In this example, self argument is used to access a Ship object's y-value

# -----------------------------------------------------------

class Ship:

    def _init_(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_ship(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment


ships = [Ship() for x in range(0, 3)]

ships[0].move_ship()
ships[1].move_ship(10, 10)
ships[2].move_ship(-10, 0)

for index, rocket in enumerate(ships):
    print('Ship {index}')