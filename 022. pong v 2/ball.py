from random import choice
from turtle import Turtle




class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.x_step = 10
        self.y_step = 10

    def move(self):
        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_step *= (-1)

    def bounce_x(self):
        self.x_step *= (-1)


    # def create(self):


    # def refresh(self):
    #     self.home()
    #     self.create()
