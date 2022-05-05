from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


def search():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showerror(title="Error", message="Don't leave the field empty")
    else:
        try:
            with open("data.json", "r") as data:
                read_data = json.load(data)
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="No data found")
        else:
            if website not in read_data:
                messagebox.showerror(title="Error", message="Invalid value")
            else:
                messagebox.showinfo(title=website,
                                    message=f"Email: {read_data[website]['username']}\nPassword: "
                                            f"{read_data[website]['password']}")


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [random.choice(letters) for _ in range(random.randint(9, 11))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    json_data = {
        website: {
            "username": username,
            "password": password,
        }
    }
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please don't leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Email: {username}\nPassword: {password}\nDo you wish save it?")
        if is_ok:
            try:
                with open("data.json", "r") as data:
                    new_data = json.load(data)
                    new_data.update(json_data)
            except FileNotFoundError:
                with open("data.json", "w") as data:
                    json.dump(json_data, data, indent=4)
            else:
                with open("data.json", "w") as data:
                    json.dump(new_data, data, indent=4)
            finally:
                website_entry.delete(0, END)
                username_entry.delete(0, END)
                password_entry.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()
username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2)
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()
