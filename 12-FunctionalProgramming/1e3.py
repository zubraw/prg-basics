speed= int(input('Enter the speed(m/s): '))

convert = lambda x: round(x*3.6)

print(f'{speed} m/s = {convert(speed)} km/h')