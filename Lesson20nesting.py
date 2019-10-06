# Lists in a dictionary
# Stores lists and displays
fav_list = {'zelda': ['Breath of the wild, Ocarina of Time, Link Between Worlds'],
            'harry potter': ['Prisoner of Azkaban', 'Goblet of Fire', 'Chamber of Secrets'],
            'pokemon': ['Ghastly', 'Blaziken', 'Hitmonchan']
            }

print("Favorite zelda games:")
print(fav_list['zelda'])

print("Favorite harry potter books:")
print(fav_list['harry potter'])

print("Favorite pokemon:")
print(fav_list['pokemon'])

# ----------------------------------------------
# Monsters.... DICTIONARIES IN DICTIONARIES
# original formatting was confusing to distinguish key: value
# {''type':'frenzy virus', 'variation': 'none', 'g-rank':True} <--madness on the eyes

monsters = {
    'gore magala': {
        'type': 'frenzy virus',
        'variation': 'none',
        'g-rank': True,
    },
    'tobi kadachi': {
        'type': 'electric',
        'variation': 'viper',
        'g-rank': False,
    },
    'zinogre': {
        'type': 'electric',
        'variation': 'stygian',
        'g-rank': True,
    },
}

for monster_name, monster_type in monsters.items():
    print(f"\nHere is some information about {monster_name.title()}")
    for key in monster_type:
        if key == 'type':
            print(f"{key}: {monster_type[key]}")
        elif key == 'g-rank':
            # Example how variable string can't be named g-rank>g_rank
            g_rank = monster_type['g-rank']
            # Instead of True/False, print yes/no
            if g_rank:
                print('g-rank: yes')
            else:
                print('g-rank: no')
        # else:
        # print(key + ": " + str(monster_type[key])) orignal format......
        # hard to read and no longer have to add "str()"
        # print(f"{key}: {monster_type[key]}")
