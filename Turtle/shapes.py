from turtle import Turtle, Screen
arr=Turtle()
screen=Screen()
def triangle():
    for i in range(3):
        arr.forward(100)
        arr.left(120)

def pentagon():
    for i in range(5):
        arr.forward(100)
        arr.left(72)


def hexagon():
    for i in range(6):
        arr.forward(100)
        arr.left(60)

def decagon():
    for i in range(10):
        arr.forward(50)
        arr.left(36)

decagon()
screen.exitonclick()

#Thumb Rule : 360/no. of sides is the angle in the left() and call  the loop upto the no. of sides 





