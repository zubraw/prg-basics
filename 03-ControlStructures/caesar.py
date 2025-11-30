def f(plain_text):
    encrypted = ''

    for char in plain_text:
        char = ord(char)
        #print(char)
        char = char + 1
        char = chr(char)
        encrypted = encrypted + char
    print(f'Plain text: {plain_text}')
    print(f'Encrypted text: {encrypted}')
f('The early bird catches the worm')
