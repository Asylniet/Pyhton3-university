class Shape():
    def __init__(self):
        pass

    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,_length, _width):
        Shape.__init__(self)
        self.length = _length
        self.width = _width

    def area(self):
        return self.length * self.width

rectangleArea = Rectangle(3, 5)
print(rectangleArea.area())