def identity_matrix(n):
    arr = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        arr.append(row)
    numx = 0
    numy = 0
    for i in arr:
        arr[numy][numx] = 1
        numx+=1
        numy+=1
    for i in arr:
        for j in i:
            print(j,end=' ')
        print()
identity_matrix(8)