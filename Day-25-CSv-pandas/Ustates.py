import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S.States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


state_data = pd.read_csv("50_states.csv")
state = state_data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct", prompt="What's another name?"
    ).title()

    if answer_state == "Exit":
        missing_states = []
        for new_state in state:
            if new_state not in guessed_states:
                missing_states.append(new_state)
                newstate = pd.DataFrame(missing_states)
                newstate.to_csv("mystate.csv")

    if answer_state in state:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        goto_data = state_data[state_data.state == answer_state]
        t.goto(int(goto_data.x), int(goto_data.y))
        t.write(goto_data.state.item())
    print(state)
turtle.mainloop()
# screen.exitonclick()
