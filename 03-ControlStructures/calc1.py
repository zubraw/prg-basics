###
# Calculates values for the following fractions: 1/2, 1/3, ..., 1/10
#

def f(n):
    for i in range(1,n+1):
        print(f'1/{i} = {1/i}')
f(23)