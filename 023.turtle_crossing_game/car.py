from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "Royalblue", "blue", "purple"]
START_X = 280


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.start_y = randint(-240, 240)
        self.start_x = randint(-270, 270)
        self.penup()
        self.shape("square")
        self.color(choice(COLORS))
        self.setheading(180)
        self.turtlesize(stretch_wid=1, stretch_len=2)
        self.goto(self.start_x, self.start_y)
        self.car_list.append(self)

    def moving(self):
        if self.xcor() > -280:
            new_x = self.xcor() - 10
            self.goto(new_x, self.ycor())
        else:
            self.refresh()

    def create_more_cars(self):
        new_car = Car()
        self.car_list.append(new_car)

    def flow(self):
        for new_car in self.car_list:
            new_car.moving()

    def refresh(self):
        new_y = randint(-240, 240)
        self.goto(START_X, new_y)
        self.color(choice(COLORS))
