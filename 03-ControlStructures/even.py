###
# Calculates the sum of 
# even numbers in the range <1,10>
#

def f(a,b):
    sum = 0
    for i in range(a,b+1):
        if i%2==0:
            sum=sum+i
        else:
            continue
    print(f'Suma liczb parzystych od {a} do {b} to {sum}')
f(1,8)