#무작위로 선 그리기
import turtle
import random
turtle.setup(width=500, height=500)
t=turtle.Pen()
t.width(3)
t.speed(5)
for i in range(200):
    t.pencolor(random.random(), random.random(), random.random())
    #random.random() 0~1.0 사이의 실수
    length = random.randint(10,60) #10~60 사이 값
    angle = random.randint(30, 120)
    t.forward(length)
    t.right(angle)
