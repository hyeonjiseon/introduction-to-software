#Frog 게임 프로그램
#tkinter, time, random모듈 사용
#아래 코드를 참고하여 <space>바를 눌러 게임 속도를 3단계로 조절
#속도 단계: normal -> fast -> faster -> normal
# canvas.bind_all('<space>', change_speed)
# def change_speed(evt):
# global game_speed...
#score와 life 사이에 현재 speed 표시

from tkinter import *
import time
import random

count = 0

class Frog:
    def __init__(self, canvas, car1, car2, car3, color): #개구리 초기위치로 이동, 객체 변수 초기화
        self.canvas = canvas
        self.car1 = car1
        self.car2 = car2
        self.car3 = car3

        self.id = canvas.create_oval(10,10,50,50, fill=color)
        self.canvas.move(self.id, 250, 420)
        self.x = 0
        self.y = 0
        self.step = 60
        self.score = 0
        self.life = 5

        self.game_speed = 'normal'

        self.canvas_width = self.canvas.winfo_width() #캔버스의 가로폭의 값 얻어오는 함
        self.canvas.bind_all('<KeyPress-Up>', self.move_up)
        self.canvas.bind_all('<KeyPress-Left>', self.move_left)
        self.canvas.bind_all('<KeyPress-Right>', self.move_right)

        self.canvas.bind_all('<space>', self.change_speed)

        canvas.create_text(90, 40, text = "score : "+str(self.score))
        canvas.create_text(400,40,text = "life : "+str(self.life))

        canvas.create_text(250, 40, text = "speed : "+str(self.game_speed))
        
    def hit_car(self, pos):
        car_pos = self.canvas.coords(self.car1.id)
        if pos[2] >= car_pos[0] and pos[0] <= car_pos[3]: #car의 x좌표 사이에 있음
            if pos[3] >= car_pos[1] and pos[1] <= car_pos[3]: #car의 위/아래 y가 frog 아래/위 y보다 더 위/아래에 있을 때 충돌
                return True
        car_pos = self.canvas.coords(self.car2.id)
        if pos[2] >= car_pos[0] and pos[0] <= car_pos[3]:
            if pos[3] >= car_pos[1] and pos[1] <= car_pos[3]:
                return True
        car_pos = self.canvas.coords(self.car3.id)
        if pos[2] >= car_pos[0] and pos[0] <= car_pos[3]:
           if pos[3] >= car_pos[1] and pos[1] <= car_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y) #개구리 객체를 현재 위치에서 x축 방향으로 x만큼, y축 방향으로 y만큼 이동
        self.x = 0 #x,y는 좌표가 아니라 현재 개구리 좌표로부터 떨어진 거리(offset)
        self.y = 0

        pos = self.canvas.coords(self.id)

        if pos[0]<=0:
            self.canvas.move(self.id, self.step/2, self.y)
            self.x=0
        elif pos[2] >= self.canvas_width:
            self.canvas.move(self.id, -self.step/2, self.y)
        elif pos[1] < 60: #개구리가 가장 상단에 도달
            self.score=self.score + 10
            canvas.create_rectangle(10,10,200,60, outline=tk.cget("bg"), fill=tk.cget("bg"))
            canvas.create_text(90,40,text="score : "+str(self.score))
            self.canvas.move(self.id, 250-pos[0], 420)

        if self.hit_car(pos) == True: #자동차에 충돌
            self.life = self.life-1
            
            if self.life <= 0:
                canvas.create_text(250, 260, text = "G A M E O V E R")
            else:
                canvas.create_rectangle(300, 10, 550, 60, outline=tk.cget("bg"), fill=tk.cget("bg"))
                canvas.create_text(400,40,text="life : "+str(self.life))
                self.canvas.move(self.id, 250-pos[0], 430-pos[1])

    def move_up(self, evt):
        self.y = -self.step

    def move_left(self, evt):
        self.x = -self.step/2

    def move_right(self, evt):
        self.x = self.step/2

    def change_speed(self, evt):
        global count
        count += 1

        if count % 3 == 0:

            car1.x = 5
            car2.x = -3
            car3.x = 1
            
            canvas.create_rectangle(200, 30, 300, 50, outline=tk.cget("bg"), fill=tk.cget("bg")) #tk.cget("bg") 배경화면과 동일한 색상
            self.game_speed = 'normal'
            canvas.create_text(250, 40, text = "speed : "+str(self.game_speed))

        if count % 3 == 1:

            car1.x = 10
            car2.x = -8
            car3.x = 6
            
            canvas.create_rectangle(200, 30, 300, 50, outline=tk.cget("bg"), fill=tk.cget("bg"))
            self.game_speed = 'fast'
            canvas.create_text(250, 40, text = "speed : "+str(self.game_speed))         

        if count % 3 == 2:
            car1.x = 15
            car2.x = -13
            car3.x = 11

            canvas.create_rectangle(200, 30, 300, 50, outline=tk.cget("bg"), fill=tk.cget("bg"))
            self.game_speed = 'faster'
            canvas.create_text(250, 40, text = "speed : "+str(self.game_speed))

class Car:
    def __init__(self, canvas, x, y, color, speed): #자동차 초기화 메소드
        self.canvas = canvas
        self.id = canvas.create_rectangle(10,10,100,60, fill = color)
        self.canvas.move(self.id, x, y)
        self.speed = speed
        self.x = speed
        self.y = 0

    def draw(self): #자동차 출력 메소드
        self.canvas.move(self.id, self.x, self.y)
        
        pos = self.canvas.coords(self.id)
        if pos[0] <= -100: #자동차가 오른쪽에서 왼쪽으로 이동하다가 x좌표가 -100보다 작으면 다시 오른쪽 방향으로 600만큼 이동시킨다.
            self.canvas.move(self.id, 600, 0)
        elif pos[2] >= 700: 
            self.canvas.move(self.id, -700, 0)

tk = Tk()
tk.title("Frog")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1) #여러 개의 윈도우 중에서 가장 상단에 놓이게 하는 데 필요한 명령어
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
tk.update()

car1 = Car(canvas, 10, 60, "red", 5)
car2 = Car(canvas, 500, 180, "green", -3)
car3 = Car(canvas, 10, 300, "yellow", 1)
frog = Frog(canvas, car1, car2, car3, "blue")

while 1:  
    if frog.life >= 0:
        car1.draw()
        car2.draw()
        car3.draw()
        frog.draw()
    
    tk.update_idletasks() #캔버스의 내용을 즉시 화면에 출력
    tk.update()
    time.sleep(0.01) #게임 속도 조절, 더 작은 값으로 하면 빨라짐
    
