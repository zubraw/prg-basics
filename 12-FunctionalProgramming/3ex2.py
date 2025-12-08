text = 'I completely agree with you'
arr = text.split()
f = lambda x: len(x)
print(list(map(f,arr)))