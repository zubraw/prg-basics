###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
def cuboid(a,b,c):
    volume = a*b*c
    surfcase_area = (2*a*b) + (2*a*c) + (2*b*c)
    print('The sides of the cuboid:')
    print(f'a={a}, b={b}, c={c}')
    print(f'Volume: {volume}')
    print(f'Surfcase area: {surfcase_area}')

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
cuboid(a,b,c)