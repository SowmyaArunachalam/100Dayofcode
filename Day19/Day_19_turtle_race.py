from turtle import Turtle, Screen
import random
screen = Screen ( )
screen.setup ( width = 500, height = 400 )
user_bet= screen.textinput ( title = "Make a bet", prompt = " Which turtle will win the race?Enter a colour:" )
colors=["red", "blue", "violet", "green", "brown", "yellow"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtle=[]
is_race_on=False
for index_turtle in range(6):
 new_turtle= Turtle ( )
 new_turtle.penup()
 new_turtle.goto(x=-230,y=y_positions[index_turtle])
 new_turtle.shape("turtle")
 new_turtle.color(colors[index_turtle])
 all_turtle.append(new_turtle)

if user_bet:
    is_race_on =True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() >230 :
            is_race_on = False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
               print ( f"You've won! The {winning_color} turtle is the winner!" )
            else:
               print ( f"You've lost! The {winning_color} turtle is the winner!" )
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)
screen.exitonclick ( )
