class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self,_length = 0):
        Shape.__init__(self)
        self.length = _length

    def area(self):
        return self.length * self.length

Asqr = Square(int(input()))
print(Asqr.area())