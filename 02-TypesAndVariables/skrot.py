def skrot(uniwersytet):
    words = uniwersytet.split() #dziele nazwe na słowa
    skrot = "".join(word[0].upper() for word in words) #pętla która wypisuje wielkie pierwsze litery z kazdego słowa
    print(skrot)
    
    
uniwersytet = input('Nazwa uniwersytetu: ')
skrot(uniwersytet)