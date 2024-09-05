import turtle as t
import random
from turtle import Screen
t.colormode(255)
tim = t.Turtle()
tim.pu()
color_list = [(219, 152, 97), (34, 106, 148), (172, 69, 36), (234, 212, 96), (122, 172, 198), (33, 132, 88), (67, 27, 11), (21, 41, 75), (120, 188, 157), (225, 81, 54), (144, 57, 89), (142, 26, 59), (212, 74, 96), (206, 132, 156), (149, 28, 14), (11, 97, 65), (48, 168, 107), (47, 46, 122), (217, 157, 19), (236, 171, 157), (147, 214, 195), (11, 58, 35), (41, 160, 186), (74, 24, 48), (91, 86, 17), (234, 164, 185)]
tim.teleport(-200, -200)

def move():
    for i in range(9):
        tim.fd(50)
        tim.dot(20, random.choice(color_list))
    tim.setheading(90)

direction = 0
for _ in range(1, 11):
    if _ % 2 == 0:
        direction = 180
    else:
        direction = 0
    tim.setheading(direction)
    tim.dot(20)
    tim.pencolor(random.choice(color_list))
    move()
    tim.fd(50)
















screen = Screen()
screen.exitonclick()