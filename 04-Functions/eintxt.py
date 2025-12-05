def counter(letter, text):
    count = 0
    for char in text:
        if char == letter:
            count = count + 1
    print(text)
    print(f'The number of letter "{letter}": {count}')
letter = 'e'
text = 'You never get a second chance to make a first impression'
counter(letter,text)