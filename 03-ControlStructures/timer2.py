import time
def timer(number):
    while number>0:
        if number == 5:
            print('Five')
        elif number == 4:
            print('Four')
        elif number == 3:
            print('Three')
        elif number == 2:
            print('Two')
        elif number == 1:
            print('One')
        else:
            print(number)
        number = number - 1
        time.sleep(1)
timer(10)
        