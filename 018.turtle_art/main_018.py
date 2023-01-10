# import colorgram
# colors = colorgram.extract("image.jpg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import turtle as t
from random import choice

color_list = [(139, 168, 195), (206, 154, 121), (192, 140, 150), (25, 36, 55), (58, 105, 140), (145, 178, 162),
              (151, 68, 58), (137, 68, 76), (229, 212, 107), (47, 36, 41), (145, 29, 36), (28, 53, 47), (55, 108, 89),
              (228, 167, 173), (189, 99, 107), (139, 33, 28), (194, 92, 79), (49, 40, 36), (228, 173, 166),
              (20, 92, 69), (177, 189, 212), (29, 62, 107), (113, 123, 155), (172, 202, 190), (51, 149, 193),
              (166, 200, 213)]
tim = t.Turtle()
my_screen = t.Screen()
t.colormode(255)
tim.speed(0)
tim.hideturtle()
tim.penup()
step_y = -225
for _ in range(10):
    tim.setposition(-225, step_y)
    for _ in range(10):
        tim.forward(50)
        tim.dot(20, choice(color_list))
    step_y += 50
my_screen.exitonclick()
