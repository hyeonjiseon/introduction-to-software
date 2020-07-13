#break문을 사용하여 일 최고 기온 리스트에서 특정 기온을 찾는 프로그램

temps = [27.9, 29.3, 21.3, 29.9, 29.6, 32.5, 29.7, 26.3, 31.8, 34.3,
         36.0, 28.0, 24.9, 31.4, 33.9, 28.9, 21.6, 27.8, 29.8, 31.2,
         29.6, 31.7, 32.1, 24.4, 26.4, 30.0, 30.0, 31.2, 28.8, 33.1, 32.4]

target = float(input("찾고자 하는 기온: "))
index = 0
while index < len(temps):
    if temps[index] == target:
        break
    index += 1
if index < len(temps):
    print("찾음 : %d 일" %(index+1))
else:
    print("찾지 못함")
