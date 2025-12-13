def f(player1,player2):
    
    value1=0
    for char in player1:
        if char in ['A','K','Q','J','T']:
            num=10
        elif char in ['1','2','3','4','5','6','7','8','9']:
            num=int(char)
        else:
            continue
        value1+= num
    print(value1)
    value2=0
    for char in player2:
        if char in ['A','K','Q','J','T']:
            num=10
        elif char in ['1','2','3','4','5','6','7','8','9']:
            num=int(char)
        else:
            continue
        value2+=num
    print(value2)
        
    
    if value1>=value2:
        print('True')
    else:
        print('False')
f("AJ972","AQT72")

        
