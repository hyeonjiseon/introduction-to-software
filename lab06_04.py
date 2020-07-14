#오륜기(청색/황색/흑색/초록/적색) 그리기
#setup함수를 사용하여 윈도우 크기 지정(가로=1000, 세로=500)
#setposition(x좌표, y좌표),goto(x좌표, y좌표) 등으로 터틀 위치 이동
#원 5개를 동시에 그리기(turtle.Pen()을 5번 생성)
#edges(원을 몇 번에 나눠 그릴 지),
#length(한 번 그릴 때마다 얼만큼 움직일 지),
#angle(한 번 그릴 때마다 몇 도씩 움직일 지) 변수 생성
#for문 안에서 forward()와 right()로 각도 조절하며 그리기

import turtle

turtle.setup(width=1000, height=500)

edges = 100
length = 400/edges
angle = 360/edges

t1 = turtle.Pen()
t2 = turtle.Pen()
t3 = turtle.Pen()
t4 = turtle.Pen()
t5 = turtle.Pen()

t1.pencolor("blue")
t1.width(10)
t1.up()
t1.goto(-250,100)
t1.down()

t2.pencolor("black")
t2.width(10)
t2.up()
t2.goto(-100,100)
t2.down()

t3.pencolor("red")
t3.width(10)
t3.up()
t3.goto(50,100)
t3.down()

t4.pencolor("yellow")
t4.width(10)
t4.up()
t4.goto(-180,10)
t4.down()

t5.pencolor("green")
t5.width(10)
t5.up()
t5.goto(-15,10)
t5.down()


for i in range(edges):
    t1.forward(length)
    t1.right(angle)
    t2.forward(length)
    t2.right(angle)
    t3.forward(length)
    t3.right(angle)
    t4.forward(length)
    t4.right(angle)
    t5.forward(length)
    t5.right(angle)

