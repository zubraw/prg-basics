import tv  

def main():
    
    my_tv = tv.TV()

    
    print("Show TV status")
    print(my_tv.show_status())

    # Turn the TV on
    print("Turn TV on")
    print(my_tv.turn_on())

    
    print(my_tv.show_status())

    
    print("Turn TV off")
    print(my_tv.turn_off())


    print(my_tv.show_status())

if __name__ == "__main__":
    main()