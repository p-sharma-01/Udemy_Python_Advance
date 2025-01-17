from turtle import Turtle,Screen
arr=Turtle()
screen=Screen()
arr.shape("turtle")
for i in range(4):
    for j in range(10):
        arr.fd(10)
        arr.penup()
        arr.forward(10)
        arr.pendown()
    arr.left(90)
screen.exitonclick()