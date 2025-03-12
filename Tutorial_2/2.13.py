import math

def calc_circle_area(r):
    if r < 0:
        return "Radius cannot be negative"
    
    area = math.pi * r ** 2
    return area


radius_input = float(input("Enter the radius of the circle: "))

print(f"Area of the circle: {calc_circle_area(radius_input):.2f}")
