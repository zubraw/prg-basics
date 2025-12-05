def f(name):
    first_letters = ''
    words = name.split()
    for i in words:
        first_letters = first_letters + i[0]
    return first_letters
f("Internet of Things")
        
