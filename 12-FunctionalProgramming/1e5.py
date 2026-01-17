distance = int(input('Enter distance in km: '))
hours = float(input('Enter number of travel hours: '))
minutes = float(input('Enter number of travel minutes: '))

avg_speed = lambda x,y,z: round(x/(y+(z/60)),1)

print(f'Average speed: {avg_speed(distance,hours,minutes)}')