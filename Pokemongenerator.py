pokemon = input("Please choose your initial pokemon ")
type = input("What Type of pokemon did you choose? ")
moves= input("What is your favourite move?")
Strenghten = input("To fight against? ")

frase = "You choose very well! The {pokemon}, is a {type} pokemon. They easily learn the moves like {moves}, that is very efective against {Strenghten} ones".format(pokemon=pokemon, type=type, moves=moves, Strenghten=Strenghten)

print(frase)    
