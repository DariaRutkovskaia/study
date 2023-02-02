import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

LEFT_START = (-370, 0)
RIGHT_START = (370, 0)
B_START = (0, -300)
time_speed = 0.1


def update_the_screen():
    global time_speed
    time_speed *= 0.9
    ball.refresh()
    l_puddle.goto(LEFT_START)
    r_puddle.goto(RIGHT_START)


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

r_puddle = Paddle(RIGHT_START)
l_puddle = Paddle(LEFT_START)
border = Paddle(B_START)
ball = Ball()
border.border()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_puddle.up, "Up")
screen.onkey(r_puddle.down, "Down")
screen.onkey(l_puddle.up, "w")
screen.onkey(l_puddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(time_speed)
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    elif ball.distance(r_puddle) <= 30 and ball.xcor() >= 350 or \
            ball.distance(l_puddle) <= 30 and ball.xcor() <= -350:
        ball.bounce_x()

    if ball.xcor() >= 390:
        update_the_screen()
        scoreboard.increase_left()

    if ball.xcor() <= -390:
        update_the_screen()
        scoreboard.increase_right()

screen.exitonclick()
