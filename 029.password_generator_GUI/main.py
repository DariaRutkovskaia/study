from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox

import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website != "" and username != "" and password != "":
        is_ok = messagebox.askyesno(title=website, message=f"This is the information to save: \n"
                                                           f"email:{username} \n"
                                                           f"password: {password} \n is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    else:
        messagebox.showinfo(title="Enter the info", message=f"Don't leave any fields empty!")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Username/email:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=36)
website_entry.focus()

website_entry.grid(sticky="ew", row=1, column=1, columnspan=2)

username_entry = Entry(width=36)
username_entry.insert(0, "my_email@mail.com")

username_entry.grid(sticky="ew", row=2, column=1, columnspan=2)

password_entry = Entry(width=21)

password_entry.grid(sticky="ew", row=3, column=1)

generate_button = Button(text="Generate password", command=generate_password)
generate_button.grid(sticky="w", row=3, column=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(sticky="ew", row=4, column=1, columnspan=2)

window.mainloop()
