#가위바위보 프로그램
#5판 3선승제
#컴퓨터가 낸 가위/바위/보는 random.randint(1,3)사용
#비길 경우에는 점수 변동 없이 다시 가위바위보 진행
#사용자나 컴퓨터 중 한 명이라도 3점을 먼저 따면 게임이 종료되며 결과 출력

import easygui
import random #난수 발생

co = 0
us = 0
n = 1

while co != 3 and us != 3 :
    
    user = easygui.buttonbox(str(n)+"번째 판\n"+"가위 바위 보 중 하나를 선택하세요", choices = ['가위', '바위', '보'])
    computer = random.randint(1,3)

    if computer == 1:
        computer = '가위'
    elif computer == 2:
        computer = '바위'
    else:
        computer = '보'

    if (computer == '가위' and user == '가위') or (computer == '바위' and user == '바위') or (computer == '보' and user == '보'):
        game = easygui.msgbox("모두 "+user+"을 냈습니다. 비겼습니다.\n컴퓨터 "+str(co)+" : "+str(us)+"사용자")

    elif (computer == '가위' and user == '바위') or (computer == '바위' and user == '보') or (computer == '보' and user == '가위'):
        us += 1
        game = easygui.msgbox("컴퓨터는 "+str(computer)+"를 냈습니다. 당신이 이겼습니다.\n컴퓨터 "+str(co)+": "+str(us)+" 사용자")
        n += 1
    else:
        co += 1
        game = easygui.msgbox("컴퓨터는 "+str(computer)+"를 냈습니다. 당신이 졌습니다.\n컴퓨터 "+str(co)+": "+str(us)+" 사용자")
        n += 1

if co == 3:
    resul = easygui.msgbox("컴퓨터 "+str(co)+" : "+str(us)+"사용자\n컴퓨터가 우승했습니다.")
else:
    resul = easygui.msgbox("컴퓨터 "+str(co)+" : "+str(us)+"사용자\n당신이 우승했습니다.")
