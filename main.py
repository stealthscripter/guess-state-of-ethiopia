import turtle
import pandas
screen = turtle.Screen()
screen.title("Ethiopia Regions Game")


image = "RegionalMap.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("RegionalData.csv")
data_list = data.state.to_list()

state_turtle = turtle.Turtle()



guess_state = []
while len(guess_state) < 9:
    answer_state = screen.textinput(title=f"{len(guess_state)}/10 State Correct", prompt="What's another state name").title()
    if answer_state == "Exit":
        break
    if answer_state in data_list:
        guess_state.append(answer_state)
        state_name = data[data.state == answer_state]
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_turtle.goto(int(state_name.x), int(state_name.y))
        state_turtle.write(answer_state)

user_data =pandas.DataFrame(guess_state)
user_data.to_csv("guessed_state")

screen.exitonclick()