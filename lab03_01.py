#난수로 발생된 숫자를 k번 안에 추측해서 맞추는 게임
import random #난수 발생
#입력값: 이름, 도전 횟수, 추측값
#추측값과 정답의 크기를 비교하여 'high' 또는 'low'로만 알려주기
#도전 횟수와 현재까지 시도한 횟수를 비교하여 남은 기회 알려주기

print('-'*30)
print("        하이-로우 게임")
print('-'*30)

name = input("이름을 입력하세요:")
k = int(input("도전 횟수를 입력하세요:"))
num = 1
answer = random.randrange(1,101)
#print(answer)


while num <= k:
    user = int(input(name+"님"+str(num)+"번째 추측 값을 입력해주세요(1~100):"))

    if user < answer:
        print(user, "는 정답보다 작습니다.")
        print(k-num, "번 기회가 남았습니다.\n")
        
        if num == k:
            print("더 이상 기회가 없습니다. 정답은", answer, "입니다.")
            break

        num = num+1
                       
        
    elif user > answer:
        print(user, "는 정답보다 큽니다.")
        print(k-num, "번 기회가 남았습니다.\n")
        
        if (num == k):
            print("더 이상 기회가 없습니다. 정답은", answer, "입니다.")
            break
        
        num = num+1
             
            
    elif user == answer:
        print(k-num, "번 기회가 남았습니다.\n")
        print("정답입니다.")
        break

if k == 0:
    print("0번 기회가 남았습니다.\n\n더 이상 기회가 없습니다. 정답은", answer, "입니다.")
                
    
#다른 방법
name = input("이름을 입력하세요:")
k = int(input("도전 횟수를 입력하세요:"))
answer = random.randint(1,100)
user = 0
num = 1
print(answer)

while user != answer and k>0:
    user = int(input(name+"님"+str(num)+"번째 추측 값을 입력해 주세요(1~100):"))

    if user<answer:
        print(user,"는 정답보다 작습니다.")
    elif user>answer:
        print(user,"는 정답보다 큽니다.")
    print(k-num, "번 기회가 남았습니다\n")

    if num == k:
        print("더 이상 기회가 없습니다. 정답은", answer, "입니다.")
        break
    num = num+1

if user == answer:
    print("정답입니다.")
if k==0:
    print("0번 기회가 남았습니다.\n\n더 이상 기회가 없습니다. 정답은", answer, "입니다.")
