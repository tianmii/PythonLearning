# -------------LOOPING through ALL KEYS in DICTIONARY----------------------


def show_horse_encyclopedia():
    # SHOW USERS WHAT IS IN DICTIONARY
    print("The following awesome horses in games listed:")
    for horse in horse_encyclopedia:
        print("- {horse_name}".format(horse_name=horse))


horse_encyclopedia = {'Epona': "Link's trusty horse that will always be his steed until the end of time.",
                      'Eoach': "Geralt's go to name for every horse that he ever named; a good horst.",
                      'Shadowmere': "An undead horse the champion of Skyrim can ride and will respawn.",
                      }

# SHOW USERS WHAT IS IN DICTIONARY


# ALLOW USERS TO INPUT MORE THAT ONE HORST#
requested_horse = ''
while requested_horse != 'quit':
    # Allow user to choose a word, and then display
    # meaning for that word
    requested_horse = input("\nWhich horse would you like to know about? (or quit) ")
    # if statement and calling on .keys(): function
    if requested_horse in horse_encyclopedia.keys():
        print("\n{horse_name}: {horse_descrip}".format(
            horse_name=requested_horse,
            horse_descrip=horse_encyclopedia[requested_horse]
        ))
    elif requested_horse != 'quit':
        # Handles misspelling, words not stored
        # This is not in horse_encyclopedia, and it's not 'quit'
        print("\n Sorry, I don't know that horst.")
    else:
        print("\n Bye!")
