def f(num,x,y):
    for number in range(x,y+1):
        if number == num:
            is_there = True
    print(f'A number: {num}')
    print(f'Number {num} is in the range <{x},{y}>: {is_there}')
f(5,2,8)