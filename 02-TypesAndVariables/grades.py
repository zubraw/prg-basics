###
# A program that calculates and prints
# the average grade of a student
#

def grades(math,art,music,history):
    average = (math + art + music + history)/4
    print(f'Average grade is: {average}')

print('Enter your grades!')
math = float(input('Math: '))
art = float(input('Art: '))
music = float(input('Music: '))
history = float(input('History: '))
grades(math,art,music,history)