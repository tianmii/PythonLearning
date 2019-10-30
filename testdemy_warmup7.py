
"""
print()
"""
"""
OOP

Why?
- Reuse code (reduces amount of time developing and maintaining code
- Modular code (break problems into smaller problems

Classes - blueprint for the house
"""

# initialize your class in python and the attributes
class Computers:
    # instance variables or attributes "name, color, os, etc"
    def __init__(self, name, color, os):
        self.name = name
        self.color = color
        self.os = os
    # method
    def start(self):
        print(f"Starting my {self.name} Computer")

# inheritance from parent computer class of all
# objects, attributes, methods
# parent class also called super class
class Tablet(Computers):
    def __init__(self):
        # must add this attribute method with parameter with 4 required arguments
        Computers.__init__(self, name="iPad Pro", color="grey", os="iOs")
        print("This is Tablet class")
    def download_app(self):
        print(f"{self.os} is now downloading new apps.")


tablet_comp = Tablet()


apple = Computers(
    "Macbook Pro",
    "Space Gray",
    "iOS"
)
microsoft = Computers(
    "Surface Pro",
    "Silver",
    "Windows"
)


apple.start()
print(apple.name)
print(apple.color)
microsoft.start()
print(microsoft.name)
print(microsoft.color)
tablet_comp.start()
tablet_comp.download_app()
