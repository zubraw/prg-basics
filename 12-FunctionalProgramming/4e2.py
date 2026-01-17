measures = [48,47,54,50,42,68,39,46]

too_high = list(filter(lambda x: x>50, measures))
print(too_high)

print('Recorded values: ',end='')
n=1
for i in measures:
    if n!=len(measures):
        print(i,end=', ')
        n+=1
    else:
        print(i)

print('Speed too high: ',end='')
n1=1
for i in too_high:
    if n1!=len(too_high):
        print(i,end=', ')
        n1+=1
    else:
        print(i)