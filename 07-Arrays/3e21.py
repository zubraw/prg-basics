def arrays(array1,array2):
    for i in array1:
        if i not in array2:
            return False
    return True
array2 = [1,2,3,5,2,4,14,3]
array1 = [1,2,3]
print(arrays(array1,array2))