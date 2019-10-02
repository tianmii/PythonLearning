# -------------------Dictionary----------------------
# Stores info that are connected in some way, connected with key-value pairs

# General format, be mindful of what you name the first two variables
# for key_name, value_name in dictionary_name.items():
# The key  is stored in whatever you called the first variable
# print(key_name)
# The value associated with that key is stored in your second variable
# print(value_name)

python_words = {'list': 'A collection of values that are not connected, but have an order.',
                'dictionary': 'A collection of key-value pairs.',
                'function': 'A named set of instructions that defines a set of actions in Python.',
                }

# Print out the items in the dictionary.
for word, meaning in python_words.items():
    print(f"\nWord: {word}")
    print(f"Meaning: {meaning}")

# ---------------------------------------------
game_words = {'gore magala': 'The eyes have not developed and relies on the Frenzy Virus to hunt.',
              'zinogre': 'The spikes on its body lie flat, but when it has a built up charge, they stick out '
                         'vertically into the air.',
              'dodogama': 'A stout wyvern that uses its strong lower jaw to scoop rocks and compress them into lava '
                          'rocks. '
              }

for word, description in game_words.items():
    print(f"\nMonster: {word.title()}")
    print(f"Description: {description}")

# empty dictionary
animal_facts = {}

# Fill dictionary, pair by pair
animal_facts['millipedes'] = 'They are roly polies and snakes combined into one.'
animal_facts['bats'] = 'Bats are bugs.'
animal_facts['martins'] = 'Super cute ferrets.'

for animal, fact in animal_facts.items():
    print(f"\nAnimal: {animal.title()}")
    print(f"Fact: {fact}")


# ------------------------------------
# USE DEF AND LABEL THEM, NO GLOBAL
# -----------------------------------

def show_game_facts(game_factoid):
    # This function takes in a dictionary of animal names and facts
    # prints each word with meaning
    print("\nThese are the Monster Hunter facts I know:")
    for game, facts in game_factoid.items():
        # THIS PART IS MUCH CLEANER vs earlier typing out the literal words like
        # Animal: Bats, Fact: They fly VERSUS
        # Bats: They fly
        print(f"{game.title()}: {facts}")


game_facts = {'gore magala': 'The eyes have not developed and relies on the Frenzy Virus to hunt.',
              'zinogre': 'The spikes on its body lie flat, but when it has a built up charge, they stick out '
                         'vertically into the air.',
              'dodogama': 'A stout wyvern that uses its strong lower jaw to scoop rocks and compress them into lava '
                          'rocks. '
              }
show_game_facts(game_facts)

# Remove word 'dodogama' and facts from dictionary
del game_facts['dodogama']

show_game_facts(game_facts)

#############################
# MODIFYING KEYS is trickier
# Make a new key, copy and assign same value
# delete old key and also deletes old value

game_facts = {'RAFoLOS': 'Shows up in every Monster Hunter game.'}

# create new key spelled correctly and connect to old value
# Delete the old key

game_facts['Rathalos'] = game_facts['RAFoLOS']
del game_facts['RAFoLOS']

# print dictionary show key changed
print(game_facts)
# --------------------------------------------

# LOOPING THROUGH ALL KEY VALUE PAIRS


my_dictionary = {'key_1': 'value_1',
                 'key_2': 'value_2',
                 'key_3': 'value_3',
                 }

for key, value in my_dictionary.items():
    print(f"\n{key}: {key}")
    print(f"\n{value}: {value}")
