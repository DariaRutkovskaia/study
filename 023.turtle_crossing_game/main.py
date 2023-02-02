import time
from turtle import Screen

from car import Car
from player import Player
from scoreboard import Scoreboard

time_speed = 0.1
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

    if player.is_on_finish_line():
        player.go_to_start()
        car.create_more_cars()
        board.level_up()

    for any_car in car.car_list[1:]:
        if any_car.distance(player) <= 20:
            game_is_on = False
            board.game_over()

screen.exitonclick()
