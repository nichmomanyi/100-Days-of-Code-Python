import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S Statates naming Game")
Image = "blank_states_img.gif"
screen.addshape(Image)
turtle.shape(Image)

data = pd.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []
missing_state = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct", prompt="What's another state name?").title()

    if answer_state == "Exit":
        # States not mentioned
        for state in all_states:
            if state not in guessed_states:
                missing_state.append(state)
            new_data = pd.DataFrame(missing_state)
            new_data.to_csv("Staes to learn.csv")
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(state_data["state"].item())



