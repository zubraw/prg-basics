import json

with open('cities.json','r', encoding='utf-8') as file:
    content = json.load(file)

for city in content:
    for key,value in city.items():
        print(key,':',value)
    print()