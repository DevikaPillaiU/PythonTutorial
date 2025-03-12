from math import pi

def calculate_area_perimeter(radius):
    circle_area = pi * radius ** 2
    circle_perimeter = 2 * pi * radius
    return f"Area is: {circle_area:.2f} & Perimeter is: {circle_perimeter:.2f}"

radius = int(input("Enter the radius of the circle: "))
result = calculate_area_perimeter(radius)
print(result)
