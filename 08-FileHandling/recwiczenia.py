import re
wzor = r'banan'
tekst = r'gruszkabananjablko'

if re.match(r'.*'+wzor+r'.*', tekst):
    print('dopasowano')
else:
    print('nie dopasowano')

if re.search(wzor,tekst):
    print('dopasowano')
else:
    print('nie dopasowano')

print(re.findall(wzor,tekst))