#어느 해 7월의 최고 기온 찾기 프로그램

temps = [27.9, 29.3, 21.3, 29.9, 29.6, 32.5, 29.7, 26.3, 31.8, 34.3,
         36.0, 28.0, 24.9, 31.4, 33.9, 28.9, 21.6, 27.8, 29.8, 31.2,
         29.6, 31.7, 32.1, 24.4, 26.4, 30.0, 30.0, 31.2, 28.8, 33.1, 32.4]

day = 0
maxday = 0
max = -100
for t in temps:
    day = day + 1
    if t > max:
        maxday = day
        max = t
print("월 최고 기운 %d 일 : %.1f 도" %(maxday, max))