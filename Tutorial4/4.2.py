class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

# Example usage
rect = Rectangle(5, 3)
print("Area of rectangle:", rect.area())

