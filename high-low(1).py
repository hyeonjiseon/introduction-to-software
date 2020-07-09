import random
answer = random.randint(1,100) #1~100 사이의 난수 발생
num = 0
times = 6

while num != answer and times > 0:
    num = int(input("값을 입력하세요:"))
    if num < answer:
        print("정답보다 작습니다.")
    elif num > answer:
        print("정답보다 큽니다.")
    times = times - 1
    print(times, "번 기회가 남았습니다.")
    print()

if num == answer:
    print("정답입니다.")
else:
    print("더이상 기회가 없습니다. 정답은", answer)
