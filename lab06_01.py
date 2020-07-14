#집 그리기
#본채, 지붕, 문은 for 문을 이용하고, 창문은 중첩 for문 이용
#setheading, left, right 함수를 이용하여 터틀 각도 설정
#setposition(x좌표, y좌표), goto(x좌표,y좌표) 등을 사용하여 터틀 위치 이동

#창문 중첩 for문 쓰는 법
# 1)첫 번재 for문: 시작 각도 조절
# 2)두 번째 for문: 네모 그리는 작업

#본채, 지붕, 문 for문 쓰는 법:
# 1)for문을 range(2)로 잡음(직사각형기기 때문. 정사각형이면 range(4))
# 2)한쪽 가로세로를 두 번

import turtle

t=turtle.Pen()
t.width(3)
t.speed(5)
t.pencolor("orange")
t.up()
t.setposition(-300, -250)
t.down()

#본채
for i in range(2):
    t.forward(600)
    t.left(90)
    t.forward(300)
    t.left(90)

t.up()
t.goto(-75, -250)
t.down()

t.pencolor("red")

#문
for i in range(2):
    t.forward(150)
    t.left(90)
    t.forward(200)
    t.left(90)

t.up()
t.goto(-50, -155)
t.down()
t.circle(10)

#창문
t.up()
t.setposition(-200,-50)
t.down()
t.pencolor("blue")
t.setheading(90)

for i in range(4):
    for j in range(4):
        t.forward(50)
        t.right(90)
    t.right(90)

t.up()
t.setposition(200,-50)
t.down()

for i in range(4):
    for j in range(4):
        t.forward(50)
        t.right(90)
    t.right(90)

#지붕
t.up()
t.setposition(-300,50)
t.down()
t.pencolor("brown")
t.setheading(30)
t.forward(344)
t.right(60)
t.forward(345)



















