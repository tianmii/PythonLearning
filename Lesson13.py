# while loops to keep program running
games = []
new_game = ''

### 'a != b' is the same as 'not a==b'
# takes left side and right side and evaulates as True is NOT EQUAL / False if EQUAL
while new_game != 'quit':
    new_game = input("Please tell me a game I should know, or enter 'quit': ")

    if new_game !='quit':
        games.append(new_game)
print(games)