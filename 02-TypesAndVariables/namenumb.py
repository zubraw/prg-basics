###
# A program that prints a numerical representation of each letter of your name.
#
def f(name):
    for num in range(0, len(name)):
        print(f'The letter {name[num]} has a code {ord(name[num])}')

name = input('What is your name?: ')
f(name)
