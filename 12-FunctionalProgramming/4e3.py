grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]

filtered = list(filter(lambda x: 2.0<x<3.85, grades))
print(filtered)