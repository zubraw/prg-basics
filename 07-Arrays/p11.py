#The weather station measures temperature once a day. 
# The measurement results for each day in March are stored in an array. Write a program that 
# analyzes the temperature based on the observations from March and prints the following report:
#TEMPERATURE REPORT
#Month: March
#Number of measurements:
#Average temperature in the month:
#Minimum temperature:
#Maximum temperature:
#Number of days with negative temperature:

temperatures = [
 3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
 4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
 -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
]
daynum = len(temperatures)
total = 0
negative = 0
for day in temperatures:
    total = total + day
    if day < 0:
        negative = negative + 1
average = total/daynum

mintemp = min(temperatures)
maxtemp = max(temperatures)

print('TEMPERATURE REPORT')
print('Month: March')
print(f'Number of measurements: {daynum}')
print(f'Average temperature in the month: {round(average)}')
print(f'Minimum temperature: {mintemp}')
print(f'Maximum temperature: {maxtemp}')
print(f'Number of days with negative temperature: {negative}')