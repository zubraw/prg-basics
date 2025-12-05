def f(product_code):
   digits = [int(d) for d in product_code]
   suma = sum(digits[:3] + digits[4:])
   print(digits[3] == suma%7)
f('1082')