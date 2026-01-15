class Czlowiek:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek
    def przedstawsie(self, powitanie = 'Cześć'):
        return powitanie + ', mam na imie ' + self.imie + ' lat: ' + str(self.wiek)
    
obiekt = Czlowiek('Sebastian', 24)
print(obiekt.przedstawsie('Witam'))
obiekt2 = Czlowiek('Krystian', 18)
print(obiekt2.przedstawsie())