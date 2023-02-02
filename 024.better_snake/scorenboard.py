from turtle import Turtle

ALLIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.goto(0, 270)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("high_score.txt", mode="r") as file:
            self.high_score = file.read()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALLIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALLIGNMENT, font=FONT)

    def reset_score(self):
        with open("high_score.txt", mode="r") as file:
            self.high_score = file.read()
            if self.score > int(self.high_score):
                with open("high_score.txt", mode="w") as data:
                    self.high_score = data.write(str(self.score))
            self.score = 0
            self.update_scoreboard()
