from turtle import Turtle

position=[(0,0),(-20,0),(-40,0)]
distance=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()
        
    def create_snake(self):
        for i in range(0,3):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position[i])
            self.segments.append(new_segment)    
    
    def move_snake(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_x=(self.segments[seg-1]).xcor()
            new_y=(self.segments[seg-1]).ycor()
            self.segments[seg].goto(new_x,new_y)  

        self.segments[0].forward(distance)
    

    def up(self):
        if self.segments[0].heading() !=DOWN:
            self.segments[0].setheading(UP)
        
    
    def down(self):
        if self.segments[0].heading() !=UP:
            self.segments[0].setheading(DOWN)
        
    
    def left(self):
        if self.segments[0].heading() !=RIGHT:
            self.segments[0].setheading(LEFT)
        

    def right(self):
        if self.segments[0].heading() !=LEFT:
            self.segments[0].setheading(RIGHT)
        


