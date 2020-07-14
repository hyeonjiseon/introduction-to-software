#미로 만들기
#거북 아이콘을 윈도우의 중앙에 위치시킨 다음,
#시계 반대 방향으로 거북이 회전할 때마다 이동 경로를 증가시킨다.
#left(90)회전, for문과 range의 증가값을 이ㅛㅇㅇ하여 선분의 길이를 8씩 증가

import turtle
turtle.setup(width=50, height=500)
t=turtle.Pen()
t.pencolor("red")
t.width(3)
for i in range(0, 301, 8):
    t.forward(i)
    t.left(90)

#제일 처음 값이 0이라 처음에 북쪽으로 간 건 두 번째 값
#동쪽부터 시작하려면 (8, 309, 8)
