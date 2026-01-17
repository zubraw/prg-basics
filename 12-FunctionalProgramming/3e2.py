text = input('Text: ')

result = list(map(lambda word: len(word), text.split()))

print(result)