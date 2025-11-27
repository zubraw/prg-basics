#The number of people and percentage of 
# the total population living in the
#  Northern Hemisphere

#The number of people and percentage 
# of the total population living in 
# the Southern Hemisphere

def pop(north):
    total = 8000000000
    south = total - north
    print(f'World population: {total}')
    print(f'Population living in the Northern Hemisphere: {north}')
    print('Northern Hemisphere in %: ', north/total*100, " %")
    print(f'Population living in the Southern Hemisphere: {south}')
    print('Southern Hemisphere in %: ', south/total*100, ' %')

north = 7200000000
pop(north)
   