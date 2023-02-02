import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
# from scoreboard import Scoreboard

LEFT_START = (-370, 0)
RIGHT_START = (370, 0)
B_START = (0, -300)
# LEFT_SCORE = -100
# RIGHT_SCORE = 100
time_speed = 0.1

#
# def update_the_screen():
#     global time_speed
#     time_speed = 0.1
#     ball.refresh()
#     l_puddle.goto(LEFT_START)
#     r_puddle.goto(RIGHT_START)


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
# l_score = Scoreboard(LEFT_SCORE)
# r_score = Scoreboard(RIGHT_SCORE)

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

    elif ball.distance(r_puddle) <= 25 or ball.distance(l_puddle) <= 25:
        ball.bounce_x()

    if ball.xcor() >= 390 :
        game_is_on = False
#     elif ball.xcor() <= -390:
#
# screen.exitonclick()
