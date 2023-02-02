from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed(0)
        self.color("royalblue")
        self.refresh()

    def refresh(self):
        random_x = randint(-14, 14,)
        random_y = randint(-14, 14)
        self.goto(random_x*20, random_y*20)
