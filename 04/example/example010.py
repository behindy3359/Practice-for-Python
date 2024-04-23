from turtle import *
shape('turtle')
pensize(2)
colormode(255)
x=int(xcor())
y=int(ycor())
color(int((x+y)%256),int((x+y)%256),int((x+y)%256))

goto(0,-200)
setheading(180)
col=255
col1=0
for i in range(19,0-1,-1):
    begin_fill()
    for ii in range(i):
        fd(100), rt(360/i)
    end_fill()
    col -= int(255/19)
    col1 += int(255/19)
penup()