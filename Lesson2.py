#I learrned how to write string commands in
# two different ways, they are useful in different contexts


butt = 9
nutts = 7

sentence = "The result of {x} + {y} = {z}".format(
    x=butt,
    y=nutts,
    z=butt+nutts,
)
print(sentence)

sentence2 = f"The result of {butt} + {nutts} = {butt+nutts}"
print(sentence2)

#Gebs is the best, but is also buttz and deez nuttz

