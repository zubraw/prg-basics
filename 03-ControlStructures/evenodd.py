###
# Checking whether the number
# entered from the keyboard is even or odd 
#

def f(number):
    if number % 2 == 0:
        is_even = True
    else:
        is_even = False
    print(f'{number} is even: {is_even}')
f(5)