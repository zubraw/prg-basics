###
# Write a program that calculates and prints
# the income of a family per person. To print the results
# in a readable form, use f-strings.
#

def income(father_income,mother_income,family_members):
    total_income = father_income + mother_income
    income_per_person = total_income/family_members
    print(f'Total family income is {total_income}, and income per person is {income_per_person}')

father_income = float(input('What is the fathers income?: '))
mother_income = float(input('What is the mothers income?: '))
family_members = int(input('Family members: '))
income(father_income,mother_income,family_members)