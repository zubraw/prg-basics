person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

for key,value in person.items():
    if isinstance(value, list):
        for i in value:
            print(f'{key}: {i}')
    elif isinstance(value, dict):
        print(f'{key}: ',end='\n')
        for key2,value2 in value.items():
            print(f'\t{key2}: {value2}')
    else: print(f'{key}: {value}')