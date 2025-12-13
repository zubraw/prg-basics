price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
before_total = 0
after_total = 0
print('BEFORE DISCOUNT')
print('==========================')
for product,price in price_list.items():
    print(f'{product}: {price}')
    before_total += price
    before_total = round(before_total, 2)
print(f'Total value before discount: {before_total}')
print()
print('AFTER DISCOUNT')
print('==========================')
for product,price in price_list.items():
    price = round(price*0.9, 2)
    print(f'{product}: {price}')
    after_total += price
    after_total = round(after_total, 2)
print(f'Total value after discount: {after_total}')
