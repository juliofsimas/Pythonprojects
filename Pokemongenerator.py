# Creating regions list
regions = ['Kanto', 'Jhoto', 'Hoen', 'Sinnoh']

# Adding possible choices for each region
kantochoices = ['charmander', 'squirtle', 'bulbasaur']
jhotochoices = ['cyndaquil', 'totodile', 'chicorita']
hoenchoices = ['torchick', 'mudikip', 'treeko']
sinnohchoices = ['chinchar', 'piplup', 'turtwig']

# Listing attacks for each type
types = ['fire', 'water', 'grass']
fireskills = ['ember', 'flamethrower', 'fire blast', 'fire punch', 'flame wheel', 'fire spin', 'heat wave', 'blast burn', 'fire fang', 'eruption']
waterskills = ['watergun', 'surf', 'hydro pump', 'aqua tail', 'bubble beam', 'water pulse', 'scald', 'dive', 'aqua jet', 'brine']
grassskills = ['razor leaf', 'solar beam', 'vine whip', 'bullet seed', 'leaf blade', 'energy ball', 'petal dance', 'giga drain', 'grass knot', 'seedbomb']

# Starting survey
while True:
    regionchoice = input("Please, what region do you wish to start your journey? ")
    if regionchoice in regions:
        print('Great! You chose the region {}.'.format(regionchoice))
        break  # Sai do loop quando uma escolha válida é feita
    else:
        print('Sorry, we can’t provide any information about this place. Please, choose one of these: {}'.format(regions))

# Add options
choices = []
if regionchoice == 'Kanto':
    choices = kantochoices
elif regionchoice == 'Jhoto':
    choices = jhotochoices
elif regionchoice == 'Hoen':
    choices = hoenchoices
elif regionchoice == 'Sinnoh':
    choices = sinnohchoices
else:
    print('Something is wrong!')

# Validation
while True:
    pokemon = input("Please choose your initial Pokémon from the following options: {}: ".format(choices))
    if pokemon in choices:
        print("You chose well! {} is a great Pokémon.".format(pokemon))
        break
    else:
        print("The Pokémon '{}' is not available for selection. Please choose from: {}.".format(pokemon, choices))

# Aqui vamos associar diretamente os Pokémon ao seu tipo
if pokemon in ['charmander', 'cyndaquil', 'torchick', 'chinchar']:
    typepokemon = 'fire'
    skills = fireskills
elif pokemon in ['squirtle', 'totodile', 'mudikip', 'piplup']:
    typepokemon = 'water'
    skills = waterskills
elif pokemon in ['bulbasaur', 'chicorita', 'treeko', 'turtwig']:
    typepokemon = 'grass'
    skills = grassskills
else:
    print('Something is wrong!')


# Validation
print('Your Pokémon is a {} type. It can learn these moves: {}.'.format(typepokemon, skills))

Strenghten = []
if typepokemon == 'fire':
    Strenghten = ['grass', 'fly', 'bug', 'steel']
elif typepokemon == 'water':
    Strenghten = ['rock', 'ground', 'fire']
elif typepokemon == 'grass':
    Strenghten = ['water', 'ground', 'rock']
else:
    print('Something is wrong!')

frase = "You chose very well! The {}, is a {} Pokémon. It easily learns moves like {}, which are very effective against {} types.".format(pokemon, typepokemon, skills, Strenghten)
print(frase)
