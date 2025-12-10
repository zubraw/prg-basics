array=[2,3,2,5,8,1,9,8]
print('Array: ',end='')
for i in array:
    print(i, end=' ')
print()
print('Unique elements: ',end='')
for i in array:
    if array.count(i) == 1: #array.count(x) odpowiada za liczenie elementów ile razy występują w tabeli array
        print(i,end=' ')