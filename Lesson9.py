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
    print(f"- {color}")

# Str numbers
numba = 13
print(f"My favorite numba is {str(numba)}.")
print()
# Gymast score
score = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
print(f"The lowest possible score is {score[0]}, and the highest possible score is {score[-1]}")

print()
for numbas in score:
    print(f"A judge can give a gymnast {numbas} points.")

# -------------- Gymnast score -----------------
# if else version so the sentence has correct grammar
score = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
print(f"The lowest possible score is {score[0]}, and the highest possible score is {score[-1]}")
for numbas in score:
    if numbas == '1':
        print(f"A judge can give a gymnast {numbas} point.")
    else:
        print(f"A judge can give a gymnast {numbas} points.")
