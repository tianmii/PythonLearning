# Kwargs


def character_info(name, game, **kwargs):
    print(f"Name: {name.title()}")
    print(f"Game: {game.title()}")
    # optional info
    for key in kwargs:
        print(f"{key.title().replace('_', ' ')}: {kwargs[key].title()}")
            # added .replace('_', ' ') so key title didn't have _
            # favorite_animal becomes Favorite Animal
    print('\n')


character_info(
    'link',
    'breath of the wild',
    favorite_animal='epona',
)

character_info(
    'aloy',
    'horizon zero dawn',
    favorite_person='rost',
    specialty_move='sneak',
)

character_info(
    'geralt',
    'witcher 3',
    favorite_daughter='ciri',
    witcher_school='wolf',
)
