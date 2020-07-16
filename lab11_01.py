#아날로그 시계 프로그램
#tkinter, time, math 모듈 사용
#분과 초 단위로 눈금 추가
#상단에 AM/PM(오전/오후) 추가, 상자 테두리: 주황색, 글씨: 검정색
#하단에 월, 일, 요일 추가, 상자 테두리: 회색, 글씨: 보라색

from tkinter import *
import time
import math

tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
width=500
height=500
r = 240

sr = height/2-50 #초침 길이
mr = height/2-80 #분침 길이
hr = height/2-110 #시침 길이

while 1:

    t = time.localtime()
    hour = (t[3] + t[4]/60)* 30 #1시간 30도, 시와 시 사이 분 반영
    minute = (t[4] + t[5]/60)*6 #1분에 6도, 분과 분 사이 초 반영
    second = t[5]*6 #1초에 6도
    
    canvas.create_arc(10, 10, width-10, height-10, extent = 359, style = CHORD) #시계 테두리
    canvas.create_arc(240, 240, 260, 260, extent = 359, style = CHORD,fill = 'black') #시계 중심
    canvas.create_rectangle(220, 80, 280, 120, outline = 'orange', width=3)
    canvas.create_rectangle(190, 420, 310, 380, outline = 'gray', width=3)

    if 0 <= t[3] <= 12:
        daylight = 'AM'
    else:
        daylight = 'PM'
    canvas.create_text(250, 100, text = str(daylight), font=('Arial', 15))

    if t[6] == 0:
        dayweek = '월'
    elif t[6] == 1:
        dayweek = '화'
    elif t[6] == 2:
        dayweek = '수'
    elif t[6] == 3:
        dayweek = '목'
    elif t[6] == 4:
        dayweek = '금'
    elif t[6] == 5:
        dayweek = '토'
    elif t[6] == 6:
        dayweek = '일'
    daydate = str(t[1])+"월 "+str(t[2])+"일("+dayweek+")"
    canvas.create_text(250, 400, text=daydate, font=('Arial', 15), fill='purple')

    #시계 테두리 눈금
    for i in range(0, 360, 6):
        x1 = 250+230*math.sin(i/360*3.14*2)
        y1 = 250-230*math.cos(i/360*3.14*2)
        x2 = 250+r*math.sin(i/360*3.14*2)
        y2 = 250-r*math.cos(i/360*3.14*2)
        bold=1
        
        for k in range(12):
            if i == 30*k:
                bold = 3
            
        canvas.create_line(x1, y1, x2, y2, width=bold)

    hx = hr * math.sin(hour/360 * 3.14*2)
    hy = hr * math.cos(hour/360 * 3.14*2)    
    canvas.create_line(250, 250, 250+hx, 250-hy, fill='Blue', width = 10)

    mx = mr * math.sin(minute/360 * 3.14*2)
    my = mr * math.cos(minute/360 * 3.14*2)
    canvas.create_line(250, 250, 250+mx, 250-my, fill='Green', width = 6)    

    sx = sr * math.sin(second/360 * 3.14*2)
    sy = sr * math.cos(second/360 * 3.14*2)
    canvas.create_line(250, 250, 250+sx, 250-sy, fill='Red', width = 2)

    tk.update()
    canvas.delete("all")
    time.sleep(1)


#다른 방법
# 시계의 테두리가 포함된 프로그램
 
from tkinter import *
import time
import math

tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.configure(background='white')
canvas.pack()

width = 500
height = 500
cx = width/2        # center x
cy = height/2       # center y

sr = height/2-50    # radius for second hand
mr = height/2-80	# radius for minute hand
hr = height/2-110	# radius for hour hand

r = 480/2

while 1:
    t = time.localtime()       
    hour = (t[3] + t[4]/60)* 30
    minute = (t[4] + t[5]/60)*6
    second = t[5]*6

    canvas.delete("all")

    canvas.create_rectangle(225, 85, 275, 115, outline = 'Orange', width = 3)

    if t[3]>=0 and t[3]<12:
        twoday = 'AM'
    else:
        twoday = 'PM'
    
    canvas.create_text(250, 100, text = twoday)

    canvas.create_rectangle(210, 435, 290, 405, outline = 'Gray', width = 3)
   
    if t[6] == 0:
        day = '일'
    elif t[6] == 1:
        day = '월'
    elif t[6] == 2:
        day = '화'    
    elif t[6] == 3:
        day = '수'
    elif t[6] == 4:
        day = '목'
    elif t[6] == 5:
        day = '금'
    elif t[6] == 6:
        day = '토'

    date = str(t[1])+"월"+str(t[2])+"일"+"("+str(day)+")"

    canvas.create_text(250, 420, text = date, fill = 'Purple')


    for i in range(60):
        cetax = (r-10)*math.sin((6*i)/360*3.14*2)
        cetay = (r-10)*math.cos((6*i)/360*3.14*2)
        centx = (r-15)*math.sin((6*i)/360*3.14*2)
        centy = (r-15)*math.cos((6*i)/360*3.14*2)
        circlex = r*math.sin((6*i)/360*3.14*2)
        circley = r*math.cos((6*i)/360*3.14*2)
        if i % 5 == 0:
            canvas.create_line(cx+centx, cy-centy, cx+circlex, cy-circley, width = 4)
        else:
            canvas.create_line(cx+cetax, cy-cetay, cx+circlex, cy-circley, width = 2) 
    

    
    # clock outline
    canvas.create_arc(10,10,width-10,height-10, extent=359,style=CHORD, width = 2)

    # hour hand
    hx = hr * math.sin(hour/360 * 3.14*2)
    hy = hr * math.cos(hour/360 * 3.14*2)    
    canvas.create_line(cx, cy, cx+hx, cy-hy, fill='Blue', width = 10)

    # minute hand
    mx = mr * math.sin(minute/360 * 3.14*2)
    my = mr * math.cos(minute/360 * 3.14*2)
    canvas.create_line(cx, cy, cx+mx, cy-my, fill='Green', width = 6)    

    # second hand
    sx = sr * math.sin(second/360 * 3.14*2)
    sy = sr * math.cos(second/360 * 3.14*2)
    canvas.create_line(cx, cy, cx+sx, cy-sy, fill='Red', width = 2)

    # center circle
    canvas.create_arc(cx-10, cy-10, cx+10, cy+10, extent=359,style=CHORD, width = 2, fill = 'black')
    
    time.sleep(0.1)
    tk.update()
