class Square:
    def __init__(self, a):
        self.a = a
    def area(self):
        return self.a**2
    def answer(self):
        print('Square with side', self.a, ':')
        print('Area is', self.area(), 'Perimeter is', self.a*4)

square1 = Square(4)
square2 = Square(5)
square3 = Square(6)
square1.answer()
square2.answer()
square3.answer()


