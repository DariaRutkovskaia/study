from turtle import Turtle
ALLIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.goto(x_pos, 280)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALLIGNMENT, font=FONT)

    def increase(self):
        self.score +=1
        self.update()