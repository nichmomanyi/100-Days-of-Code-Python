import turtle
from turtle import Turtle, Screen

tim = Turtle()
import random

# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("blue")
# timmy_the_turtle.right(60)
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(10):
#     tim.forward(10)
#     tim.color('white')
#     tim.forward(10)
#     tim.color('black')

# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# num_sides = 2
# while num_sides <=10:
#     num_sides += 1
#     for _ in range (num_sides):
#         angle = 360 / num_sides
#         tim.forward(100)
#         tim.right(angle)

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# directions = [0, 90, 180, 270]
# tim.pensize(10)
# tim.speed('fastest')
#
# for _ in range(200):
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#     tim.color(random_color())

tim.speed("fastest")
def spiro(gap):
    for _ in range(int(360/gap)):
        tim.color(random_color())
        tim.circle(50)
        tim.setheading(tim.heading() + gap)
spiro(5)


screen = Screen()
screen.exitonclick()
