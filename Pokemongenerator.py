#creating regions list

regions = ['Kanto','Jhoto','Hoen','Sinnoh','Unova']

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
regions = ['Kanto', 'Jhoto', 'Hoen', 'Sinnoh']

while True:
    regionchoice = input("PLease, what region do you wish to star you journey: ")
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
           
  
pokemon = input("Please choose your initial pokemon: {}.".format(choices))

#validation
while True:
  if pokemon not in choices:
      print('The pokemon {} is not available for selection. Choose from {}'.format(pokemon, choices))
      break
  else:
      print('You chose well!{} is a great pokemon'.format(pokemon)

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
