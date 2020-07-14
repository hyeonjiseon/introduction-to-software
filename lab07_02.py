#파이썬 사전을 이용하여 영한사전 구현하기
#단어 입력, 조회/수정, 삭제, 전체 단어 출력, 단어 시험, 종료로 구성
#단어 입력
# 1) 빈 칸인 상태에서 엔터키 눌렀을 경우 입력 종료
# 2) 단어가 사전에 존재하는지 확인한 후 저장
# 3) 사전에 이미 존재하는 단어일 경우 "이미 존재하는 단어입니다" 출력 후 재입력
#단어 조회/수정
# 1) 단어가 사전에 존재하는지 확인 후 출력
# 2) 수정할 경우 단어와 뜻 재입력, 수정하지 않을 경우 조회/수정 종료
# 3) 단어가 존재하지 않는 경우 "000은(는) 사전에 존재하지 않습니다." 출력 후 조회/수정 종료
#단어 삭제
# 1) 사전에 존재할 경우 삭제
# 2) 사전에 존재하지 않을 경우 삭제 종료
#전체 단어 출력: 사전에 존재하는 모든 단어 출력
#단어 시험: 사전에 존재하는 단어 보고 뜻 맞추는 시험
#종료: "이용해 주셔서 감사합니다." 출력 후 종료

voca = {}

while True:
    print('='*50)
    print("                   영한사전")
    print('='*50)
    print("1. 단어 입력\n2. 단어 조회/수정\n3. 단어 삭제\n4. 전체 단어 출력\n5. 단어 시험\n6. 종료")
    print('='*50)
    select = int(input("선택 : "))

    if select == 1:
        print()
        print("저장할 단어를 입력하세요. 끝내시려면 엔터키를 눌러주세요.\n")

        while True:
            eng = input("단어 :")
            
            if len(eng) == 0:
                break
            else:
                if eng in voca.keys():
                    print("이미 존재하는 단어입니다.\n")
                else:
                    kor = input("뜻 :")
                    print()
                    voca[eng]=kor
            
    elif select == 2:
        print()
        print("찾으실 단어를 입력하세요.")
        ineng = input("단어 : ")

        if ineng in voca:
            print('-'*50)
            print(ineng, ":", voca[ineng])
            print('-'*50)
            remo = input("수정하시겠습니까?[Y/N] : ")
            if remo == 'Y':
                reng = input(str(ineng)+":")
                voca[ineng]=reng
            print()
        else:
            print(ineng, "은(는) 사전에 존재하지 않습니다.\n")

    elif select == 3:
        print()
        print("삭제할 단어를 입력하세요.")
        deng = input("단어 : ")
        if deng in voca:
            del voca[deng]
            print("삭제되었습니다.\n")
        else:
            print(deng,"은(는) 사전에 존재하지 않습니다.\n")

    elif select == 4:
        print('-'*50)
        for e, k in voca.items():
            print(str(e),"\t",str(k))
        print('-'*50)
        print()

    elif select == 5:
        count = 0
        print()
        if len(voca) == 0:
            print("단어가 존재하지 않아 시험이 불가능합니다\n")
        else:            
            for e, k in voca.items():
                et = input(str(e)+":")
                if et == k:
                    print("정답입니다.\n")
                    count += 1
                else:
                    print("오답입니다.\n")
            print()
            print("총 "+str(count)+"개 정답입니다.\n")

    elif select == 6:
        print()
        print("이용해 주셔서 감사합니다.")
        break
    else:
        print()
        print("잘못 입력했습니다. 다시 선택해주세요.")
