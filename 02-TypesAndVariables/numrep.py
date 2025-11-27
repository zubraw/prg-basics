###
# A program to print numerical representations of characters.
#
def numrep():
    print(f'a = {ord('a')}')
    print(f'b = {ord('b')}')
    print(f'z = {ord('z')}')
    print(f'A = {ord('A')}')
    print(f'B = {ord('B')}')
    print(f'Z = {ord('Z')}')
    print(f'1 = {ord('1')}')
    print(f'= = {ord('=')}')
    print(f'+ = {ord('+')}')
    print(f'€ = {ord('€')}')

numrep()

def numb(letter):
    print(f'{letter} = {ord(letter)}')

i=0
while i<10:
    letter = input('Please enter the letter: ')
    numb(letter)

    

    