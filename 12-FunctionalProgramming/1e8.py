name = input('Name: ')
surname = input('Surname: ')

initials = lambda x,y: f'{x.upper()[0]}.{y.upper()[0]}.'

print(initials(name,surname))