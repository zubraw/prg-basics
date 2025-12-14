import csv
with open('vehicle.txt','r',encoding='utf-8') as file1:
    content1 = file1.read()
vehicles = content1.splitlines()
cars={}
with open('province.csv','r',encoding='utf-8') as file2:
    content2 = csv.reader(file2)
    next(content2)
    
    for row in content2:
        for car in vehicles:
            if row[0] == car[0]:
                if row[1] in cars:
                    cars[row[1]]+=1
                else:
                    cars[row[1]] = 1
print(cars)
