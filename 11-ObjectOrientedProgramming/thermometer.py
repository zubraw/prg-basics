import random
class Thermometer:
    def __init__(self):
        self.temperature = 0
        self.is_on = False
        self.comment = ''
    
    def on(self):
        self.is_on = True
    
    def off(self):
        self.is_on = False

    def measure(self):
        if self.is_on:
            self.temperature = (random.randint(340,420))/10
            if self.temperature <= 35.8:
                self.comment = '(Little too cold)'
            elif 35.8 < self.temperature < 37.0:
                self.comment = '(ok)'
            elif 37.0 <= self.temperature < 40.9:
                self.comment = '(fever)'
            elif self.temperature >=41:
                self.comment = '(CRITICAL TEMPERATURE!!)'
            else:
                self.comment=''
    
   
    def display(self):
        if self.is_on:
            return f'Thermometer is on\nTemperature: {self.temperature} {self.comment}'
        else:
            return 'Thermometer is off\n'

def main():
    my_thermometer = Thermometer()
    print(my_thermometer.display())
    my_thermometer.on()
    my_thermometer.measure()
    print(my_thermometer.display())
    my_thermometer.off()

if __name__ == '__main__':
    main()