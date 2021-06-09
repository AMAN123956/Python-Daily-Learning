<<<<<<< HEAD
from turtle import Turtle,Screen

my_turtle = Turtle()

# Different Shape
def draw_shape(num_side):
    angle = 360/num_side
    for _ in range(num_side):
        my_turtle.forward(100)
        my_turtle.right(angle)
        

def select_shape():
    for side in range(3,11):
        draw_shape(side)

select_shape()


# Exit Screen on Click
screen = Screen()
screen.exitonclick()
=======
from turtle import Turtle,Screen

my_turtle = Turtle()

# Different Shape
def draw_shape(num_side):
    angle = 360/num_side
    for _ in range(num_side):
        my_turtle.forward(100)
        my_turtle.right(angle)
        

def select_shape():
    for side in range(3,11):
        draw_shape(side)

select_shape()


# Exit Screen on Click
screen = Screen()
screen.exitonclick()

