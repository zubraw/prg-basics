import json
with open('computer.json','r', encoding='utf-8') as file:
    info = json.load(file)

for key,value in info.items():
    print(key,':',value)