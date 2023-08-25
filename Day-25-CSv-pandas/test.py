import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_data = pd.read_csv("50_states.csv")
states_list = state_data.state.to_list()

while len(states_list) > 0:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in states_list if state != "Exit"]
        new_data = pd.DataFrame(missing_states, columns=["Missing States"])
        new_data.to_csv("missing_states.csv", index=False)
        break

    if answer_state in states_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        goto_data = state_data[state_data.state == answer_state]
        t.goto(int(goto_data.x), int(goto_data.y))
        t.write(answer_state)

        states_list.remove(answer_state)

turtle.mainloop()

