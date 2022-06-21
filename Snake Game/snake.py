from turtle import Turtle

DISTANCE = 20
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    # Step 1: Create snake body
    def create_snake(self):
        for position in START_POSITION:
            self.add_snake(position)

    def add_snake(self, position):
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.snake_segments.append(new_snake)

    def extend_snake(self):
        self.add_snake(self.snake_segments[-1].position())

    # Step 2: Move the snake
    def move_snake(self):
        for snakes in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[snakes - 1].xcor()
            new_y = self.snake_segments[snakes - 1].ycor()
            self.snake_segments[snakes].goto(new_x, new_y)
        self.head.forward(DISTANCE)

    # Step 3: Control the snake movements
    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    # End of Step 3
