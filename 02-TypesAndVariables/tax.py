###
# People up to and including 26 years of age are exempt
# from paying taxes in Poland. Write a program that,
# based on the person's age entered from the keyboard,
# prints True if the person is exempt from paying taxes
# and prints False otherwise.
#
def tax(age):
    no_tax = age < 26
    if no_tax == True:
        print(f'Exemption from paying taxes: {no_tax}')
    else:
        print(f'Exemption from paying taxes: {no_tax}... You have to pay lil bro')
    
age = int(input('Enter your age: '))
tax(age)
