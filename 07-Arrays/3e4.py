arr = [-15, 8, -31, 47, -2, 19]
n = len(arr)
for i in range(n):
    for j in range(0,n-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
min_arr = arr[0]
max_arr = arr[-1]
