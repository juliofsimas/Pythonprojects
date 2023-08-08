pokemon = input("Please choose a initial pokemon ")
type = input("What Type of pokemon did you choose? ")
moves= input("What is your favourite move?")
Strenghten = input("To fight against? ")

frase = "You choose very well, the {pokemon}, is a {type} type of pokemon. They easily learn the move {moves}, that is very efective against {Strenghten} ones".format(pokemon=pokemon, type=type, moves=moves, Strenghten=Strenghten)

print(frase)