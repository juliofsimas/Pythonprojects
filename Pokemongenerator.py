#creating lists of region from pokemons

regions = ['kanto','Jhoto','Hoen','Sinnoh','Unova']
kantochoices = ['charmander', 'squirtle', 'bulbasaur']
jhotochoices = ['cyndaquil','totodile','chicorita']
hoenchoices = ['torchick','mudikip','treeko']
sinnohchoices = ['chinchar','piplup','turtwig']

#defining the lists of pokemons and atacks
types = ['fire', 'water', 'grass']
fireskills = ['ember', 'flamethrower', 'fire blast', 'fire punch', 'flame wheel', 'fire spin', 'heat wave', 'blast burn', 'fire fang', 'eruption']
waterskills = ['watergun', 'surf', 'hydro pump', 'aqua tail', 'bubble beam', 'water pulse', 'scald', 'dive', 'aqua jet', 'brine']
grassskills = ['razor leaf', 'solar beam', 'vine whip', 'bullet seed', 'leaf blade', 'energy ball', 'petal dance', 'giga drain', 'grass knot', 'seed bomb']

#startin survey
regionchoice = input("Please, tell where you wish to begin you journey? ")
if regionchoice not in regions:
    print ('We cant provide you any choice. can you tell me another regio? chose one of these{}'.format(regions))
else:
    print ('oh! great place')
  
pokemon = input("Please choose your initial pokemon: ")

#validation
if pokemon not in choices:
    print('The pokemon {} is not available for selection. Choose from {}'.format(pokemon, choices))
else:
    print('You chose well!')

type = input("What Type of pokemon did you choose? ")

moves= input("What is your favourite move?")
#validation
if pokemon not in skills:
    print('The atack that you chose {} is not available for while. pick one of these below: {}'.format(pokemon, skills))
else:
    print('Good work!')
Strenghten = input("To fight against? ")

frase = "You choose very well! The {pokemon}, is a {type} pokemon. They easily learn the moves like {moves}, that is very efective against {Strenghten} ones".format(pokemon=pokemon, type=type, moves=moves, Strenghten=Strenghten)

print(frase) 
