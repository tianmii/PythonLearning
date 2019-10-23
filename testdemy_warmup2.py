"""
Fizzbuzz challenge
print from 1 - 100
if number is divisible by 3, print "fizz"
if number is divisible by 5, print "buzz"
if number is divisible by 3 & 5, print "fizzbuzz"
Bonus: Wrap it in a function

"""
# numbers = list(range(1, 11))
# print(numbers)

# == 0 will mean the remainder is 0
# fizzbuzz needs to happen first because if % 3 only is first
# you will only get Fizz on number 15
def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 ==0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

fizzbuzz()

