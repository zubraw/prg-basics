a = [1,2,3,4,5]
print(f'Array: {a}')
a[0] = 0
print(f'Array: {a}')
a[-1] = 4
print(f'Array: {a}')
m = len(a)//2
a[m] = a[m]*2
print(f'Array: {a}')
