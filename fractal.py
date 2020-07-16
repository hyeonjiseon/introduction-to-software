#프랙탈 삼각형
from tkinter import*
import random
import time

tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.configure(background='light gray')
canvas.pack()
x=250
y=250
for i in range(50000):
    dice = random.randint(1,3)

    if dice == 1: #C
        px=250
        py=50
        mycolor='red'
    elif dice == 2: #B
        px = 50
        py = 450
        mycolor = 'green'
    else: #A
        px = 450
        py=450
        mycolor = 'blue'

    x=(x+px)/2
    y=(y+py)/2
    canvas.create_line(x, y, x+1, y+1, fill=mycolor)
    tk.update()
    time.sleep(0.005)
