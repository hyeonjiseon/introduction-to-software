#N개의 정수를 입력 받아 리스트 저장 후, 최대값, 최소값, 중간값과 순위 출력
#숫자 입력을 마치면 리스트 출력 후 최대값, 최소값, 중간값 순위 출력
#중간값 출력 시
# 1) 짝수 개의 정수를 입력 받은 경우: 중간 두 수의 평균을 출력
# 2) 홀수 개의 정수를 입력 받은 경우: 중간에 위치한 숫자 출력
#숫자 아무것도 입력하지 않고 처음부터 엔터만 눌렀을 경우: "숫자가 존재하지 않습니다" 출력
#sort()로 내림차순 정렬
#입력한 점수들로 순위 매기기
# 예) 100, 100, 100, 40, 50, 50을 점수로 넣었을 때
#     : 1위 100점 1위 100점 1위 100점 4위 50점 4위 50점 6위 40점
# <힌트>
# 1) 순위를 세는 변수 생성(예: rank)
# 2) 같은 숫자가 몇 개 있는지 세는 변수 생성(예: sameScoreCount)

numArray = []

while True:
    number = input("숫자를 입력해 주세요. 끝내시려면 엔터키를 눌러주세요.\n")
    if len(number) == 0:           
        break
    else:
        numArray.append(int(number))
        

if len(numArray) == 0:
    print("숫자가 존재하지 않습니다.")

else:
    numArray.sort(reverse = True)
    print(numArray)
    print('='*50)

    print("최대값 ", numArray[0])
    print("최소값 ", numArray[len(numArray)-1])    

    #중간값
    if len(numArray)%2 == 0: #중간에 두 개 평균
        print("중간값 ", (numArray[len(numArray)//2-1]+numArray[len(numArray)//2])/2)
    else: #가운데 있는 것
        print("중간값 ", numArray[len(numArray)//2])

    print('='*50)
    print("점수판")
    print('='*50)

    rank = 1
    hide = 0

    for i in range(len(numArray)):
        print(str(rank)+"위\t"+str(numArray[i])+"점")
        if i < len(numArray)-1:
            if numArray[i] == numArray[i+1]:
                hide += 1
            else:
                rank = rank + 1 + hide
                hide = 0
        else:
            continue

#다른 방법
scores = []

while True:
    print("숫자를 입력해 주세요. 끝내시려면 엔터키를 눌러주세요.")
    score = input()
    
    if len(score) == 0:
        break
    scores.append(int(score))
    
if len(scores) == 0:
    print("숫자가 존재하지 않습니다.")
else:
    scores.sort(reverse = True)
    print(scores)
    print("="*50)
    innum = len(scores)
    print("최대값 :", scores[0])
    print("최소값 :", scores[innum - 1])

    if len(scores)%2 == 0:
        print("중간값 :", (scores[int(innum/2-1)]+scores[int(innum/2)])/2)
    else:
        print("중간값 :", scores[innum//2])
    print("="*50)
    print("점수판")
    print("="*50)

    rank = 0
    
    sameScoreCount = 0
    for x in range(len(scores)):
        rank=1+x
        if x==0:
           print(str(rank)+"위"+"\t"+str(scores[x])+"점")
        elif scores[x-1]==scores[x]:
            sameScoreCount+=1
            print(str(rank-sameScoreCount)+"위"+"\t"+str(scores[x])+"점")
        else:
            sameScoreCount=0
            print(str(rank)+"위"+"\t"+str(scores[x])+"점")


