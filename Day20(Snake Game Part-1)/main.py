from turtle import Turtle, Screen

# from turtles import segments
from snake import Snake

import time

# Screen Creation
screen = Screen()
# Turning off tracer
screen.tracer(0)
#Setting Screen Width
screen.setup(width=600,height=600)

# Setting Background Color
screen.bgcolor("black")

#Setting Title of the Screen
screen.title("My Snake Game")

# Logic for Snake Game
game_is_on=True

# Create Snake as an instance of Class
snake = Snake()
# Listening to keypress
screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

# Exit Screen
screen.exitonclick()