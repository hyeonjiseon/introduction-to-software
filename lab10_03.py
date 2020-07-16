#원이 점점 커지다가 다시 작아지는 프로그램
#tkinter와 random모듈 사용
#원이 화면 밖을 넘어가지 않도록 하며, 무한반복으로 움직이기
#5가지 이상의 색을 리스트로 선언한 후 random 모율의 choice()를 사용하여 색 선택
#outline='색 이름' 인자를 사용하여 색 설정
# 예) canvas.create_arc(다른 인자들, outline='red')
#canvas.delete('all') 사용하여 전에 그린 원 지우기
#time.sleep()으로 시간을 주면 원 움직임을 관찰하기 쉬움

from tkinter import *
import random
import time

tk=Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
color = ['red', 'orange', 'yellow', 'green', 'blue', 'black']

while True:

    for i in range(10, 250, 10):
        x1 = 250 - i
        y1 = 250 - i
        x2 = 250 + i
        y2 = 250 + i
        canvas.create_arc(x1, y1, x2, y2, extent = 359, style=ARC, outline = random.choice(color))
        tk.update()
        canvas.delete('all')
        time.sleep(0.05)

    for i in range(250, 10, -10):
        x1 = 250 - i
        y1 = 250 - i
        x2 = 250 + i
        y2 = 250 + i
        canvas.create_arc(x1, y1, x2, y2, extent = 359, style=ARC, outline = random.choice(color))
        tk.update()
        canvas.delete('all')
        time.sleep(0.05)

#다른 방법
from tkinter import *
import random
import time
tk = Tk()
canvas = Canvas(tk, width = 500, height = 500)
canvas.pack()
colors = ['red', 'pink', 'blue', 'purple', 'orange']
width = 500
height = 500
step = 5
fill = random.choice(colors)

while True:
    for i in range(10, 250, step):
        x1 = width /  2 - i
        y1 = height / 2 - i
        x2 = width / 2 + i
        y2 = width / 2 + i
        canvas.create_arc(x1, y1, x2, y2, extent=359, style = ARC, outline = fill)
        tk.update()
        canvas.delete('all')
        fill = random.choice(colors)
        time.sleep(0.05)
    
    for i in range(250, 10, -step):
        x1 = width /  2 - i
        y1 = height / 2 - i
        x2 = width / 2 + i
        y2 = width / 2 + i
        canvas.create_arc(x1, y1, x2, y2, extent=359, style = ARC, outline = fill)
        tk.update()
        canvas.delete('all')
        fill = random.choice(colors)
        time.sleep(0.05)

