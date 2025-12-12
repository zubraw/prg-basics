import csv
with open('clothing.csv','r') as file:
    read_file = csv.reader(file)
    next(read_file)
    for row in read_file:
        price = float(row[5])
        stock = int(row[6])
        #price is less than 60 and 
        # whose stock is less than 40
        if price<60 and stock<40:
            print(row)