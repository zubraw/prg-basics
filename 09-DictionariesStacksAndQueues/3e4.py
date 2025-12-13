import queue
def conventer(number):
    print(f'Natural number: {number}')
    binary = queue.LifoQueue()
    while number>0:
        binary.put(int(number%2))
        if number%2 == 0:
            number = number/2
        else:
            number = (number-1)/2
    
    print('Binary number: ',end='')
    while not binary.empty():
        print(binary.get(),end='')
conventer(67)

    

    

