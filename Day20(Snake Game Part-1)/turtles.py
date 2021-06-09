from turtle import Turtle

segments=[]

position=[(0,0),(-20,0),(-40,0)]


for i in range(0,3):
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position[i])
    segments.append(new_segment)


