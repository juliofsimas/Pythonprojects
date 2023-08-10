import random

class Dice:

    def roll (self):
        roll=[]
        for elem in range (1,7):
            roll.append(elem)
        computer = random.choice(roll)

        return computer

while True:
    d = Dice()
    print(d.roll())
    another_roll =input('want to roll the dice again? type "yes" to roll dice: ')    
    if another_roll.lower() == 'yes':
        continue
    else:
        break

