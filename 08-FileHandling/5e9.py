import csv

with open('it_company.csv','r') as file:
    read_file = csv.reader(file)
    print('GRAPHIC DESIGNERS')
    print('=====================')
    for row in read_file:
        if row[2] == 'Graphic Designer':
            print(f'{row[0]} {row[1]}, {row[3]}')