from turtle import Turtle , Screen
arrow=Turtle()
screen=Screen()
screen.listen()
def forward():
    arrow.forward(50)
def backward():
    arrow.backward(50)
def clockwise():
    arrow.right(90)
def anti_clockwise():
    arrow.left(90)
def clean_drawing():
    arrow.clear()
    arrow.up()
    arrow.home()
    arrow.down()
screen.onkey(forward,"W")
screen.onkey(backward,"S")
screen.onkey(clockwise,"A")
screen.onkey(anti_clockwise,"D")
screen.onkey(clean_drawing,"C")
screen.exitonclick()