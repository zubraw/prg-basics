def ms_to_kmh(ms):
    convert = lambda x: x*3.6
    result = convert(ms)
    print(f'{ms} m/s = {result} km/h')
ms_to_kmh(int(input('Enter speed: ')))
