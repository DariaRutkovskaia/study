from turtle import Turtle

FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-260, 260)
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_board()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over", align="center", font=FONT)
