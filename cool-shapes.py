from turtle import *
bgcolor('black')
speed(0)
hideturtle()
for i in range(120):
    color('aqua')
    circle(i)
    color('white')
    circle(i*0.8)
    right(3)
    forward(1)
done()    