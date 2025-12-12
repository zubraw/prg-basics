file_name = input('Enter file name: ')
with open(file_name,'r') as file:
    content = file.read()
lines_content = content.splitlines()
words_content = content.split()

lines = 0
characters = 0
words = 0

for word in words_content:
    words+=1

for line in lines_content:
    lines+=1

for character in content:
    characters+=1

print(f'File name: {file_name}')
print(f'Number of lines: {lines}')
print(f'Number of characters: {characters}')
print(f'Number of words: {words}')