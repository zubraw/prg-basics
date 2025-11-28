def f(speed):
    is_valid = speed>40 and speed<140
    print(f'Speed is valid: {is_valid}')
speed = float(input('Enter vehicle speed: '))
f(speed)