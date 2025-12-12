with open('ex11.txt','a') as file:
    i=1
    while i<=100:
        second = i**2
        third = i**3
        file.write(f'{i},{second},{third}\n')
        i+=1