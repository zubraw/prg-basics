import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
    stack = queue.LifoQueue()
    pairs = {')':'(', ']':'[', '}':'{'}
    for char in expression:
        if char in '({[':
            stack.put(char)
        elif char in ')}]':
            if stack.empty():
                return False
            if stack.get() != pairs[char]:
                return False
            
    return stack.empty()

          
    
    return #True if brackets in expression are ok of False otherwise

if brackets_ok(expression1):
   print(f'{expression1} ---> is ok ')
else:
   print(f'{expression1} ---> is not ok ')

if brackets_ok(expression2):
    print(f'{expression2} ---> is ok ')
else:
   print(f'{expression2} ---> is not ok ')

if brackets_ok(expression3):
    print(f'{expression3} ---> is ok ')
else:
   print(f'{expression3} ---> is not ok ')