from turtle import Turtle
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]
        self.length=4
        self.p=0
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for i in range(self.length):
            self.add_segments(i)
            
    def add_segments(self,i):
        arrow=Turtle("square")
        arrow.color("white")
        arrow.penup()
        arrow.goto(x=self.p,y=0) 
        self.p-=20
        self.segments.append(arrow)
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]
    def extend(self):
        self.add_segments(self.segments[-1].position())
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    
            
        
    
