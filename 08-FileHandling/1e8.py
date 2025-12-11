def read_from_file(name):
    with open(name) as file:
        content = file.read()
    return content

filecontent = read_from_file('pets.txt')
wordsinfile = filecontent.split()

words = 0
for word in wordsinfile:
    words += 1
print(f'Total words: {words}')