# us-states-game
# This game is intended to test the user on how many states they can name.
# The user is prompted to type in the name of a US state and, if a valid state name,
# the name entered will be automatically added to the map on that state.
# Gameplay continues until the user names all the states or they type 'exit'
# Any states that the user misses will be written to a file named 'states_missed.csv'
#

import turtle
import pandas

NUM_STATES_TO_GUESS = 50

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Display the x and y coords of where the mouse is clicked
# def get_mouse_click_coord(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coord)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
states_guessed = []

while len(states_guessed) <= NUM_STATES_TO_GUESS:

    answer = screen.textinput(title=f"{len(states_guessed)}/50 States Correct",
                              prompt="Enter the name of a state ('exit' to stop):").title()
    # print(answer)
    if answer == "Exit":
        states_missed = [
            state for state in states_list if state not in states_guessed]
        # states_missed = []
        # for state in states_list:
        #     if state not in states_guessed:
        #         states_missed.append(state)
        # print(states_missed)
        new_file = pandas.DataFrame(states_missed)
        new_file.to_csv("states_missed.csv")
        break

    if answer in states_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        data_row = data[data.state == answer]
        t.goto(int(data_row.x), int(data_row.y))
        t.write(answer)
        # t.write(data_row.state.item())
        states_guessed.append(answer)

if len(states_guessed) == NUM_STATES_TO_GUESS:
    new_file = pandas.DataFrame(["All Correct!"])
    new_file.to_csv("states_missed.csv")

screen.exitonclick()
