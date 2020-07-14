#점선으로 사각형 그리기
import turtle
turtle.setup(width=500, height=500)
t=turtle.Pen()
t.pencolor("dark green")
t.width(3)
edges=4
length=500
dot_size=length/20

for i in range(edges):
    for j in range(edges):
        t.forward(dot_size)
        t.up() #펜을 들어서 이동
        t.forward(dot_size)
        t.down() #펜을 내려서 그리기 시작
    t.right(90)

#점이 더 작게
t.pencolor("red")
for i in range(edges):
    for j in range(edges*2):
        t.forward(dot_size/2)
        t.up()
        t.forward(dot_size/2)
        t.down()
    t.right(90)
