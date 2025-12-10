x = (10,20,30,40,50,)
print('Tuple: ',end='')
for i in range(len(x)):
    if i < len(x) - 1:
        print(x[i],end=',')
    else:
        print(x[i])
print('Reverse order: ',end='')
for i in reversed(x):
    print(i,end=' ')
