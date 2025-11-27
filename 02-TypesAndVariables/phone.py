def number(phone_num):
    print(f'Enter phone number: {phone_num}')
    print(f'Phone number: {phone_num[0:3]}-{phone_num[3:6]}-{phone_num[6:9]}')

phone_num = input('Please enter your phone number: ')
number(phone_num)