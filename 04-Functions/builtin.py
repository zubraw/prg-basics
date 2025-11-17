###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

###
#letter read from the keyboard
letter = input('Please enter a letter:')
print(f'You entered letter {letter}')
#number representing the string "20303"
nstring = "20303"
number = int(nstring)
print(number)
#binary string representing decimal number 304
no = 304
bno = bin(no)
print(bno)
#hexadecimal string representing decimal number 304
hno = hex(no)
print(hno)
#integer representing the Unicode code of the € sign
sign = '€'
num = hash(sign)
print(num)
#absolute value of -17
numb = -17
ano = abs(numb)
print(ano)
