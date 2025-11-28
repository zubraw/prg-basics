###
# A program that enables a user to challenge a computer.
# The computer throws dice. Then, the user then tries to guess
# the number from dice by entering a number from 1 to 6
# from the keyboard. If the user has guessed the number
# from the dice, the computer prints True. Otherwise,
# the computer prints False.
#

import random
def guess(you):
    computer = random.randint(1,6)
    if computer == you:
        print('You won!!')
    else:
        print('You lose')
you = int(input('Pick number (1-6):'))
if you > 6 or you < 1:
    print('From 1 to 6...')
else:
    guess(you)    
