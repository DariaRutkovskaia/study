from random import choice
from turtle import Turtle

START_ANGLES = [45, 135, 225, 315]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create()

    def move(self):
        if self.ycor() >= 280:
            if self.heading() == 45:
                self.right(90)
            elif self.heading() == 135:
                self.left(90)
        elif self.ycor() <= -280:
            if self.heading() == 225:
                self.right(90)
            elif self.heading() == 315:
                self.left(90)
        self.forward(10)

    def create(self):
        random_angle = choice(START_ANGLES)
        self.penup()
        self.shape("square")
        self.color("white")
        self.settiltangle(random_angle)
        self.right(random_angle)

    def refresh(self):
        self.home()
        self.create()
