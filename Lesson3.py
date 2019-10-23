# Lists
# I learned how to organize lists, Gabe taught me that
# print("It's me, " + A.title() + "!")  can easily cause errors
# because of having to remember to add spaces in between quotations
# and plus signs are weird to have in a sentence

As = ['ryan', 'k8', 'tomo', 'ryuka']

for A in As:
    print(f"It's me {A.title()}!")

    As = ['ryan', 'k8', 'tomo', 'ryuka']

families = ['ryan', 'k8', 'ryuka', 'tomo']
family = families[0]
print(family.upper())

families = ['ryan', 'k8', 'ryuka', 'tomo']
family = families[1]
print(family.title())

families = ['ryan', 'k8', 'ryuka', 'tomo']
family = families[-2]
print(family.title())

values = ['python', 'c', 'java']
value = values[0]
print(value.lower())

values = ['python', 'c', 'java']
value = values[1]
print(value.lower())

values = ['python', 'c', 'java']
value = values[2]
print(value.lower())

# tiresome way to write a sentence
values = ['python', 'c', 'java']
for value in values:
    print(f"A nice programming language is {value.lower()}.")

values = ['python', 'c', 'java']
value = values[1]
print(f"One item on my list is {value.lower()}.")

cats = ['ryuka', 'tomo', 'guppy', 'tammy']
for cat in cats:
    print(cat)

cats = ['ryuka', 'tomo', 'guppy', 'tammy']
for cat in cats:
    print(f"I like {cat.title()}.")

cats = ['british shorthair', 'domestic shorthair']
for cat in cats:
    print(f"\nI like {cat}s!")
    print(f"No, I really really like {cat}s!")

print("\nThat's just how I feel about cats.")

# DO THIS INSTEAD
# best way to avoid errors, you're typing the sentence as you
# normally would

bs = 'british shorthairs'
ds = 'domestic shorthairs'
rag = 'ragdolls'
sentence = f"I really like {bs}, {ds}, and {rag}"
print(sentence)

# Exercises
# First List
# Store the values 'python', 'c', and 'java' in a list.
# Print each of these values out, using their position in the list.
cats = ['ryuka', 'tomo', 'guppy']
a = cats[0]
b = cats[1]
c = cats[2]
print("\n")
print(a, b, c)

# First Neat List
# Store the values 'python', 'c', and 'java' in a list.
# Print a statement about each of these values, using their position in the list.
# Your statement could simply be, 'A nice programming language is value.'

game = 'zelda'
sentence = f"\nI like the game {game}"

print(sentence)

games = ['zelda', 'pokemon', 'kirby']
for word in games:
    print('I like the game {}, {}'.format(
        word, 1
    ))

# for word in games:
for word in ['zelda', 'pokemon', 'kirby']:
    print(f"I like the game {word.lower()}")

# messed up version
# for word in enumerate(['zelda', 'pokemon', 'kirby']):
# print('I like the game {a}'.format(
#     a = word.lower()
# ))

for idx, word in enumerate(['zelda', 'pokemon', 'kirby']):
    print(f"{idx}. I like the game {word}")

for idx, word in enumerate(['zelda', 'pokemon', 'kirby'], start=15):
    print(f"{idx}. I like the game {word}")

print()
for tup in enumerate(['zelda', 'pokemon', 'kirby']):
    print(tup)
    idx = tup[0]
    word = tup[1]
    print(f"{idx}. I like the game {word}")
print()

for idx, word, *_ in [('zelda', 5, 12), ('pokemon', 9, 14, 80, 100, 3333), ('kirby', 100, 200, 300)]:
    print(f"{idx}. I like the game {word}.")

