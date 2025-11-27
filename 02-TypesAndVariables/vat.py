def tax(amount):
    vat = amount*0.23
    print(f'Amount : {amount:.2f}')
    print(f'VAT 23% : {vat:.2f}')

amount = float(input('Enter the amount:'))
tax(amount)