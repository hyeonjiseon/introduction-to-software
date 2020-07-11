import math

print('*'*50)
print("         숙명여자대학교 4월 단기 주차장")
print("       (24시간 이상 주차하실 수 없습니다.)")
print('*'*50)
print()

car = input("차량 번호를 입력하세요: ")

while True:
    inhour = int(input("들어온 시간을 입력하세요(0-23): "))
    inmin = int(input("들어온 분을 입력하세요(0-59): "))
    outhour = int(input("나간 시간을 입력하세요(0-23): "))
    outmin = int(input("나간 분을 입력하세요(0-59): "))

    if 0 <= inhour <= 23 and 0 <= outhour <= 23 and 0 <= inmin <=59 and 0 <= outmin <= 59:
        print()
        break     
        
    else:
        print('-'*50)
        print("입력 오류입니다. 범위를 맞추어 다시 입력해 주세요.")
        print('-'*50)
       
print('='*50)
print("        '"+str(car)+"' 차량 주차료 명세서")
print('='*50)

print("입차 시간 : "+str(inhour)+"시 "+str(inmin)+"분")
print("출차 시간 : "+str(outhour)+"시 "+str(outmin)+"분")


firstmin = (60-inmin) + (23-inhour)*60
secmin = outhour*60 + outmin

if outmin - inmin > 0:
    remin = outmin - inmin
    if outhour - inhour > 0:
        rehour = outhour - inhour

        tomin = rehour*60+remin

        if tomin <= 30:
            tocash = 1500
        elif 30 < tomin <= 292.5:
            tocash = 1500 + 600 * (tomin - 30 )/15
        else:
            tocash = 12000    
        
    else:
        rehour = 24-inhour+outhour

        if firstmin <= 30:
            fcash = 1500
        elif 30 < firstmin <= 292.5:
            fcash = 1500 + 600 * (firstmin - 30 )/15
        else:
            fcash = 12000

        if secmin <= 30:
            scash = 1500
        elif 30 < secmin <= 292.5:
            scash = 1500 + 600 * (secmin - 30 )/15
        else:
            scash = 12000

        tocash = fcash + scash
        
else:
    remin = 60-inmin+outmin
    if outhour - inhour > 0:
        rehour = outhour - inhour - 1

        tomin = rehour*60+remin

        if tomin <= 30:
            tocash = 1500
        elif 30 < tomin <= 292.5:
            tocash = 1500 + 600 * (tomin - 30 )/15
        else:
            tocash = 12000

        
    else:
        rehour = 24-inhour+outhour-1

        if firstmin <= 30:
            fcash = 1500
        elif 30 < firstmin <= 292.5:
            fcash = 1500 + 600 * (firstmin - 30 )/15
        else:
            fcash = 12000

        if secondmin <= 30:
            scash = 1500
        elif 30 < secmin <= 292.5:
            scash = 1500 + 600 * (secmin - 30 )/15
        else:
            scash = 12000

        tocash = fcash + scash

tomin = rehour*60+remin

print("주차 시간 : "+str(rehour)+"시간 "+str(remin)+"분("+str(tomin)+"분)")
print('-'*50)
print("주차 요금: "+str(math.ceil(tocash))+"원")


#다른 풀이
import math

print('*'*55)
print('         숙명여자대학교 4월 단기 주차장')
print("        (24시간 이상 주차하실 수 없습니다.)")
print('*'*55)
print()

name=input("차량 번호를 입력하세요: ")

while True:
    in_hour = int(input("들어온 시간을 입력하세요(0-23): "))
    in_min = int(input("들어온 분을 입력하세요(0-59): "))
    out_hour = int(input("나간 시간을 입력하세요(0-23): "))
    out_min = int(input("나간 분을 입력하세요(0-59): "))
    if 0<=in_hour<=23 and 0<=in_min<=59 and 0<=out_hour<=23 and 0<=out_min<=59:
        break
    else:
        print('-'*55)
        print("입력 오류입니다.범위를 맞추어 다시 입력해 주세요.")
        print('-'*55)

d_hour = out_hour - in_hour
d_min = out_min - in_min

if d_min < 0:
    d_hour -= 1
    d_min += 60

