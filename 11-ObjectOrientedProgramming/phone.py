class Phone:
    def __init__(self, model, mark, battery):
        self.model = model
        self.mark = mark
        self.battery = battery
        self.is_on = False
    
    def on(self):
        if self.battery > 0:
            self.is_on = True
    
    def off(self):
        if self.battery == 0:
            self.is_on = False

    def phone_info(self):
        print(f'My phones mark is {self.mark}')
        print(f'My phones model is {self.model}')
        if self.is_on:
            print(f'The actual baterry status is {self.battery}% so phone is on')
        else:
            print('Unfortunately my phone dead...')
    
def main():
    my_phone = Phone('iPhone 17', 'Apple', 1)

    my_phone.on()
    my_phone.off()
    my_phone.phone_info()
if __name__ == '__main__':
    main()
