import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

LEFT_START = (-370, 0)
RIGHT_START = (370, 0)
B_START = (0, -300)
LEFT_SCORE = -100
RIGHT_SCORE = 100
time_speed = 0.1


def update_the_screen():
    global time_speed
    time_speed = 0.1
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
l_score = Scoreboard(LEFT_SCORE)
r_score = Scoreboard(RIGHT_SCORE)

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

    if ball.distance(r_puddle) <= 60 and ball.xcor() >= 340 or ball.distance(l_puddle) <= 60 and ball.xcor() <= -340:
        time_speed *= 0.9
        if ball.heading() == 315 or ball.heading() == 135:
            ball.right(90)
        elif ball.heading() == 45 or ball.heading() == 225:
            ball.left(90)
    elif ball.xcor() >= 400:
        l_score.increase()
        update_the_screen()
    elif ball.xcor() <= -400:
        r_score.increase()
        update_the_screen()

screen.exitonclick()
