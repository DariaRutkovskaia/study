from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
reps = 0

timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    global reps, timer
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    timer_label.config(text="Timer", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps < 9:
        checkmark_label.config(text=CHECK_MARK * (reps // 2))
        if reps % 2 == 1:
            count_down(work_sec)
            timer_label.config(text="Work", fg=GREEN)
        elif reps == 8:
            count_down(long_break_sec)
            timer_label.config(text="Break", fg=RED)
        elif reps % 2 == 0:
            count_down(short_break_sec)
            timer_label.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps, timer

    count_min = count // 60
    count_sec = count % 60
    if count_min == 0:
        count_min = "00"
    elif 10 > count_min > 0:
        count_sec = f"0{count_min}"

    if count_sec == 0:
        count_sec = "00"
    elif 10 > count_sec > 0:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    elif count == 0:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(height=224, width=200, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_png)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# count_down(5)
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

checkmark_label = Label(text=" ", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
checkmark_label.grid(column=1, row=3)

start_button = Button(text="Start", font=(FONT_NAME, 13, "bold"), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 13, "bold"), command=timer_reset)
reset_button.grid(column=2, row=2)

window.mainloop()
