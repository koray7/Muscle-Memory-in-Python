from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=800)
screen.title("PingPong")
screen.tracer(0)

r_paddle = Paddle((470, 0))
l_paddle = Paddle((-480, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

# Detect collision with walls
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()

    if ball.distance(r_paddle) < 30 and ball.xcor() > 400 or ball.distance(l_paddle) < 30 and ball.xcor() < -400:
        ball.bounce_x()

# Passing the walls
    if ball.xcor() > 500:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -500:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()