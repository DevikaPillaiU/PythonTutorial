import turtle

def draw_hexagon(side_length):
    for _ in range(6):
        turtle.forward(side_length)
        turtle.right(60)

def draw_radial_pattern(hex_size, num_hexagons):
    for _ in range(num_hexagons):
        draw_hexagon(hex_size)
        turtle.right(360 / num_hexagons)

turtle.speed(0.5)
draw_radial_pattern(50, 10)

turtle.done()
