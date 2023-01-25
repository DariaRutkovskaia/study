import time
from turtle import Screen

from car import Car
from player import Player
from scoreboard import Scoreboard

START_POSITION = (0, -270)
time_speed = 0.2
screen = Screen()
board = Scoreboard()
screen.setup(width=600, height=600)
screen.bgcolor("LightGrey")
screen.title("Crossing game")
screen.tracer(0)
player = Player()
car = Car()
for _ in range(15):
    car.create_more_cars()
screen.listen()
screen.onkey(player.go, "Up")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(time_speed)
    car.flow()

    if player.ycor() >= 290:
        time_speed *= 0.9
        player.goto(START_POSITION)
        car.create_more_cars()
        board.level_up()

    for any_car in car.car_list[1:]:
        if any_car.distance(player) <= 20:
            game_is_on = False

screen.exitonclick()
