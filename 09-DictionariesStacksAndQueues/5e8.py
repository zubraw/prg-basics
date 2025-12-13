# Price list
prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

# Shopping cart with quantities
cart = {'juice': 3, 'bread': 1, 'milk': 2}

total=0
for key, price in prices.items():
    for key2, quantities in cart.items():
        if key==key2:
            total+= (price*quantities)
total = round(total,2)
print(total)
