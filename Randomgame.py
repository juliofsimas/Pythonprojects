import random
import math

#create a function to generate a randon number

def random_number():
    even=[]
    for elem in range(1,10):
        if elem % 2 == 0:
            even.append(elem)
            computer = random.choice(even)
    return

#creat a mechanism to ask the player your choice

def check_guess():
    print ('Guess a number between 1-10, youll have 3 tries'):
    guess=int(input('Enter number: '))

    value = random_number

    if win(guess,value):
        return (1,guess,value)

    if guess < value:
        return(-1,guess,value)
    else:
        return(-1,guess,value)
    
def win (guess,value):
    if guess == value:
        return True
    return False


def best_of(n):
    player_wins=0
    opponents_wins=0
    wins_necessary=math.ceil(n/2)

    while (player_wins<wins_necessary and opponents_wins<wins_necessary):
        (result,guess,value)=check_guess

#checking results
        if (result==1):
            player_wins =+1
            print('You and the computer have chosen {}.you win.'.format(value)) 

        elif ((result == -1)and (guess<value)):
            opponents_wins =+1
            print ('guess to low')

        else:
            opponents_wins =+1
            print ('guess too high')
    if (player_wins > opponents_wins):
        print ('you have won the best out {}.You are the champion'.format(n))
    else:
        print ('unfurtunally you lost.Try again!')    



if __name__ == '__main__':
    best_of(3)        





            
