def disc(price, discount):
    price_after = price * (1 - discount/100)
    reduction = price - price_after
    print(f'Enter price: {price:.2f}')
    print(f'Enter discount: {discount:.0f}')
    print(f'Price with discount: {price_after:.2f}')
    print(f'Reduction: {reduction:.2f}')
price = float(input('Please enter the price: '))
discount = float(input('Please enter the discount: '))
if discount > 100:
    print(f'tf u mean {discount}% discount??')
elif discount <= 100:
    disc(price, discount)