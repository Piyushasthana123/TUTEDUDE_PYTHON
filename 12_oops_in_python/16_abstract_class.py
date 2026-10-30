from my_abstact_class import Shape

class Square(Shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side**2

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

sq1 = Square(10)
print(sq1.area())

r1 = Rectangle(5,9)
print(r1.area())

c1 = Circle(5)
print(c1.area())