#creating regions list

regions = ['Kanto', 'Jhoto', 'Hoen', 'Sinnoh']

#Adding possibles choices for each region

kantochoices = ['charmander', 'squirtle', 'bulbasaur']
jhotochoices = ['cyndaquil','totodile','chicorita']
hoenchoices = ['torchick','mudikip','treeko']
sinnohchoices = ['chinchar','piplup','turtwig']

#listing attacks for each type
types = ['fire', 'water', 'grass']

fireskills = ['ember', 'flamethrower', 'fire blast', 'fire punch', 'flame wheel', 'fire spin', 'heat wave', 'blast burn', 'fire fang', 'eruption']
waterskills = ['watergun', 'surf', 'hydro pump', 'aqua tail', 'bubble beam', 'water pulse', 'scald', 'dive', 'aqua jet', 'brine']
grassskills = ['razor leaf', 'solar beam', 'vine whip', 'bullet seed', 'leaf blade', 'energy ball', 'petal dance', 'giga drain', 'grass knot', 'seed bomb']

#startin survey

while True:
    regionchoice = input("PLease, what region do you wish to star you journey? ")
    if regionchoice in regions:
        print('great! You choose the region {}.'.format(regionchoice))
        break  # Sai do loop quando uma escolha válida é feita
    else:
        print('Sorry, We cant provide any information about this place. Please, choose one of these: {}'.format(regions))

#add options
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
    print('Something its wrong!')  

#validation
while True:
    pokemon = input("Please choose your initial Pokémon from the following options: {}: ".format(choices))
    if pokemon in choices:
        print("You chose well! {} is a great Pokémon.".format(pokemon))
        break
    else:
        print("The Pokémon '{}' is not available for selection. Please choose from: {}.".format(pokemon, choices))


skills = []
index = 1
index = choices[index]

if index[0] == 0:
        typepokemon = 'fire'
        skills = fireskills
elif index[0] == 1:
        typepokemon = 'water'
        skills = waterskills
elif index[0] == 2:
        typepokemon = 'grass'
        skills = grassskills
else:
    print('Something is wrong!')




#validation
    print('You chose is a  {} one. It can learn these moves: {}.'.format(typepokemon, skills))

Strenghten= []           

if typepokemon == 'fire':
    Strenghten = ['grass','fly','bug','steel']
elif typepokemon == 'waters' :
   Strenghten = ['Rock','ground','fire']
elif typepokemon == 'grass':
    Strenghten = ['Water','ground','rock']
else:
    print('Something its wrong!')             


frase = "You choose very well! The {pokemon}, is a {type} pokemon. They easily learn the moves like {moves}, that is very efective against {Strenghten} ones".format(pokemon=pokemon, type=typepokemon, moves=index, Strenghten=Strenghten)

print(frase) 
