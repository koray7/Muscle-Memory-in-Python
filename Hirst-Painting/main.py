import random

import colorgram
import turtle as T
# *************-Extract colors-******************
# colors = colorgram.extract('IMG.jpg', 30)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

# ******************************************************
color_list = [(243, 237, 222), (242, 233, 239), (231, 241, 236), (191, 165, 116), (139, 166, 189), (59, 101, 137), (138, 90, 53), (13, 23, 53), (221, 206, 125), (60, 23, 12), (181, 146, 165), (178, 152, 47), (142, 176, 150), (74, 116, 82), (61, 15, 26), (124, 80, 101), (16, 38, 25), (127, 32, 18), (25, 52, 124), (178, 188, 215), (110, 34, 48), (162, 106, 135), (98, 149, 102), (96, 122, 172), (209, 180, 195), (171, 106, 95), (172, 205, 181), (77, 148, 163), (26, 89, 64)]
random_color = random.choice(color_list)

lily = T.Turtle()
lily.shape("turtle")
lily.color("Blue")
T.colormode(255)
lily.speed("fastest")
lily.penup()
lily.hideturtle()

lily.setheading(225)
lily.forward(300)
lily.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    lily.dot(20, random.choice(color_list))
    lily.forward(50)

    if dot_count % 10 == 0:
        lily.setheading(90)
        lily.forward(50)
        lily.setheading(180)
        lily.forward(500)
        lily.setheading(0)



screen = T.Screen()
screen.exitonclick()