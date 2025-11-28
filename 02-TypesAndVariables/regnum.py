###
# Vehicle registration numbers 
# in Krakow start
# with the letters KR or KK. 
# Write a program that checks
# whether the vehicle registration number
#  entered
# from the keyboard means a 
# vehicle from Krakow.
# Print True whether a car is 
# from Krakow or False otherwise.
#


def regnum(reg):
    is_krakow = reg[0:2] == 'KR' or reg[0:2] == 'KK'
    print(f'Car is from Krakow: {is_krakow}')
reg = input('Enter car registration: ')
regnum(reg)