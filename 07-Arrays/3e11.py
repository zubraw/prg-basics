def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    print(f'Sorted array: {array}')
bubblesort([3,1,6,5,8,7])