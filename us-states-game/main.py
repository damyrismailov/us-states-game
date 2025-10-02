import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
data_list = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title =f"{len(guessed_states)}/50 States correct", prompt = "What is your guess?").title()
    print(answer_state)
    if answer_state == "Exit":
        states_to_learn = [state for state in data_list if state not in guessed_states]
        s = pandas.DataFrame(states_to_learn)
        s.to_csv("states_to_learn.csv")
        break
    if answer_state in data_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
