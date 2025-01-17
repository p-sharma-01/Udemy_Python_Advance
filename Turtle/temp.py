from turtle import Turtle, Screen
import time





screen = Screen()
screen.tracer()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
position = [0, -20, -40]
segments = []

for i in range(3):
    bun = Turtle("square")
    bun.color("white")
    bun.penup()
    bun.goto((position[i], 0))
    segments.append(bun)


is_game_on = True

while is_game_on:
    time.sleep(1)
    screen.update()
    
    for bun in segments:
        bun.fd(20)
        

        
    
screen.exitonclick()