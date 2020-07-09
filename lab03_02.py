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
elif int(call)>=120: etrcall = (int(call) - 120) * 60 * 1.98


if int(messg)<200: etrmessg=0
elif int(messg)>=200: etrmessg = (int(messg) - 200) * 22

if int(data)<800: etrdata=0
elif int(data)>=800: etrdata = (int(data) - 800) * 55

total = int(call) + int(etrcall) + int(messg) + int(etrmessg) + int(data) + int(etrdata)


total = easygui.msgbox("====정혜인님의 4월 이용요금====\n" + "34요금제 기본 요금: 37400원\n"
                       + "음성통화 초과 요금:" + str(etrcall) + "원\n" +
                       "문자 초과 요금:" + str(etrmessg) + "원\n"
                       + "데이터 사용 초과 요금:" + str(etrdata) + "원\n"
                       + "=================================\n"
                       + "총 요금:" + str(total) + "원")
