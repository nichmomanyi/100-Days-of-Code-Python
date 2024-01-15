# import colorgram
import turtle as t
import random
# colors = colorgram.extract('img.jpg', 30)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.b
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
t.colormode(255)
tim = t.Turtle()
color_list = [(199, 117, 117), (212, 215, 215), (125, 24, 24), (223, 228, 228), (167, 56, 56), (186, 52, 52), (6, 83, 83), (108, 85, 85), (112, 175, 175), (21, 174, 174), (63, 138, 138), (39, 35, 35), (76, 48, 48), (9, 47, 47), (90, 52, 52), (182, 79, 79), (131, 41, 41), (141, 156, 156), (210, 149, 149), (179, 186, 186), (173, 159, 159), (212, 176, 176), (151, 119, 119), (177, 203, 203), (206, 190, 190), (37, 84, 84), (45, 63, 63), (48, 80, 80)]

tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.forward(300)
tim.setheading(0)
num_of_dots = 100
tim.speed("fastest")

for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen = t.Screen()
screen.exitonclick()