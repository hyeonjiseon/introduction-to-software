#주사위 예제
#주사위를 각각 100번, 1000번, 10000번 던져서 주사위의 각 눈이 나오는 횟수와 비율을 계산

import random

for n in [100, 1000, 10000]:
    count = [0, 0, 0, 0, 0, 0]
    print('\n')
    print("# of throws : ", n)
    for i in range(n):
        eye = random.randint(1, 6)
        count[eye - 1] = count[eye - 1] + 1

    print(count)
    for i in range(len(count)):
        print("%4.1f" % float(count[i] / n*100), '% ', end = ' ')
