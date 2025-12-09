names = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
print('Names: ',end='')
for i in names:
    print(i,end=' ')
print()
longest_name = names[0]
for name in names:
    if len(longest_name) < len(name):
        longest_name = name
print(f'Longest name: {longest_name}')
