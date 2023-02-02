import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

## How we can get state's coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


def get_coordinates(name_of_state):
    new_x = int(data[data.state == name_of_state].x)
    new_y = int(data[data.state == name_of_state].y)
    return new_x, new_y


def print_state_name(position, name):
    printer = turtle.Turtle()
    printer.hideturtle()
    printer.penup()
    printer.goto(position)
    printer.write(f"{name}", align="center")


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
answer_state = screen.textinput(title=f"Guess The State",
                                prompt="What's another state name?").title()
while len(guessed_states) < 50:
    if answer_state == "Exit":
        states_to_learn = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        new_pos = get_coordinates(answer_state)
        print_state_name(new_pos, answer_state)
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 correct states",
                                    prompt="What's another state name?").title()


