arr = [32,45,76,12,81]

print(arr[3])
arr[4] = 14

###
# arr[0] pierwsza
# arr[-1] ostatnia (tylko w pythonie)
# arr[]

n = len(arr) #liczy liczbe elementow
arr[n -1] #n-1 bo ostatni element ma licze 4 a nie 5
arr[len(arr)-1]
arr[-1] #te 3 wyrazenia maja takie samo znaczenie

arr[len(arr)//2]

arr[1:3] # w tym przypadku wypisuje wartosci 45, 76 (bez 12)
for element in arr:
    print(element)

n = 0

while n < len(arr):
    arr[n] = 0
    n = n+1