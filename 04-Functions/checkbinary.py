def f(binary_number):
    for num in binary_number:
        if num != '0' and num != '1':
            is_binary = False
            break
        else:
            is_binary = True
    print(f'{binary_number} is a binary number: {is_binary}')
f('100101')
