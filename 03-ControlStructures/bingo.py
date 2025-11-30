i=1
while i<=30:
    if i%3==0 and i%5==0:
        print('BINGO',end=' ')
    elif i%5==0:
        print('FIVE',end=' ')
    elif i%3==0:
        print('THREE',end=' ')
    else:
        print(i,end=' ')

    i += 1
    
