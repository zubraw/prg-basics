import re

email_file ='report.txt'

with open(email_file,'r',encoding='utf-8') as file:
   email = file.read()

pattern = r'€(\d+)'

amounts = re.findall(pattern,email)

suma = 0
for amount in amounts:
    suma += int(amount)
print(suma)