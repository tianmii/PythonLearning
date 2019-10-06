# Kwargs


def character_info(name, game, **kwargs):
    print("Name: {chara_name}".format(chara_name=name.title()))
    print("Game: {chara_game}".format(chara_game=game.title()))
    # optional info
    for key in kwargs:
        print("{key_title}: {kwarg_key}".format(
            # added .replace('_', ' ') so key title didn't have _
            # favorite_animal becomes Favorite Animal
            key_title=key.title().replace('_', ' '),
            kwarg_key=kwargs[key].title(),
        ))
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
    wticher_school='wolf',
)
