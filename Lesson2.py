#I learrned how to write string commands in
# two different ways, they are useful in different contexts


bolts = 9
nuts = 7

sentence = "The result of {x} + {y} = {z}".format(
    x=bolts,
    y=nuts,
    z=bolts+nuts,
)
print(sentence)

sentence2 = f"The result of {bolts} + {nuts} = {bolts+nuts}"
print(sentence2)


