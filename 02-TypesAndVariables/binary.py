def convert(number):
    binary = bin(number)
    hexadecimal = hex(number)
    print(f'Binary number: {binary}')
    print(f'Hexadecimal number: {hexadecimal}')
number = int(input('Enter number: '))
convert(number)