

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

    while wrong < len(world) - 1:
        print ("\n")
        msg = ("Guess a letter: ")
        char = input(msg)

        if char in rletters:
            cind = rletters.index(char)
            board [cind] = char
            rletters [cind] = '$'
        else:
            wrong =+ 1

        print(" ".join(board))
        e = wrong + 1
        print("\n".join[0:e]) 

        if "__" not in board:
            print ("You win!The word was: {}".format(world))
            win = True
            break

    if not win:  
        print("\n".join(stages[0:wrong]))
        print("You lose! The word was: {}".format(world)) 

hangman("Heart")       



    
