###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#


import keyboard # your own defined module

# Reads employee's data from keyboard
first_name = input_string('Enter name: ')
last_name = input_string('Enter last name: ')
age = input_integer('Enter age: ')
salary = input_real('Enter salary: ')
is_salary_hidden = input_boolean('Hide salary? (y/n)')

# Prints employee's record
print('DATA RECORD')
print('===========')
print(f'Name: {first_name} {last_name}')
print(f'Age: {age}')
if is_salary_hidden:
    print('Salary is hidden')
else:
    print(f'Salary: {salary}')
    