class Rectangle:
    def __init__(self, height, width, corner_x, corner_y):
        self.height = height
        self.width = width
        self.corner_x = corner_x
        self.corner_y = corner_y

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

    def find_center(self):
        center_x = self.corner_x + self.width / 2
        center_y = self.corner_y + self.height / 2
        return (center_x, center_y)  

# Instantiating the class
rect1 = Rectangle(10, 20, 0, 0)

print("Area:", rect1.area())
print("Perimeter:", rect1.perimeter())
print("Center:", rect1.find_center())
