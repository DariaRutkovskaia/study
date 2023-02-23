import json
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
    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }

    if website != "" and username != "" and password != "":
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showinfo(title="Enter the info", message=f"Don't leave any fields empty!")


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            existed_password = data[website]
    except KeyError:
        messagebox.showinfo(title="Ooops", message=f"No details for{website} exists")
    except FileNotFoundError:
        messagebox.showinfo(title="Ooops", message=f"Password list does not exist")
    else:
        messagebox.showinfo(title=f"{website}", message=f"email: {existed_password['email']}\n"
                                                        f"password: {existed_password['password']}")


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

website_entry = Entry()
website_entry.focus()
website_entry.grid(sticky="ew", row=1, column=1)

username_entry = Entry(width=36)
username_entry.insert(0, "my_email@mail.com")

username_entry.grid(sticky="ew", row=2, column=1, columnspan=2)

password_entry = Entry(width=21)

password_entry.grid(sticky="ew", row=3, column=1)

generate_button = Button(text="Generate password", command=generate_password)
generate_button.grid(sticky="w", row=3, column=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(sticky="ew", row=4, column=1, columnspan=2)

search_button = Button(text="Search", command=search)
search_button.grid(sticky="ew", row=1, column=2)

window.mainloop()
