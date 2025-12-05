def f(palindrome):
    backwards = ''
    is_it = False
    for i in palindrome:
        backwards = i + backwards
    if palindrome == backwards:
        is_it = True
    print(is_it)
f("radar")