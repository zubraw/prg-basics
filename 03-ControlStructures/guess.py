###
# A simple number guessing game
#
import random

# Randomly chosen number to be guessed from 1 to 100
num_to_guess = random.randint(1,100)
user_guess = 0
print("Guess the number between 1 and 100!")
while user_guess != num_to_guess:
    user_guess = int(input('Enter your number'))
    if user_guess < num_to_guess:
        print('Too low..')
    elif user_guess > num_to_guess:
        print('Too high')
    else:
        print("Congratulations! You guessed the correct number.")