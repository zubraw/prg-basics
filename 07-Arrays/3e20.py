arr = [7,9,2,4,5,6]
n = len(arr)
for i in range(n):
    for j in range(0, n - 1 - i):
        if arr[j] > arr[j+1] or arr[j]%2!=0 and arr[j+1]%2==0:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)