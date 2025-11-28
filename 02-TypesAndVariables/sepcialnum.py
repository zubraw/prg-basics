import random
def f(diceroll):
    is_special = diceroll == 1 or diceroll == 6
    print(f'Dice rolled: {diceroll}')
    print(f'Special number (1 or 6): {is_special}')
diceroll = random.randint(1,6)
f(diceroll)