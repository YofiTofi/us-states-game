from turtle import Turtle, Screen
import pandas
IMAGE = "blank_states_img.gif"
state_data_csv = "50_states.csv"
state_data = pandas.read_csv(state_data_csv)
states = state_data.state
screen = Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE)
screen.screensize(canvwidth=725, canvheight=491)
tom = Turtle(shape=IMAGE)
tom.penup()
tim = Turtle()
tim.hideturtle()
tim.penup()
guessed_states = 0
while guessed_states < 50:
    user_state_guess = screen.textinput(title="State Name Input", prompt="Please input a valid state name: ").title()
    guess_index = states[states.str.contains(user_state_guess) == True].index
    if guess_index.nbytes > 0:
        # print(guess_index.nbytes)
        state_x_cor = state_data[state_data["state"].str.contains(user_state_guess) == True]["x"].to_list()[0]
        state_y_cor = state_data[state_data["state"].str.contains(user_state_guess) == True]["y"].to_list()[0]
        # print(f"x: {state_x_cor}\ny: {state_y_cor}")
        tim.goto(x=state_x_cor, y=state_y_cor)
        tim.write(user_state_guess)
        guessed_states += 1
    else:
        print(guess_index.nbytes)
screen.exitonclick()
