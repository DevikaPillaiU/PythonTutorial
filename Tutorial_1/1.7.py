def quadrant(x_coord, y_coord):
    if x_coord > 0 and y_coord > 0:
        return "Quadrant 1 (Top-Right)"
    elif x_coord < 0 and y_coord > 0:
        return "Quadrant 2 (Top-Left)"
    elif x_coord < 0 and y_coord < 0:
        return "Quadrant 3 (Bottom-Left)"
    elif x_coord > 0 and y_coord < 0:
        return "Quadrant 4 (Bottom-Right)"
    elif x_coord == 0 and y_coord == 0:
        return "Origin (0,0)"
    elif x_coord == 0:
        return "Y-axis"
    else:
        return "X-axis"

x_coord = float(input("Enter the x-coordinate: "))
y_coord = float(input("Enter the y-coordinate: "))

print(quadrant(x_coord, y_coord))
