# 99 bottles
# List of numbers, do not manually type them in, use a built in function
# "Take one down, pass it around" but cannot manually type numbers into song
# reach one bottle left, bottles becomes bottle
# Blank line between each verse of the song


bottles = 5
while bottles > 0:
    print("{current_num} bottles of beer on the wall, {current_num} bottles of beer.".format(
        current_num=bottles
    ))
    print("Take one down pass it around")
    bottles = bottles - 1
    if bottles == 1:
        print("{current_num} bottle of beer on the wall!\n".format(current_num=bottles))
    elif bottles > 1:
        print("{current_num} bottles of beer on the wall!\n".format(current_num=bottles))
    else:
        print("No more bottles of beer on the wall!")


