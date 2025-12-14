import json
product = {}
name = input('Name of he product: ')
price = float(input('Price: '))
paid = input('Paid(y/n): ')

product['name'] = name
product['price'] = price
if paid not in ['y','n','Y','N']:
    product['paid'] = False
elif paid in ['y','Y']:
    product['paid'] = True
else:
    product['paid'] = False
    
with open('product.json','w') as file:
    string = json.dumps(product, indent=4)
    file.write(string)