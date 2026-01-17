###
# Calculates arithmetic mean of two integer numbers
#
def mean(x,y):
    mean = round((x+y)/2,2)
    return mean

n1 = int(input('First number'))
n2 = int(input('Second number'))

result = mean(n1,n2)
print(result)
