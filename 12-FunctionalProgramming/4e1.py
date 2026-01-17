employees = [
'SMITH Lucy',
'JONES Janet',
'LEE Jerry',
'JACKSON Peter',
'JOHNSON Rick',
'LEWIS Terry',
'CLARKE Robin'
]

emp_j = list(filter(lambda x: x[0] == 'J', employees))

print(emp_j)