import math

firstx = int(input("첫 번째 x좌표 입력:"))
firsty = int(input("첫 번째 y좌표 입력:"))
secondx = int(input("두 번째 x좌표 입력:"))
secondy = int(input("두 번째 y좌표 입력:"))

distance = math.sqrt(math.pow(secondx-firstx, 2)+math.pow(secondy-firsty, 2))
print("두 점 사이의 거리:", distance)

#다른 방법
x = secondx-firstx
y = secondy-firsty
distance = math.sqrt(math.pow(x,2)+math.pow(y,2))

