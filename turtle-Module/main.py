from turtle import Turtle, Screen

tim = Turtle()

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


num_sides = 3
while num_sides <=10:
    num_sides += 1
    for _ in range (num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)






screen = Screen()
screen.exitonclick()