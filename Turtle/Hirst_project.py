# import colorgram
# rgb_color=[]
# color=colorgram.extract("th.jpg",30)
# for i in color:
#     r=i.rgb.r
#     g=i.rgb.g
#     b=i.rgb.b
#     p=(r,g,b)
#     rgb_color.append(p)
# print(rgb_color)
from turtle import Turtle,Screen,colormode
from random import choice
colormode(255)
arrow=Turtle()
colors=[(236, 232, 223), (229, 233, 239), (239, 230, 235), (227, 235, 230), (194, 164, 111), (68, 90, 123), (142, 168, 186), (132, 93, 54), (215, 205, 133), (142, 66, 87), (30, 38, 64), (185, 142, 158), (122, 32, 55), (76, 14, 33), (138, 180, 150), (161, 152, 58), (44, 55, 98), (174, 97, 111), (53, 33, 22), (67, 117, 102), (219, 176, 189), (102, 118, 161), (178, 186, 212), (93, 151, 116), (180, 104, 88), (172, 204, 173), (165, 201, 212), (89, 144, 153), (82, 71, 35), (223, 177, 168)]
arrow.setheading(225)
arrow.up()
arrow.forward(300)
arrow.setheading(360)
for i in range(5):
    for j in range(10):
        arrow.dot(20,choice(colors))
        arrow.up()
        arrow.forward(50)
        arrow.down()
    arrow.left(90)
    arrow.up()
    arrow.forward(50)
    arrow.left(90)
    arrow.forward(50)
    arrow.down()
    for j in range(10):
        arrow.dot(20,choice(colors))
        arrow.up()
        arrow.forward(50)
        arrow.down()
    arrow.right(90)
    arrow.up()
    arrow.forward(50)
    arrow.right(90)
    arrow.forward(50)
    arrow.down()


screen=Screen()
screen.exitonclick()