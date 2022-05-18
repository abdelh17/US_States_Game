import turtle
import pandas as pd
screen=turtle.Screen()
screen.title("Name The State Game")
image="country_img.gif"
screen.addshape(image)
turtle.shape(image)

states=pd.read_csv("50_states.csv")
state_list=states.state.to_list()

user_answer=screen.textinput(title="Guess a State",prompt="Enter a state")
print(states[states.state==user_answer.title()])

print(states[states.state==user_answer.title()].x.item())

if user_answer.title() in  state_list:
    text=turtle.Turtle()
    text.hideturtle()
    text.penup()
    x_coor=states[states.state==user_answer.title()].x.item()
    y_coor=states[states.state==user_answer.title()].y.item()
    text.goto(x_coor,y_coor)
    print("goodguess")

screen.exitonclick()