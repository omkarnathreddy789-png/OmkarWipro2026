from abc import ABC,abstractmethod
class Shape(ABC):
    def display(self):
        print("Normal method")
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def area(self):
        print("Rectangle area")

r=Rectangle()
r.area()
r.display()

