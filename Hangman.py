
#definindo a função e criando as variaveis 
def hangman(world):
    wrong = 0
    stages = ["",
              "________ ",
              "|        ",
              "|   |    ",
              "|   0    ",
              "|  /|\   ",
              "|  / \   ",
              "|        "]
    rletters = list(world)
    board = ["__"] * len(world)
    win = False
    print("Welcome to Hangman")


    