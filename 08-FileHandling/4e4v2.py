import re
email_file = 'report.txt'
with open(email_file,'r',encoding='utf-8') as file:
    email=file.read()
pattern = r'€(\d+)'
amounts = re.findall(pattern,email)
result = 0
for amount in amounts:
    result += int(amount)
print(result)