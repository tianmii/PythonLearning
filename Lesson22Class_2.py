# Classes


# ----------Class Definition Syntax-----------

# class ClassName:
#     <statement-1>
#     <statement-2>
#     <statement-3>
#     <statement-etc>


# -------------An example of class----------------
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.description = "This shape has not been described yet"
        self.author = "Nobody has claimed to make this shape yet"

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2 * self.x + 2 * self.y

    def describe(self, text):
        self.description = text

    def author_name(self, text):
        self.author = text

    def scale_size(self, scale):
        self.x = self.x * scale
        self.y = self.y * scale


# -------------Classes and functions----------------
# Classes contain functions (methods) and data

class Roach(object):
    # __init__ is a special function(method) whenever you make
    # an instance of a class. As you heard, it initializes the object
    # Here, we'll initialize the data
    def __init__(self):
        # We add some data to the (instance of the) class
        self.position = (100, 100)
        self.velocity = (0, 0)

    # we can add our own functions, when roach bounces,
    # its vertical velocity will be negated (no gravity here)
    def bounce(self):
        self.velocity = self.velocity[0] - self.velocity[1]


# now we have a ball class, how to use it?
# ----------input into terminal----------
roach1 = Roach()
print(roach1)
# <__main__.Roach object at 0x0402B3F0>
# ^not very useful

# much more useful
roach1.position = (200, 100)
print("\n")
print(roach1.position)

roach2 = Roach()
roach2.velocity = (5, 10)
print("\n")
print(roach2.velocity)
print(roach2.position)

print("\n")
print(roach1.velocity)

print("\n")
roach2.bounce()
print(roach2.velocity)


# ---------------OOP (Object-Oriented Programming)-----------------
# self represents the object of Class A as a Python 3 syntax by default
# when there are multiple functions (methods) needed to shape object
# Classes help organize the functions

# The key attribute to self (self.x) is Hello
# We now want to to add additional data to object
# method_a allows us to attach foo in the below format
class A(object):
    def __init__(self):
        self.x = 'Hello'

    def method_a(self, foo):
        print(f'{self.x} {foo}')

    def method_b(self, boo):
        # if you do not call an attribute to self in the function
        # python will literally print you the memory location of
        # the object (indecipherable to us mortals)
        # <__main__.A object at 0x042EA250>, back atcha
        print(f'{self}, {boo}')
        # Hello, back atcha
        print(f'{self.x}, {boo}')


# Not passing any argument to __init__
a = A()
print("\n")
# Pass a single argument by calling the function
a.method_a('buddy!')
b = A()
print("\n")
b.method_b('back atcha')

# -------------Class Objects----------------

# class Bag:
#     def __init__(self):
#         self.data = []
#
#     def __add__(self, x):
#         self.data.append(x)
#
#     def addtwice(self, x):
#         self.add(x)
#         self.add(x)
