#키보드와 마우스를 이용하여 원하는 위치에 선택한 도형이 그려지는 프로그램
#만들어야 하는 함수
# 1) 펜을 들고 2) 내리는 함수와 3) 좌표를 이동하는 함수
# 4) 길이를 늘리고 5) 줄이는 합수(길이는 50으로 초기화)
# 6) 정사각형, 7) 정삼각형, 8) 정팔각형, 9) 원, 10) 별이 그려지는 함수
# 11) 빨강 12) 노랑, 13) 파랑으로 색을 바꾸는 함수
# 14) 캔버스를 초기화하는 함수와 15)터틀 그래픽을 끝내는 함수

import turtle

turtle.setup(600, 600)
s=turtle.Screen()

t = turtle.Turtle()
t.width(5)
t.color("black")

length = 50

def up():
    return t.up()

def down():
    return t.down()

def move(x,y):
    return t.goto(x,y)

def long():
    global length
    length = length + 10
    return length

def short():
    global length
    length = length - 10

def square():
    t.begin_fill()
    for i in range(4):
        t.fd(length)
        t.rt(90)
    t.end_fill()

def triangle():
    t.begin_fill()
    for i in range(3):
        t.fd(length)
        t.rt(120)
    t.end_fill()

def circle():
    t.begin_fill()
    t.circle(length)
    t.end_fill()

def octagon():
    t.begin_fill()
    for i in range(8):
        t.fd(length)
        t.rt(45)
    t.end_fill()

def star():
    t.begin_fill()
    for i in range(5):
        t.fd(100)
        t.rt(144)
    t.end_fill()

def red():
    t.color("Red")

def yellow():
    t.color("Yellow")

def blue():
    t.color("Blue")

def reset():
    s.reset()

def bye():
    s.bye()

s.onclick(move)
s.onkey(up, "Up")
s.onkey(down, "Down")

s.onkey(square, 's')
s.onkey(long, 'Right')
s.onkey(short, 'Left')
s.onkey(triangle, 't')
s.onkey(circle, 'c')
s.onkey(octagon, 'o')
s.onkey(star, 'k')

s.onkey(red, 'r')
s.onkey(yellow, 'y')
s.onkey(blue, 'b')
s.onkey(reset, 'z')
s.onkey(bye, 'x')

s.listen() #키보드 입력을 맏을 수 있도록 포커스를 줌
s.mainloop() #종료 전까지 프로그램을 실행하면서 마우스나 키보드 입력을 계속 처리
