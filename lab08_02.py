#random과 time 모듈을 이용한 미니 게임
#from 모듈이름 import 함수이름 사용
# 예) randint() 사용하려면 from random import randint
#     이렇게 하면 random.randint()라고 안 쓰고 randint()라고만 써도 사용 가능
#메뉴 잘못 입력 시 다시 입력 받기
#최단 시간을 100000으로 초기화

#타자 게임(영어 단어)
# 1) 횟수, 단어리스트를 매개변수로 가지는 함수
# 2) 횟수는 10번으로 제한
# 3) words.txt 파일에서 단어들 불러와 섞은 뒤 앞의 10개의 단어로 게임 진행
#    random 모듈에 존재하는 shuffle() 함수 사용하여 리스트 섞기
#    예) a=['x','y','z'] shuffle(a) -> a의 내용이 섞임
# 4) 리스트에서 차례대로 값을 꺼내 타자 게임 진행
# 5) 오타 시 재입력 받기
# 6) time 모듈에 존재하는 time() 함수 사용하여 타자 시간 출력(소수점 둘째 자리까지)
#    시작하는 시간과 끝나는 시간을 기록하여 둘을 빼기
#    예) start=time() end=time() print(end-start) -> 걸린 시간 출력됨
# 7) words.txt파일에 있는 기록과 비교하여 시간이 더 짧을 경우 기록 갱신

#단어 추가
# 1) 빈 칸만 입력할 때까지 단어 입력
# 2) 파일입출력으로 words.txt라는 파일에 최단 시간과 단어 저장
#   - words.txt 파일에 첫째 줄에는 게임의 최단 시간 기록
#   - 둘째 줄부터는 입력 받은 단어들 나열

from random import shuffle
from time import time

mymemo = []

#처음에 시작할 때 메모장을 열어서 100000이라고 적힌 words.txt파일 만들기
f=open('words.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    line = line.strip()
    mymemo.append(line)


shortime = mymemo[0]

def game():
    round = 1
    global shortime

    
    if len(mymemo) < 10:
        print("단어가 10개 미만입니다. 단어를 추가한 뒤에 게임을 실행할 수 있습니다.")
    else:
        print("준비되면 엔터!\n")
        input()

        question = mymemo[1:11]
        shuffle(question)
                
        start = time()

        for answer in question:
            print("START!", round)
            print(answer)
            follow = input()

            if follow == answer:
                print("[정타]\n")
                round += 1
            else:
                print("[오타]\n")

                while True:

                        print("START!", round)
                        print(answer)
                        follow = input()

                        if follow != answer:
                            print("[오타]\n")
                            continue
                        
                        else:
                            print("[정타]\n")
                            round += 1
                            break
                        
        end = time()

        newtime = end-start        
       
        if float(shortime) > float(newtime):
            shortime = newtime
            print("타자 시간: ", '%.2f' % float(shortime), "초")
            print("***신기록 달성!***")
        else:
            print("타자 시간: ", '%.2f' % float(shortime), "초")

def add():
    while True:
        word = input("추가할 단어를 입력하세요. 끝내려면 엔터를 두 번 입력하세요.\n단어 : ")
        
        if len(word) == 0:            
            print("저장 완료")
            #mymemo.pop()
            print(mymemo)
            break
        mymemo.append(word)
    f.close()
    
while True:
    print('='*60)
    print("1. 타자 게임(영어 단어)\n2. 단어 추가\n0. 종료")
    print("최단 기록 :", '%.2f' % float(shortime),"초")
    print('='*60)
    select = input("선택 : ")

    if select == '1':
        game()
    elif select == '2':
        add()
    elif select == '0':
        f=open('words.txt', 'w')
        f.write(str(shortime))
        for item in mymemo:
            msg = item + '\n'
            f.write(msg)
        f.close()
        print("게임을 종료합니다.")    
        break
    else:
        print("잘못 입력했습니다. 다시 입력해 주세요.")
