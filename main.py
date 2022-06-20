import turtle
import pandas as pd
screen=turtle.Screen()
screen.title("Name The State Game")
image="country_img.gif"
screen.addshape(image)
turtle.shape(image)

states=pd.read_csv("50_states.csv")
state_list=states.state.to_list()
guessed=[]
while len(guessed)<len(state_list):
    user_answer=screen.textinput(title=f"{len(guessed)}/{len(state_list)} Guess a State",prompt="Enter a state (Out to exit)")
    user_answer=user_answer.title()

    if user_answer=="Out":
        missedState=[missed for missed in state_list if (missed not in guessed)]
        new_data=pd.DataFrame(missedState)
        new_data.to_csv("missed_states.csv")
        break

    if user_answer in  state_list :
        if user_answer not in guessed:
            guessed.append(user_answer)
            text=turtle.Turtle()
            text.hideturtle()
            text.penup()
            x_coor=states[states.state==user_answer].x.item()
            y_coor=states[states.state==user_answer].y.item()
            text.goto(x_coor,y_coor)
            text.write(user_answer)

screen.exitonclick()