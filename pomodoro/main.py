from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = 0
# ---------------------------- TIMER RESET ------------------------------- #
def  reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "00:00")
    title_lab.config(text="Timer", fg=GREEN)
    checkmarks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    shortbread_sec = SHORT_BREAK_MIN * 60
    longbreak_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(longbreak_sec)
        title_lab.config(text= "Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(shortbread_sec)
        title_lab.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        title_lab.config(text="Work", fg=GREEN)

    count_down(5 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec <10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    global timer
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        checkmarks.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_lab = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_lab.grid(column=1, row=0)

canvas = Canvas(width=200, height=225, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_botton = Button(text="Start", highlightthickness=0, command=start_timer)
start_botton.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmarks = Label(fg=GREEN, bg=YELLOW, font=10)
checkmarks.grid(column=1, row=3)

window.mainloop()
