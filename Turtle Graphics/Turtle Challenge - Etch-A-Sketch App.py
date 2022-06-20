import random
from turtle import Turtle, Screen

screen = Screen()

# Set the size and position of the main window.
screen.setup(width=500, height=400)

# Pop up a dialog window for input of a string.
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "blue", "yellow", "green", "purple"]

y_pos = [-100, -70, -40, -10, 20, 50]
all_turtles = []
is_race_on = False

for turtle_index in range(0, 6):
    # Create turtle objects and Set turtle shape
    new_turtle = Turtle(shape="turtle")
    # Set turtle color
    new_turtle.color(colors[turtle_index])
    # Pull the pen up – no drawing when moving
    new_turtle.penup()
    # Move turtle to an absolute position.
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    # Appending all new turtles to a list
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for each_turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        each_turtle.forward(rand_distance)
        if each_turtle.xcor() == 230:
            is_race_on = False
            winner_turtle = each_turtle.pencolor()
            print(f'User bet on: {user_bet}')
            if winner_turtle == user_bet:
                print(f"You've won !! The {winner_turtle} turtle is winner...")
            else:
                print(f"You've lost !! The {winner_turtle} turtle is winner...")

screen.exitonclick()
