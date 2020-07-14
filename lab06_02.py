#빨간 하트 그리기
#직선과 반원을 이용하여 하트 그리기
#펜 색은 검은색, 하트 안은 빨간색
#turtle.circle(반지름, 각도의 범위)
# 예) turtle.circle(5,180): 반지름이 5인 반원
#pencolor, color, begin_fill, end_fill 함수 사용

import turtle

t=turtle.Pen()

t.color("red")
t.pencolor("black")
t.begin_fill()
t.left(45)
t.forward(50)
t.circle(25, 180)
t.right(90)
t.circle(25,180)
t.forward(50)
t.end_fill()
