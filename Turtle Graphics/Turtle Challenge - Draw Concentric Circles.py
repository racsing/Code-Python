import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)

# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()
color_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (223, 137, 176), (143, 108, 57),
              (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227),
              (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36),]

# radius of the circle
r = 10

# Loop for printing concentric circles
for i in range(20):
    tim.color(random.choice(color_list))
    tim.circle(r * i)
    tim.penup()
    tim.sety((r * i) * (-1))
    tim.pendown()

screen = Screen()
screen.exitonclick()
