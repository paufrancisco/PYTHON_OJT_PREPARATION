class Shape:
    def area(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius **2
    
class Rectangle(Shape):
    def __init__(self,side1 , side2):
        self.side1 = side1
        self.side2 = side2
    def area(self):
        return (self.side1)*(self.side2)
    

# Creating objects of the derived classes
circle = Circle(5)
rectangle = Rectangle(4, 6)

    
shapes = [circle, rectangle]
for shape in shapes:
    print(f"Area: {shape.area()}")