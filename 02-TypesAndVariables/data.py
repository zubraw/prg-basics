###
# Printing student's personal data
#

def data(name,age,height):
    print(f'My name is {name}')
    print(f'I am {age} years old, and my height is {height} cm.')
    print('In 6 years I will be ', age + 6,' years old.')

name = input('What is your name?: ')
age = int(input('How old are you?: '))
height = int(input('What is your height?: '))
data(name,age,height)
    