#삼각형이 위아래로 움직이는 프로그램
#tkinter와 time 모듈 사용
#canvas 크기 width = 500, height = 500
#삼각형이 화면 밖을 넘어가지 않도록 하며, 벽 부분에 가면 튕겨져 나오도록
#canvas의 coords() 함수 사용하면 도형의 현재 좌표 알 수 있음
# 예)canvas = Canvas(매개변수들)
#    canvas.createpolybon(삼각형을 구성하는 x,y 좌표들)
#    position = canvas.coords(1)
# >>position은 삼각형을 구성하는 좌표들이 [x0, y0, x1, y1, x2, y2]처럼 리스트 형태
#Canvas의 move() 함수를 통해 삼각형을 조금식 움직임
#삼각형이 벽에 닿을 것 같으면 방향 전환
# canvas.coords(1)로 구한 과표들 중에서 왼쪽 꼭지점의 x좌표가 0미만이 되면 왼쪽 벽에 닿았다는 뜻
# 벽에 닿을 것 같으면 move()의 방향 전환

from tkinter import *
import time
import random

tk = Tk()
canvas = Canvas(tk, width = 500, height = 500)
canvas.pack()
canvas.create_polygon(25, 150, 50, 200, 0, 200)
x=3
y=3

while True:
      
    canvas.move(1, x, y)
    position = canvas.coords(1)

    if position[3]>=500:
        y=-3
    if position[3]<=50:
        y=3
    if position[4]<=0:
        x=3
    if position[2]>=500:
        x=-3
    tk.update()
    time.sleep(0.05)




