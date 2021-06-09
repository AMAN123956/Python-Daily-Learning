<<<<<<< HEAD
from turtle import Turtle,Screen
import random
screen = Screen()

is_race_on=False
# Setup Height and Width of Window
screen.setup(width=500,height=400)
# taking input from user
user_bet =  screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race?Enter Your Color:")
colors=["red","green","blue","yellow","purple","black"]
all_turtle=[]
def create_turtle(p1,p2,color):
    tim=Turtle(shape="turtle")
    tim.penup()
    tim.color(color)
    # To move Turtle to Start of Screen
    tim.goto(x=p1,y=p2)
    #Appending to a list
    all_turtle.append(tim)


y_positions=[20,60,100,-20,-60,-100]
for i in range(0,6):
    create_turtle(p1=-250, p2=y_positions[i], color=colors[i])

if user_bet:
    is_race_on=True


while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The following {winning_color} is the winner")
                is_race_on=False
            else:
                print(f"You lost The following {winning_color} is the winner")
                is_race_on=False
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)


=======
from turtle import Turtle,Screen
import random
screen = Screen()

is_race_on=False
# Setup Height and Width of Window
screen.setup(width=500,height=400)
# taking input from user
user_bet =  screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race?Enter Your Color:")
colors=["red","green","blue","yellow","purple","black"]
all_turtle=[]
def create_turtle(p1,p2,color):
    tim=Turtle(shape="turtle")
    tim.penup()
    tim.color(color)
    # To move Turtle to Start of Screen
    tim.goto(x=p1,y=p2)
    #Appending to a list
    all_turtle.append(tim)


y_positions=[20,60,100,-20,-60,-100]
for i in range(0,6):
    create_turtle(p1=-250, p2=y_positions[i], color=colors[i])

if user_bet:
    is_race_on=True


while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The following {winning_color} is the winner")
                is_race_on=False
            else:
                print(f"You lost The following {winning_color} is the winner")
                is_race_on=False
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)


>>>>>>> 15cd792293402f706cafa95b891709c8f33f1ed8
screen.exitonclick()