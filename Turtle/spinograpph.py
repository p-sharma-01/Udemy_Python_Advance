from turtle import Turtle , Screen
from random import randint
arrow=Turtle()
screen=Screen()
arrow.speed("fastest")
for i in range(360):
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    arrow.pencolor(r,g,b)
    for j in range(360):
        arrow.forward(1)
        arrow.left(1)
    arrow.left(5)
screen.exitonclick()
