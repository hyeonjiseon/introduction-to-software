#다양한 색을 사용하여 육각형 벌집 7개 그리기
#pencolor를 사용하여 다양한 색 지정(무작위 숫자는 random.random()으로 받아옴)
#육각형 한 변의 길이만큼 이동한 후, 회전시켜 다시 육각형 그리기

import random
import turtle

t=turtle.Pen()
t.width(3)


for i in range(6):
    for j in range(6):
        t.pencolor(random.random(), random.random(), random.random())
        t.forward(50)
        t.left(60)
    t.forward(50)
    t.right(60)
