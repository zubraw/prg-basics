def f(number, even):
    sum = 0
    for num in str(number):
        digit = int(num)
        if even:
            if digit % 2 == 0:
                sum = sum + digit
        else:
            if digit % 2 != 0:
                sum = sum + digit
    print(f'{number}, {even} => {sum}')
f(2049203, True)

