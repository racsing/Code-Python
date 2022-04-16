from turtle import Turtle, Screen
import random

tim = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

for i in range(3,11):
    angle = (360 / i)
    tim.color(random.choice(colours))
    for j in range(i):
        tim.forward(100)
        tim.right(angle)

screen = Screen()
screen.exitonclick()