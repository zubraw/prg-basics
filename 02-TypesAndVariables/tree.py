###
#A tree may be cut down if its diameter 
# is at least 50 cm. Write a program that, 
# based on the circumference of the tree 
# entered from the keyboard, calculates 
# and prints the value True if the tree 
# can be cut down, or print the value 
# False otherwise.
#Obwód: 2ℼr
#Średnica: 2r

def tree(obw):
    diameter = obw//3.14
    can_be = diameter>=50
    print(f'Enter tree circumference in cm: {obw}')
    print(f'Tree can be cut down: {can_be}')
obw = float(input('Enter tree circumference: '))
tree(obw)