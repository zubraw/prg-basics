def f(amount):
    if amount % 5 == 0:
        piec = amount/5
        dwa = 0
        jeden = 0
    else:
        x = amount % 5
        piec = (amount - x) / 5
        if x % 2 == 0:
            dwa = x/2
            jeden = 0
        else:
            y = x % 2
            dwa = (x - y) / 2
            jeden = y
    piec = int(piec)
    dwa = int(dwa)
    jeden = int(jeden)
    print(f'Amount: {amount}')
    print(f'5 PLN coins: {piec}')
    print(f'2 PLN coins: {dwa}')
    print(f'1 PLN coins: {jeden}')
f(28)
    