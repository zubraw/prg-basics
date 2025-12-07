#The list contains vehicle registration numbers in Poland. 
# Cars from Krakow have numbers starting with the letters 'KR' or 'KK'.
# Write a program that prints car registration numbers from Krakow. Number the list printed.

polish_license_plates = [
   'KR5233F', 'PO6987E', 'KR16179', 'BI7192L', 'KK12255',
   'WA7930T', 'SK6922I', 'KK61108', 'KR90538', 'BI8052Q',
   'KK54985', 'LU4864U'
]
i=1
for num in polish_license_plates:
    if num[0:2] == 'KK' or num[0:2] == 'KR':
        print(f'{i}. {num}')
        i = i + 1