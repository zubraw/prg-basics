def f(time1, time2):
    godzina1 = time1[0:2]
    godzina2 = time2[0:2]
    godzina1 = int(godzina1)
    godzina2 = int(godzina2)
    minuta1 = time1[3:5]
    minuta2 = time2[3:5]
    minuta1 = int(minuta1)
    minuta2 = int(minuta2)
    if godzina1 < godzina2:
        return time1
    elif godzina1 > godzina2:
        return time2
    elif godzina1 == godzina2:
        if minuta1 < minuta2:
            return time1
        elif minuta1 > minuta2:
            return time2
        elif minuta1 == minuta2:
            return 0
