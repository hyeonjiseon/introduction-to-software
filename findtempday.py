#특정 기온을 입력받아 그 이상인 날을 찾는 프로그램

temps = [27.9, 29.3, 21.3, 29.9, 29.6, 32.5, 29.7, 26.3, 31.8, 34.3,
         36.0, 28.0, 24.9, 31.4, 33.9, 28.9, 21.6, 27.8, 29.8, 31.2,
         29.6, 31.7, 32.1, 24.4, 26.4, 30.0, 30.0, 31.2, 28.8, 33.1, 32.4]

day = 0
count = 0
days = []
target = int(input("몇도 이상인 날들을 찾고 싶으세요? "))
for t in temps:
    day = day + 1
    if t >= target:
        count += 1
        days.append(day)
print("%d 도 이상인 날: %d 일" %(target, count))
print('-'*20)
for day in days:
    print("%2d 일: %.1f" %(day, temps[day-1]))
