###
# A program that checks whether the password length
# read from the keyboard is correct.
#

def passwd(password):
    if len(password) >= 8:
        print(f'Your password is valid: {len(password)} characters')
    else:
        print(f'Your password is too short: only {len(password)} characters')

password = input('Enter your password: ')
passwd(password)