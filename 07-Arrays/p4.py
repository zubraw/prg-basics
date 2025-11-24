###
# Prints some array elements
#the array
#number of elements
#first value
#second value
#last value
#last but one value (do not use negative index values)
#sum of the first and last value
#middle value
#all array values separated by a single space (use a loop statement)


arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print(f'Last value: {arr[-1]}')
print(f'Last but one value: {arr[-2]}')
sum = arr[0] + arr[-1]
print(f'Sum of the first and last value: {sum}')
m = len(arr)//2
print(f'Middle value: {arr[m]}')
for element in arr:
    print(element, end=' ')