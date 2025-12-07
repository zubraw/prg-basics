with open('countries.txt', 'r') as file:
    i = 1
    for line in file:
        print(i,line, end='')
        i = i+1