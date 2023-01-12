from random import randint
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_guess = screen.textinput(title='Make your bet', prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "Royalblue", "blue", "purple"]


def the_race(name_list):
    while True:
        for index in range(7):
            name_list[index].forward(randint(1, 10))
            if name_list[index].xcor() >= 230:
                return name_list[index].pencolor()


y = 160
turtles = []

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y)
    y -= 50
    turtles.append(new_turtle)

the_winner = the_race(turtles)
if user_guess.lower() == the_winner.lower():
    print(f"You win!! The winner is {the_winner}")
else:
    print(f"You lose!! The winner is {the_winner}")
screen.exitonclick()
