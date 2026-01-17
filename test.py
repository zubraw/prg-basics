add = lambda x, y: x + y
#print(add(2,3))

num = [1,2,3,4,5]
doubled = map(lambda x: x*2, num)
print(list(doubled))

gte_3 = filter(lambda x: x>=3, num)
print(list(gte_3))

students = [
    {'name': 'Anna', 'age': 22},
    {'name': 'Ben', 'age': 21},
    {'name': 'Clara', 'age': 19}
]

students.sort(key=lambda x: x['name'])
print(students)