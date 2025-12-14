
def f(string):
    stack = []
    for char in string:
        stack.append(char)
    
    reversed = ''
    while stack:
        reversed += stack.pop()
    return reversed
#print(f('jaja jak berety'))