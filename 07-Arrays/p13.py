# Prices of 10 products in the computer store (in currency units)
product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]

# Number of units available for each product
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]

i = 0
total = 0
for product in product_prices:
    print('Product no.',i+1,': ', round(product*product_quantities[i], 2))
    total = total + (product*product_quantities[i])
    total = round(total , 2)
    i += 1
print(f'Total cost: {total}')