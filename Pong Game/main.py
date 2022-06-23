"""
    Step 1: Create the Screen
    Step 2: Create & Move a paddle
    Step 3: Create another paddle
    Step 4: Create a ball and make it move
    Step 5: Detect collision with wall and bounce
    Step 6: Detect Collision with paddle
    Step 7: Detect when paddle misses
    Step 8: Keep Score
"""

from turtle import Screen
from paddle import Paddle

# Screen settings
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("green")
screen.title("Pong")

# To disable the animation
screen.tracer(0)

# Turtle object
paddle = Paddle()

screen.listen()
screen.onkey(paddle.go_up, "Up")
screen.onkey(paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
