###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math


def triangle_area(a,b,c):
    s = 0.5*(a + b  + c)
    p = s*(s - a)*(s - b)*(s - c)
    result = math.sqrt(p)
    return result

result1 = triangle_area(3,5,4)
result2 = triangle_area(5,12,13)
result3 = triangle_area(7,24,25)
    


print(f'The area of ​​a triangle with sides 3,5,4 is {result1}')
print(f'The area of ​​a triangle with sides 5,12,13 is {result2}')
print(f'The area of ​​a triangle with sides 7,24,25 is {result3}')