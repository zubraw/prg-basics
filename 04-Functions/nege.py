def f(x,y):
    neg_even_num = 0
    for i in range(x,y+1):
        if i<0 and i%2==0:
            neg_even_num = neg_even_num + 1
        else:
            neg_even_num = neg_even_num
    return neg_even_num
f(-5,7)
