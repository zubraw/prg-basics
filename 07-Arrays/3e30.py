array = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
array[0] = [1,2,3,4,5]
for i in range(5):
    for j in range(5):
        array[i][j] = (i+1) * (j+1)

for row in array:
    for val in row:
        print(val, end=' ')
    print()
