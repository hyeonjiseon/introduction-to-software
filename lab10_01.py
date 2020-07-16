#사용자로부터 5개의 점수를 입력 받아 점수별 그래프로 출력하는 프로그램
#tkinter 모듈 사용
#캔버스 크기는 800*800
#점수 구간에 따라 다른 색상으로 그리기
# 90점 이상: 녹색
# 80점 이상 90점 미만: 파란색
# 60점 이상 80점 미만: 주황색
# 60점 미만: 빨간색

from tkinter import *
import time

tk = Tk()
canvas = Canvas(tk, width = 800, height = 800)
canvas.pack()
scores = []
i = 0

print("5개의 점수를 입력하세요.")

for k in range(5):
    score = int(input("점수 입력 : "))
    scores.append(score)

for score in scores:
    x1=100
    y1=100 + i
    x2=100+score*3
    y2=100+50+i
    
    if score >= 90:
        colors = "green"
    elif 80 <= score < 90:
        colors = "blue"
    elif 60 <= score < 80:
        colors = "orange"
    else:
        colors = "red"
    
    canvas.create_rectangle(x1, y1, x2, y2, fill = colors)   
    canvas.create_text(x2+40, y1+20, text = str(score))
    i = i + 100
    tk.update()
    time.sleep(0.5)


#다른 방법
    
from tkinter import*
import time
tk = Tk()
canvas = Canvas(tk, width = 800, height = 800)
canvas.pack()
scores = []
print("5개의 점수를 입력하세요.")
for k in range(5):
    score = int(input("점수 입력 : "))
    scores.append(score)
i=0

for score in scores:
    x1 = 100
    y1 = 100 + i
    x2 = 100 + score*3
    y2 = 100 + 50 + i

    if score>=90:
        canvas.create_rectangle(x1, y1, x2, y2, fill = "green")

    elif score>=80 and score<90:
        canvas.create_rectangle(x1, y1, x2, y2, fill = "blue")
    elif score>=60 and score<80:
        canvas.create_rectangle(x1, y1, x2, y2, fill="orange")
    else:
        canvas.create_rectangle(x1, y1, x2, y2, fill="red")

    canvas.create_text(x2+40, y1+20, text = str(score))
    i = i+100
    tk.update()
    time.sleep(0.5)

