import turtle
import pandas

screens=turtle.Screen()
screens.addshape("india_map.gif")
screens.title("Guess the state")
screens.setup(700,800)
tim=turtle.Turtle()
turtle.shape("india_map.gif")
tim.penup()
tim.hideturtle()
titlebar="Guess the state"
score=0

while (score<29):
    answer=screens.textinput(title=titlebar, prompt="Type state name").title()
    game_list=pandas.read_csv("Indian_states.csv")
    states_name=game_list.State.to_list()
    if answer in states_name:
        row=game_list[game_list.State==answer]
        tim.goto(x=row.X.item(),y=row.Y.item())
        tim.write(answer)
        score+=1
        titlebar=f"{score}/28 Guessed correctly"
    else:
        titlebar=f"{score}/28 Guessed correctly"
    



screens.mainloop()