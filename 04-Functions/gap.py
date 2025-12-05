def f(number1,number2,number3):
    if number1 < number2 and number1 < number3:
        if number2 < number3:
            difference = number3 - number1
        elif number2 > number3:
            difference = number2 - number1
    elif number2 < number1 and number2 < number3:
        if number1 < number3:
            difference = number3 - number2
        elif number1 > number3:
            difference = number1 - number2
    elif number3 < number1 and number3 < number2:
        if number1 > number2:
            difference = number1 - number3
        elif number1 < number2:
            difference = number2 - number3
    else:
        print('0')
    print(difference)
f(23,7,9)
        