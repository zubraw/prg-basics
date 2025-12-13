translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}

word = input('Word to translate: ')
if word in translations:
    print(f'{word} is {translations[word]} in polish')
else:
    print('There is no available translation')