###
# A program for printing detailed information.
#
def f(employee):
    words=employee.split()
    name = words[1]
    surname = words[2].replace(',','')
    born = words[-1]
    print(f'Name: {name}')
    print(f'Surname: {surname}')
    print(f'Born: {born}')
    print(f'Initials: {name[0]}.{surname[0]}.')


employee = "Mr. John May, born on 1998-02-16"
f(employee)