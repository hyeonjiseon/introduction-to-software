import random

print('-'*30)
print("        하이-로우 게임")
print('-'*30)

name = input("이름을 입력하세요:")
k = int(input("도전 횟수를 입력하세요:"))
num = 1
answer = random.randrange(1,101)
#print(answer)


while(num <= k):
    user = int(input(print(name,"님", num, "번째 추측 값을 입력해주세요(1~100):")))

    if (user < answer):
        print(user, "는 정답보다 작습니다.")
        if(num == k):
            print("더 이상 기회가 없습니다. 정답은", answer, "입니다.")
            break
        else:
            print(k-num, "번 기회가 남았습니다.\n")
            num = num+1
        
    elif (user > answer):
        print(user, "는 정답보다 큽니다.")
        if(num == k):
            print("더 이상 기회가 없습니다. 정답은", answer, "입니다.")
            break
        else:
            print(k-num, "번 기회가 남았습니다.\n")
            num = num+1
    elif (user == answer):
        print("정답입니다.")
        break
        
    
