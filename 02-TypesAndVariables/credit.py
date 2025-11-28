def card(num):
    characters = len(num)
    if characters == 16:
        num = num[:4]+'**********'+num[-2:]
        print(f'Your credit card number is: {num}')
    else:
        print('Your credit card number should have 16 characters')
num = input('Credit card number:')
card(num)

