def f(size1,size2):
    def value(size):
        if size == 'XS':
            return 1
        elif size == 'S':
            return 2
        elif size == 'M':
            return 3
        elif size == 'L':
            return 4
        elif size == 'XL':
            return 5
    s1 = value(size1)
    s2 = value(size2)
    if s1==s2:
        print('0')
    elif s1 > s2:
        print('1')
    elif s1 < s2:
        print('2')
f('L','M')