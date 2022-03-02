import math

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def show(self):
        return self.x, self.y


    def move(self, x, y):
        self.x += x
        self.y += y


    def dist(self, pt):
        dx = pt.x - self.x
        dy = pt.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)

p1 = Point(0, 0)
p2 = Point(2, 2)
print(p1.show())
p1.move(1, 1)
print(p1.show())
print(p1.dist(p2))