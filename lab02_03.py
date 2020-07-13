#이차원 공간에서 두 점 (x1, y1)과 (x2, y2)를 사용자로부터 입력 받아 두 점 사이의 거리를 계산
import math #math 모듈 불러오기
#좌표는 int형으로 입력 받기
#math.sqrt(x): x 제곱근을 계산하여 반환
#math.pow(x,y): x의 y승을 계산하여 반환
#두 점 사이의 거리 공식: ((x2-x1)^2 + (y2-y1)^2)^1/2

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

