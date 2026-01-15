def f(first_letter, last_letter):
    with open('data.txt','r',encoding='utf-8') as file:
        content = file.read()
    words = content.split()
    counter = 0
    for word in words:
        if word[0] == first_letter and word[-1] == last_letter:
            counter+=1
        else:
            continue
    return counter
print(f('w','d'))