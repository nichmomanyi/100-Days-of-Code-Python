from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.minsize(width=300, height=200)
window.config(pady=20, padx=20)

# Entry
mile_entry = Entry(width=7)
mile_entry.grid(column=1, row=0)

km_input = Label(text="0")
km_input.grid(column=1, row=1)

# Label
is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

miles_input = Label(text="miles")
miles_input.grid(column=2, row=0)

km_lab = Label(text="Km")
km_lab.grid(column=2, row=1)


def converter():
    miles = float(mile_entry.get())
    km = round(miles * 1.609, 2)
    km_input.config(text=f"{km}")


# button
calc = Button(text="Calculate", command=converter)
calc.grid(column=1, row=2)


window.mainloop()
