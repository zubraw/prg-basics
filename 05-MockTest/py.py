def f(number):
    if number < 0:
        return False
    
    a=0
    b=1
    while a<number:
       a, b=b, a+b
    print(a==number or b==number)
f(5)