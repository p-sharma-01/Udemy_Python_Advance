from turtle import Turtle , Screen,colormode
from random import randint
arrow=Turtle()
screen=Screen()
colormode(255)
arrow.speed("fastest")
arrow.pensize(10)

for i in range(360//5):
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    p=(r,g,b)
    arrow.pencolor(p)
    arrow.circle(100)
    arrow.setheading(arrow.heading()+5)
screen.exitonclick()

