###
# A program that, for a given speed in km/h,
# prints the speed in m/s
#
def f(speed_kmh):
    speed_ms = speed_kmh//3.6
    print(f'{speed_kmh} km/h = {speed_ms} m/s')
    
speed_kmh = 70
f(speed_kmh)

