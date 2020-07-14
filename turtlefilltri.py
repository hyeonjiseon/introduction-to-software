#삼각형 칠하기
#begin_fill과 end_fill 함수 블록 사이 다각형의 내부에 칠해진다
#setheading(60)은 거북이 향하는 방향을 초기 방향(동쪽)에서 반시계 방향으로 60도 회전한 쪽으로 변경
import turtle

t=turtle.Pen()
t.width(3)
t.speed(5)
t.color(1,1,0) #빨강, 초록이라 노랑이 됨
t.pencolor(0,0,1) #파랑
t.begin_fill()
t.setheading(60)
for i in range(3):
    t.forward(100)
    t.right(120)
t.end_fill()
