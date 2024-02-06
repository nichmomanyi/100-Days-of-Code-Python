from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json


# import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(numbers) for char in range(randint(2, 4))]
    password_numbers = [choice(symbols) for char in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    # pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Ensure no field is empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            # saving updated data
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_pass():
    website = web_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(height=200, width=200)
logo_mg = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_mg)
canvas.grid(column=1, row=0)

# Labels
website_lab = Label(text="Website: ")
website_lab.grid(row=1, column=0)

email_lab = Label(text="Email/Username:")
email_lab.grid(row=2, column=0)

password_lab = Label(text="Password:")
password_lab.grid(row=3, column=0)

# Entries
web_entry = Entry(width=30)
web_entry.grid(column=1, row=1)
web_entry.focus()

email_entry = Entry(width=47)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "nmomce44@gmail.com")

pass_entry = Entry(width=27)
pass_entry.grid(column=1, row=3)

# Buttons
gen_pass_button = Button(text="Generate Password", command=generate_password)
gen_pass_button.grid(column=2, row=3, columnspan=2)

add_button = Button(text="Add", width=45, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=search_pass, width=15)
search_button.grid(column=2, row=1, columnspan=2)

window.mainloop()
