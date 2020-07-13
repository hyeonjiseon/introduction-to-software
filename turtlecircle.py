#원 그리기
#원은 수많은 선분들이 각도를 조금씩 바꾸어서 연결된 것
#길이가 4인 선분 100개를 3.6도씩 오른쪽으로 회전하면서 그린다.
import turtle
turtle.setup(width=500, height=500)
edges=100
length=400/edges #길이 4
angle=360/edges #3.6도
t=turtle.Pen()
t.pencolor("blue")
t.width(5)
t.speed(5)
for i in range(edges):
    t.forward(length)
    t.right(angle)
