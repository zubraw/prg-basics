
###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#3, 4, 5 (result is 6)
import math
def triangle(a, b, c):
    s = 0.5*(a + b + c)
    wynik = math.sqrt(s * (s-a) * (s-b) * (s-c))
    return wynik

triangle1 = triangle(3, 4, 5)
triangle2 = triangle(5, 12, 13)
triangle3 = triangle(7, 24, 25)


print(f"The area of a triangle with sides 4,5,6 is {triangle1}")
print(f"The area of a triangle with sides 5,12,13 is {triangle2}")
print(f"The area of a triangle with sides 7,24,25 is {triangle3}")