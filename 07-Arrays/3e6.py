arr = [15, 8, 31, 47, 2, 19]
i=0
value = 0
while i < len(arr):
    value += arr[i]
    i+= 1
result = round(value/len(arr), 2)
print(result)