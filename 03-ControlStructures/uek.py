###
# Prints the name of university where you are studying
# with an extra space between characters (add a space between
# each character), e.g.
# 'book' -> 'b o o k'
#

def f(university):
    university_expanded = '' 
    for char in university:
        university_expanded = university_expanded + char + ' '
    print(f'University: {university}')
    print(f'University expanded: {university_expanded}')
f('Krakow University of Economics')