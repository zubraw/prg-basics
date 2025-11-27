import math
def f(a,b):
    diagonal = math.sqrt(a**2 + b**2)
    print(f'The diagonal of the triangle where a={a} and b={b} is: {diagonal}')

a = float(input('Enter the lenght of the first side: '))
b = float(input('Enter the lenght of the second side: '))
f(a,b)