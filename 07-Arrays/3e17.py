tup = (50,20,40,50,30,50,)
value=int(input('Enter the value: '))
print('Tuple: ',end='')
for i in tup:
    print(i,end=' ')
print()
print(f'Value: {value}')
print('Number of occurrences: ',end='')
number = 0
for i in tup:
    number = tup.count(value)
print(number)