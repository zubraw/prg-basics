def f(number):
    digits = str(number)
    sum = 0
    for i in digits:
        if digits.count(i) > 1:
            sum = sum + int(i)
    print(sum)
f(3332)