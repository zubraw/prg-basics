import json
#aDict = {'a':54, 'b':87}

#WPISYWANIE DANYCH DO PLIKU
#with open('plik.txt', 'w') as file:
#    json_string = json.dumps(aDict, indent= 4)
#    file.write(json_string)

#WYPISYWANIE DANYCH Z PLIKU
#with open('plik.txt','r') as file:
#    slownik = json.loads(file.read())
#    print(slownik)



class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

# p1 = Osoba('Marian', 36)

# with open('plik.json', 'w') as plik:
#     json_string = json.dumps(p1.__dict__, indent=4)
#     plik.write(json_string)

with open('plik.json','r') as plik:
    osoba = Osoba(**json.loads(plik.read()))
    print(osoba.imie, osoba.wiek)
