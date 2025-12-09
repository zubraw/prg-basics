def compare(array1,array2):
    if len(array1) != len(array2):
         is_the_same = False
    for i in range(len(array1)):
            if array1[i] == array2[i]:
                is_the_same = True
            else:
                 is_the_same = False
    if is_the_same:
        result = 'arrays are the same'
    else:
        result='arrays are not the same'
    print('Array1: ',end='')
    for i in array1:
        print(i,end=' ')
    print()
    print('Array2: ',end='')
    for j in array2:
        print(j,end=' ')
    print()
    print(f'Comparison: {result}')

compare(['water','book','sky'],['water','book','sky'])