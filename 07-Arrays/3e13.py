def occurs(number,array):
    for i in array:
        if number == i:
            return True
    return False

number = int(input('Enter number:'))
array = [15,38,7,23,14]
print(f'Number: {number}')
print('Array: ', end='')
for i in array:
    print(i,end=' ')
print()
if occurs(number,array):
    print(f'Result: number {number} appears in the array')
else:
    print(f'Result: number {number} do not appears in the array')