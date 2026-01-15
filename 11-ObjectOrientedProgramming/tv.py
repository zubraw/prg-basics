class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0
    def turn_off(self):
        self.is_on = False
    def turn_on(self):
        self.is_on = True
    
    def set_channel(self, num):
        self.channel_no = num
        
    def set_channels(self, channel_list):
        self.channels = channel_list

    def show_channels(self):
        if not self.channels:
            print('Not available channels.')
        else:
            print('Available channels:')
            i=1
            for channel in self.channels:
                print(f'{i}. {channel}')
                i+=1
    
    def volume_up(self):
        if self.volume != 10:
            self.volume += 1
        else:
            self.volume = 10
    
    def volume_down(self):
        if self.volume != 0:
            self.volume -= 1
        else:
            self.volume = 0
        
    
    def show_status(self):
        if self.is_on:
            if self.channel_no >=1 and self.channel_no <= len(self.channels):
                channel_name = self.channels[self.channel_no-1]
                return f'TV is  on, channel {self.channel_no} ({channel_name})\nCurrent volume: {self.volume}'
            else:
                return f'TV is on, channel no. {self.channel_no}\nCurrent volume: {self.volume}'
        else:
            return 'TV is off'
        
    