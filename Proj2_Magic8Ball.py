# -------- Magic 8 Ball -----------------
# Allow user to enter question, raw input
# Display in progress message "thinking"
# Create 5-20 responses, randomize it using rand int
# Allow user to ask another question or quit

import time
from random import randint

replies = ["Maybe", "Ask Again later", "You tell me", "I'm not telling", "Yes", "Nah", "Indubitably", "error"]


def user_input():
    print("\nTell me your question.\n")
    input()
    print("Thinking")
    time.sleep(3)
    random_reply = replies[randint(0, 7)]
    print(random_reply)
    end()


def end():
    print("\nDo you want to ask another question?")
    user_reply = input()
    if user_reply == "yes":
        user_input()
    else:
        print("\nSorry, try again")
        end()


print("\nWelcome to the Magic 8-Ball\n")
user_input()
