# module_name import function_name syntax:
from Lesson22Multiplying import double, triple, quadruple

print(double(5))
print(triple(5))
print(quadruple(5))


# import module_name:
# squiggles are on import because it should always be placed a the top of the file
import Lesson22Multiplying

print("\n")
print(Lesson22Multiplying.double(10))
print(Lesson22Multiplying.triple(10))
print(Lesson22Multiplying.quadruple(10))

# import module_name as local_module_name syntax:
import Lesson22Multiplying as m

print("\n")
print(m.double(34.4))
print(m.triple(34.4))
print(m.quadruple(34.4))

# from module_name import * syntax:
from Lesson22Multiplying import *

print("\n")
print(double(3))
print(triple(3))
print(quadruple(3))


# PEP 8
# Modules need tp be on separate lines, not "import sys, os"
# import sys
# import os

# Modules should be short and lowercase, mine is too long and caps
