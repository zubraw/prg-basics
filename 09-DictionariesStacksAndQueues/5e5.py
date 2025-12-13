paragraph = "cat dog mouse cat rat cat mouse"
splited_p = paragraph.split()
counts = {}

for word in splited_p:
    if word in counts:
        counts[word] +=1
    else:
        counts[word] = 1
print(counts)