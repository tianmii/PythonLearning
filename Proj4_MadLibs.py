madlib = "{}! He said {} as he jumped into his convertible {} and drove off with his {} uncle."

blanks = [
    "exclamation",
    "adverb",
    "noun",
   "adjective",
]

print("\nMad Libs the game! Fill in the blanks.")

answers = []
for blank in blanks:
    ans = ""
    while not ans:
        ans = input(f"\n{blank}: ")
        if not ans:
            print("Don't leave it blank!")
    answers.append(ans)
print(madlib.format(*answers))
