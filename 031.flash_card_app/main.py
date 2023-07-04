BACKGROUND_COLOR = "#B1DDC6"
from random import choice
from tkinter import *

import pandas


def flip_card():
    global current_card
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(card_title, text="Russian", fill="white")
    canvas.itemconfig(card_word, text=current_card["Russian"], fill="white")


def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_image, image=card_front_image)
    canvas.itemconfig(card_title, text="Finnish", fill="black")
    canvas.itemconfig(card_word, text=current_card["Finnish"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    global current_card
    to_learn.remove(current_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    new_card()


window = Tk()
window.title("Finnish Flashcards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
current_card = {}
flip_timer = window.after(3000, func=flip_card)
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/fi-ru.csv")
finally:
    to_learn = data.to_dict(orient="records")

card_back_image = PhotoImage(file="images/card_back.png")

canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file="images/card_front.png")
card_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))

card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=new_card)
unknown_button.grid(row=1, column=0)
new_card()
window.mainloop()
