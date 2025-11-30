def suma(a,b):
    sum = 0
    for i in range(a,b+1):
        sum = sum+i
    print(f'Suma liczb od {a} do {b} to: {sum}')
suma(1,7)