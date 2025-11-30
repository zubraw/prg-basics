def f(student1, student2):
    oceny1 = [int(x) for x in student1.split(',') if x in '2345']
    oceny2 = [int(x) for x in student2.split(',') if x in '2345']

    srednia1 = sum(oceny1) / len(student1) if oceny1 else 0
    srednia2 = sum(oceny2) / len(student2) if oceny2 else 0
    if srednia1>srednia2:
        print('1')
    elif srednia1<srednia2:
        print('2')
    else:
        print('0')
student1 = '2,2,3,4'
student2 = '5,5,4,4'
f(student1, student2)