###
# A program that checks whether the number entered
# from the keyboard is even.
# A number is even if the remainder when divided by 2 is 0.
# What operator do you need to use to calculate
# the remainder of division?
#

def even(num):
    result = num/2
    result = int(result)
    if num % 2 == 0:
        print(f'Number is even: {num}/2={result}')
    else:
        print(f'{num} is not even')
num = int(input("Enter number: "))
even(num)