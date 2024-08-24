import random
from turtle import Turtle, Screen

new_turtle = Turtle()
screen = Screen()
is_race_on = False
screen.setup(width=600, height=600)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-90, -60, -30, 0, 30, 60]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-280, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 280:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've Won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've Lost. The {winning_color} turtle is the winner.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()

