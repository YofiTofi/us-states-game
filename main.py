from turtle import Turtle, Screen
import pandas
IMAGE = "blank_states_img.gif"
state_data_csv = "50_states.csv"
states_data = pandas.read_csv(state_data_csv)
states = states_data.state.to_list()
print(states)
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
    user_guess = screen.textinput(title=f"{guessed_states}/50 Correct States", prompt="Please guess a state name:").title()
    if user_guess in states:
        guessed_state = states_data[states_data.state == user_guess]
        tim.goto(x=int(guessed_state.x), y=int(guessed_state.y))
        tim.write(user_guess)
        guessed_states += 1
screen.exitonclick()
