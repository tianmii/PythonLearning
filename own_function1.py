
def mult():
    return 2 * 2

# Function with multiple PARAMETERS
def add(num1, num2, num3):
    return num1 + num2 + num3

"""
Calculates the Prime Number
:param num: int
:return: True or False
"""
def prime_number(num):
    count = 2

    while count < num - 1:
        if num % count ==0:
            return False
        count = count + 1

    return True
