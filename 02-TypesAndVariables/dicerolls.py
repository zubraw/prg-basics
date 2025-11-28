import random
diceroll1 = random.randint(1,6)
diceroll2 = random.randint(1,6)
diceroll3 = random.randint(1,6)
sum = diceroll1 + diceroll2 + diceroll3
print(f'First dice roll: {diceroll1} ')
print(f'Second dice roll: {diceroll2} ')
print(f'Third dice roll: {diceroll3} ')
print(f'Sum of the dice rolls: {sum}')