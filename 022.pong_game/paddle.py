from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, start_position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.setposition(start_position)

    def up(self):
        if self.ycor() < 250:
            self.forward(20)

    def down(self):
        if self.ycor() > -250:
            self.backward(20)

    def border(self):
        self.hideturtle()
        self.shapesize(stretch_wid=0.1, stretch_len=2)
        self.goto(0, -300)
        self.setheading(90)
        self.pensize(10)
        for _ in range(6):
            self.forward(50)
            self.stamp()
            self.forward(50)

