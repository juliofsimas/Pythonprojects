#defining the lists of pokemons and atacks
choices = ['charmander', 'squirtle', 'bulbasaur']
skills = ['ember', 'watergun', 'razor leaf']

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
