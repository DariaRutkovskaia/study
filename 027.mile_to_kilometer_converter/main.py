from tkinter import *


def miles_to_km():
    miles = float(input_window.get())
    kilometers = round(miles * 1.609, 2)
    answer_label.config(text=kilometers)


window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

calc_label = Label(text="is equal to")
calc_label.grid(column=0, row=1)

answer_label = Label(text="0")
answer_label.grid(column=1, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

input_window = Entry(width=7)
input_window.grid(column=1, row=0)

window.mainloop()
