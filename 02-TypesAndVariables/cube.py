###
# A program to calculate the volume and surface area of ​​a cube.
# 

def cube(a):
    cube_volume = a**3
    cube_surfcase_area = a**2*6
    print(f'The volume of the cube with side {a} is: {cube_volume}')
    print(f'The surfcase area of the cube with side {a} is: {cube_surfcase_area}')
a = float(input('Cube side: '))
cube(a)