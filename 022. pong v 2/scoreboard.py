from turtle import Turtle

ALLIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 280)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score_r = 0
        self.score_l = 0
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score_l}    Score: {self.score_r}", align=ALLIGNMENT, font=FONT)

    def increase_right(self):
        self.score_r += 1
        self.update()

    def increase_left(self):
        self.score_l += 1
        self.update()
