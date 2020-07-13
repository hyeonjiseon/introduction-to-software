#오각형 그리기
import turtle
turtle.setup(width=600, height=600)
t=turtle.Pen()

t.pencolor("blue")
t.width(10)

for i in range(5):
    t.forward(150)
    t.right(72)

t.pencolor("yellow")

for i in range(5):
    t.forward(150)
    t.left(72)

t.pencolor("red")
t.left(108)
t.forward(100)

for i in range(4):
    t.right(72)
    t.forward(100)
    
   
    
