#원 그리기
import turtle
import random
turtle.setup(width=500, height=500)
t=turtle.Pen()
t.width(3)
t.speed(5)
t.color(1,1,0)
t.pencolor(0,0,1)

t.begin_fill()
t.circle(50) #50반지름 가진 원(원 그리기 함수 제공)
t.end_fill()
