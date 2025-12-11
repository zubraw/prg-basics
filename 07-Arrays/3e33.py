arr=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
print('Before')
for i in arr:
    for j in i:
        print(j,end=' ')
    print()
print('After')
n=0
for i in arr:
    extra = arr[n][-1]
    arr[n][-1] = arr[n][0]
    arr[n][0] = extra
    n+=1
for i in arr:
    for j in i:
        print(j,end=' ')
    print()
