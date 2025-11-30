##
#Write a program that allows you to 
# convert time in 24-hour format to 
# 12-hour format. The time in 24-hour 
# format (hh:mm) 
# is read from the keyboard.

def convert(time):
    hours = time[0:2]
    minutes = time[3:5]
    hours = int(hours)
    minutes = int(minutes)
    #print(hours)
    #print(minutes)
    if hours==0:
        print(f'{time} to w systemie 12 godzinnym: 00:{minutes}am')
    elif hours > 0 and hours<12:
        print(f'{time} to w systemie 12 godzinnym: {hours}:{minutes}am')
    elif hours >=12 and hours<24:
        print(f'{time} to w systemie 12 godzinnym: {hours}:{minutes}pm')
    elif hours < 0 or hours > 24 or minutes < 0 or minutes >= 60:
        print('Nie ma takiej godziny')
convert('01:22')