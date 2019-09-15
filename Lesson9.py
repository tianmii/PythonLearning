# Tuples
# Tuples are lists that can never be changed
# Lists are dynamic; can remove/append
# Tuples use () instead of [list]
# can still use for loop

colors = ('chartreuse', 'mahogany', 'greige')
print("The foist color is: {first}".format(
    first=colors[0]
))

print("\nThe available colors are:")
for color in colors:
    print("- {all}".format(all=color))

# Str numbers
numba = 69
print("My favorite numba is {num}. ;)".format(
    num=str(numba)
))

# Gymast score
score = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
print("The lowest possible score is {low}, and the highest possible score is {high}".format(
    low=score[0],
    high=score[-1],
))
for numbas in score:
    print("A judge can give a gymnast {all} points.".format(
        all=numbas
    ))

# -------------- Gymnast score -----------------
# if else version so the sentence has correct grammar
score = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
print("The lowest possible score is {low}, and the highest possible score is {high}".format(
    low=score[0],
    high=score[-1],
))
for numbas in score:
    if numbas == '1':
        print("A judge can give a gymnast {single} point.".format(
            single=numbas
        ))
    else:
        print("A judge can give a gymnast {all} points.".format(
            all=numbas
        ))
