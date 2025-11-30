def f(a,b):
    result = 0
    for x in range(a,b+1):
        if x % 3 == 0:
            result = result + x
    return result
f(2,10)

