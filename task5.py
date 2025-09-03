from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.radius = r
        
    def area(self):
        return 3.14 * self.radius * self.radius
        
class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def area(self):
        return self.a * self.b
        
c = Circle(5)
r = Rectangle(4, 6)
print(c.area())
print(r.area())