"""
    Step 1: Create a Snake body
    Step 2: Move the snake
    Step 3: Control the snake movements
    Step 4: Detect Collision with Food
    Step 5: Create a Scoreboard
    Step 6: Detect Collision with wall
    Step 7: Detect Collision with tail
"""

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Screen settings
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Snake Object
snake = Snake()

# Food Object
food = Food()

# ScoreBoard object
scoreboard = ScoreBoard()

# Snakes movement on Key Strokes
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")

# Screen Refresh
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # Step 4: Detect Collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    # Step 6: Detect Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Step 7: Detect Collision with tail
    for sn in snake.snake_segments[1:]:
        if snake.head.distance(sn) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
