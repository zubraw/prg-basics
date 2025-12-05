def f(detector):
    sum=0
    is_there = False
    for i in detector:
        if i == '+':
            sum = sum + 1
            if sum == 3:
                is_there = True
                break  
        elif i == '-':
            sum = sum - 1
    print(is_there)
f("+-++-++-+---")