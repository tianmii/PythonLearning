
for pokemon_name, pokemon_type in pokemon.items():
    print("\n{pokemon_name}".format(
        pokemon_name=pokemon_name.title()
    ))
    for key in pokemon_type:
        if key == 'type':
            print("{key_type}: {value_type}".format(
                key_type=key.title(),
                value_type=(pokemon_type[key].title()),
            ))
        if key == 'specialty':
            print("{key_specialty}: {value_specialty}".format(
                key_specialty=key.title(),
                value_specialty=(pokemon_type[key].title()),
            ))
        elif key == 'mega evolution':
            mega_evolution = pokemon_type[key]
            if mega_evolution:
                print("Mega Evolution: Yes\n")
            else:
                print("Mega Evolution: No\n")




pokemon = []
pokemon_current = {
    'ghastly': {
        'type': 'ghost & poison',
        'specialty': 'levitation',
        'mega evolution': True,
    },
    'blaziken':{
        'type': 'fire & fighting',
        'speciality': 'kick moves',
        'mega evolution': True,
    },
    'rowlett':{
        'type': 'grass & flying',
        'specialty': 'being cute',
        'mega evolution': True,
    },
}