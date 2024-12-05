from turtle import Turtle, Screen
import random
winner = ""
racing = False
screen = Screen()
screen.setup(width=500, height=400)
racer = screen.textinput("Make your bet!", "Which turtle will win the race? enter a color.")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_pos = [-180, -110, -40, 30, 100, 170]
all_turtles = []
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.pu()
    new_turtle.goto(-230, y_pos[turtle_index])
    all_turtles.append(new_turtle)

if racer:
    racing = True

while racing:
    for turtle in all_turtles:
        turtle.fd(random.randint(0, 10))
        if turtle.xcor()>230:
            racing = False
            print(f"Winner is {turtle.pencolor()}!")
            if racer == turtle.pencolor():
                print("You win!")
            else:
                print("You lose!")



screen.exitonclick()