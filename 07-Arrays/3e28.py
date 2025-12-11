darray =[
    [7,3,7,9,0],
    [2,9,0,1,5],
    [3,8,6,4,7],
    [8,7,1,1,5]
]
for i in darray:
    for j in i:
        print(j,end=' ')
    print()
sum = 0
for i in darray:
    sum += i[-1]
print(f'sum of values in the last column: {sum}')   