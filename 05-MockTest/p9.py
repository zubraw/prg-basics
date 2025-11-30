def f(size1,size2):
    #XS,S,M,L,XL
    if size1 == size2:
        return 0   
    else:
        if size1 == 'XS' and size2 != size1:
            return 2
        elif size2 == 'XS' and size2 != size1:
            return 1
        elif size1 == 'S' and size2 != size1 and size2 != 'XS':
            return 2
        elif size2 == 'S' and size2 != size1 and size1 != 'XS':
            return 1
        elif size1 == 'M' and size2 != size1 and size2 != 'XS' and size2 != 'S':
            return 2
        elif size2 == 'M' and size2 != size1 and size1 != 'XS' and size1 != 'S':
            return 1
        elif size1 == 'L' and size2 != size1 and size2 != 'XS' and size2 != 'S' and size2 != 'M':
            return 2
        elif size2 == 'L' and size2 != size1 and size1 != 'XS' and size1 != 'S' and size1 != 'M':
            return 1
        elif size1 == 'XL' and size2 != size1 and size2 != 'XS' and size2 != 'S' and size2 != 'M' and size2 != 'L':
            return 2
        elif size2 == 'XL' and size2 != size1 and size1 != 'XS' and size1 != 'S' and size1 != 'M' and size1 != 'L':
            return 1
            
