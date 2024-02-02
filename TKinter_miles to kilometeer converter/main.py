from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.minsize(width=300, height=200)
window.config(pady=20, padx=20)

# Entry
mile_entry = Entry()
mile_entry.insert(END, string="0")
mile_entry.grid(column=1, row=0)

km_entry = Entry()
km_entry.insert(END, string="0")
km_entry.grid(column=1, row=1)

# Label
is_equal = Label(text="is equal to", font=("arial", 16, "normal"))
is_equal.grid(column=0, row=1)

miles = Label(text="miles", font=("arial", 16, "normal"))
miles.grid(column=2, row=0)

km = Label(text="Km", font=("arial", 16, "normal"))
km.grid(column=2, row=1)


def converter():
    pass


# button
calc = Button(text="Calculate", command=converter())
calc.grid(column=1, row=2)


window.mainloop()
