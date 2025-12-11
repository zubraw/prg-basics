arr=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
print('Before')
for i in arr:
    for j in i:
        print(j,end=' ')
    print()
extra_row = arr[2]
arr[2] = arr[0]
arr[0] = extra_row
print('After')
for i in arr:
    for j in i:
        print(j,end=' ')
    print()
