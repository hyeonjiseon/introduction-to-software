#https://pypi.python.org/pypi/eqsygui에서 tar.gz 다운로드
#easygui-0.98.1.tar 파일 압축 풀기
#python 설치 경로에 easygui 폴더 복사
#ex)C:\Users\(PC이름)\AppData\Local\Programs\Python\Pyton36-32\Lib
#AppData 폴더의 경우 숨김 폴더로 되어 있으니 숨김 폴더 볼 수 있게 설정하기

#S텔레콤 32요금제의 월 이용요금을 계산하는 프로그램
#기본 요금: 37400원 - 음성: 120분, 문자 200건, 데이터 800MB 기본 제공
#초과 요금: 음성 통화 1.98/초, 문자 22원/건, 데이터사용 55원/MB
#import easygui를 맨 위에 붙이기
#easygui.enterbox()로 각각 값 입력 받으 후 변수에 저장
#출력을 문자열 접합으로 하나의 스트링 변수에 저장 후 easygui.msgbox()로 출력. 줄바꿈은 '\n'사용
#입력 값: 이름, 음성통화시간(분), 문자 건수, 데이터 사용량(MB)

import easygui
name = easygui.enterbox("이름을 입력하세요")
time = int(easygui.enterbox("음성 통화시간(분)을 입력하세요"))
message = int(easygui.enterbox("문자 건수를 입력하세요"))
data = int(easygui.enterbox("데이터 사용량(MB)을 입력하세요"))

extime = 0
exmsg = 0
exdata = 0

if time>120 :
	extime = int((time - 120)*60*1.98)
if message>200:
	exmsg = (message - 200)*22
if data > 800:
	exdata = (data - 800)*55

total = 37400+extime+exmsg+exdata

easygui.msgbox("===="+name+"님의 4월 이용 요금====\n34요금제 기본 요금: 37400원\n음성통화 초과 요금:"+str(extime)+
               "원\n문자 초과 요금:"+str(exmsg)+"원\n데이터 사용 초과 요금:"+str(exdata)+"원\n"+'='*30+"\n총 요금:"+str(total)+"원")



#다른 풀이
import easygui
name = easygui.enterbox("이름을 입력하세요")
call = easygui.enterbox("음성 통화시간(분)을 입력하세요")
messg = easygui.enterbox("문자 건수를 입력하세요")
data = easygui.enterbox("데이터사용량(MB)을 입력하세요")

if int(call)<120: etrcall=0
elif int(call)>=120: etrcall = int((int(call) - 120) * 60 * 1.98)


if int(messg)<200: etrmessg=0
elif int(messg)>=200: etrmessg = (int(messg) - 200) * 22

if int(data)<800: etrdata=0
elif int(data)>=800: etrdata = (int(data) - 800) * 55

total = 37400 + int(etrcall) + int(etrmessg) + int(etrdata)


total = easygui.msgbox("====정혜인님의 4월 이용요금====\n" + "34요금제 기본 요금: 37400원\n"
                       + "음성통화 초과 요금:" + str(etrcall) + "원\n" +
                       "문자 초과 요금:" + str(etrmessg) + "원\n"
                       + "데이터 사용 초과 요금:" + str(etrdata) + "원\n"
                       + "=================================\n"
                       + "총 요금:" + str(total) + "원")
