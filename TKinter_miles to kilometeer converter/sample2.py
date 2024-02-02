from tkinter import *

window = Tk()
window.title("MY first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)
# Label
my_label = Label(text="New Text", font=("Arial", 20, "bold"))
my_label.config(text="This is a new text")
my_label.grid(column=0, row=0)


# Button
def button_clicked():
    print("I got clicked")
    my_label.config(text="Button got clicked")


def button_next():
    print("Move to the next")


button = Button(text="Click me", command=button_clicked())
button.grid(column=1, row=2)

button2 = Button(text="Click next", command=button_next())
button2.grid(column=2, row=1)
# Entry
input = Entry()
input.grid(column=1, row=1)
input.get()

window.mainloop()
