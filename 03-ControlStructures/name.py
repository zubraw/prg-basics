def f(name):
    is_female = name[-1]=='a'
    if is_female == True:
        print(f'{name} is polish female name')
    else:
        print(f'{name} is not polish female name')

f('Ann')