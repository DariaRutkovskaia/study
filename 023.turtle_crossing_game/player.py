from turtle import Turtle

START_POSITION = (0, -270)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(START_POSITION)

    def go(self):
        self.forward(10)

    def go_to_start(self):
        self.goto(START_POSITION)

    def is_on_finish_line(self):
        if self.ycor() > 280:
            return True
