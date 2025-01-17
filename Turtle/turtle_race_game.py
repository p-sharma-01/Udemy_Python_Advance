from turtle import Turtle , Screen
from random import randint
screen=Screen()
race_start=False
user_bet=screen.textinput("Make your bet","Choose your color :")
is_race_start=False
screen.setup(width=500,height=400)
colors=['red','yellow','green','blue','purple','orange']
y_positions=[-70,-40,-10,20,50,80]
all_turtle=[]
for i in range(6):
    new_turtle=Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_positions[i])
    all_turtle.append(new_turtle)

if user_bet:
    race_start=True

while race_start:
    for i in all_turtle:
        i.forward(randint(1,10))
        if i.xcor()>230:
            if i.color()==user_bet.lower():
                print(f"You Won !!! {i.color()[0]} turle won the match.")
                race_start=False
            else:
                print(f"You Loses !!! {i.color()[0]} turle won the match.")
                race_start=False

