import tv
def main():
    my_tv = tv.TV()
    print(my_tv.show_status())
    my_tv.turn_on()
    print(my_tv.show_status())
    
    list_of_channels = ['TVP1','TVP2','Polsat','TVN','Filmbox','Discovery','Eleven Sport']
    my_tv.channels = list_of_channels
    
    my_tv.show_channels()
    my_tv.volume_up()
    print(my_tv.show_status())
    my_tv.volume_down()
    my_tv.volume_down()
    my_tv.set_channel(7)
    print(my_tv.show_status())

if __name__ == '__main__':
    main()
        