#자정을 넘기는 경우
if d_hour < 0:
    d_hour +=24
    first_day_min = 0 - inmin
    first_day_hour = 24 - in_hour
    if first_day_min < 0:
        first_day_min += 60
        first_day_hour -= 1

    second_day_min = out_min
    second_day_hour = out_hour

    first_day_minute = first_day_hour*60 + first_day_min
    second_day_minute = second_day_hour*60 + second_day_min
    minute = first_day_minute + second_day_minute

    #첫째 날
    if first_day_minute == 0:
        first_day_fee = 0
    elif 0 < first_day_minute < 30:
        first_day_fee = 1500
    else:
        fisrt_day_fee = 1500 + math.ceil((first_day_minute -30)/15)*600

    if first_day_fee > 12000: #하루 최대 12000원을 넘지 않게
        first_day_fee = 12000

    #둘째 날
    if second_day_minute == 0:
        second_day_fee = 0
    elif 0<second_day_minute <30:
        second_day_fee = 1500
    else:
        second_day_fee = 1500 + math.ceil((second_day_minute - 30)/15)*600

    if second_day_fee > 12000: #하루 최대 12000원을 넘지 않게
        second_day_fee = 12000

    fee = first_day_fee + second_day_fee

#자정을 넘기지 않는 경우
else:
    minute = d_hour*60 + d_min
    if minute == 0:
        fee = 0
    elif 0 < minute < 30:
        fee = 1500
    else:
        fee = 1500 + math.ceil((minute-30)/15)*600

    if fee>12000:
        fee = 12000

print()
print('='*55)
print("             '"+name+"' 차량 주차료 명세서")
print('='*55)
print("입차 시간 : "+str(in_hour)+"시"+str(in_min)+"분")
print("출차 시간 : "+str(out_hour)+"시"+str(out_min)+"분")
print("주차 시간 : "+str(d_hour)+"시"+str(d_min)+"분("+str(minute)+"분)")
print("-"*55)
print("주차 요금 :"+str(fee)+"원")


#또 다른 풀이
import math
print("*******************************************************")
print("             숙명여자대학교 4월 단기 주차장")
print("          (24시간 이상 주차하실 수 없습니다.)")
print("*******************************************************")
print("")

while True:
 name = input("차량 번호를 입력하세요: ")
 enterhour = int(input("들어온 시간을 입력하세요(0-23): "))
 entermin = int(input("들어온 분을 입력하세요(0-59): "))
 leavehour = int(input("나간 시간을 입력하세요(0-23): "))
 leavemin = int(input("나간 분을 입력하세요(0-59): "))
 print("------------------------------------------------------")

 if (enterhour >= 0 and enterhour <= 23) or (leavehour >= 0 and leavehour <= 23) or (entermin >=0 and entermin <= 59) or (leavemin >=0 and leavemin <= 59):
     break
 else:
     print("입력 오류입니다. 범위를 맞추어 다시 입력해 주세요.")
     
print("")
print("=======================================================")
print(          "'", name, "'", "차량 주차료 명세서")
print("=======================================================")
print("입차 시간 : ", enterhour, "시", entermin, "분")
print("출차 시간 : ", leavehour, "시", leavemin, "분")

if leavemin - entermin >= 0:
    parkingmin = leavemin - entermin
    if leavehour - enterhour >= 0:
        parkinghour = leavehour - enterhour
    else:
        parkinghour = leavehour - enterhour + 24
else:
    parkingmin = leavemin - entermin + 60
    if leavehour - enterhour >= 0:
        parkinghour = leavehour - enterhour -1
    else:
        parkinghour = leavehour - enberhour + 23
parkminute = parkinghour * 60 + parkingmin
print("주차 시간 : ", parkinghour, "시간 ", parkingmin, "분(", parkminute, "분)")
print("------------------------------------------------------")

if leavehour - enterhour >= 0:
    if parkminute > 0 and parkminute <=30:
        fee = 1500
    elif parkminute < 293:
        fee = 1500 + math.ceil((parkminute - 30)/15)*600
    else:
        fee = 12000
else:
    firstday= 1500 + math.ceil((23 - enterhour)*60 + (60 - entermin)/15)*600
    seconday= 1500 + math.ceil((leavehour*60 + leavemin)/15)*600
        fee = firstday + seconday

print("주차 요금 : ", fee, "원")

