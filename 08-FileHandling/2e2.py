seven_wonders = [
   "Great Wall of China",
   "Petra",
   "Christ the Redeemer",
   "Machu Picchu",
   "Chichen Itza",
   "Roman Colosseum",
   "Taj Mahal"
]

file = 'sev_wonders.txt'

wonder_sorted = sorted(seven_wonders)

with open(file,'w') as file:
    for item in wonder_sorted:
        file.write(f'{item}\n')