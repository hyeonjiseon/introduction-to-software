#음식 가격에 세금과 팁을 포함한 총 지불 금액 계산
#세금: 입력 받은 음식 가격의 10.5%
#팁: 입력 받은 음식 가격의 15%
#사용자로부터 입력 받을 값: 음식 가격

food = int(input("음식 가격을 입력하세요"))
cash = food*0.105+food*0.15+food
print("지불 총액은", cash, "원 입니다.")


#또 다른 예
tax=0.105
tip=0.15
total = cost + cost*tax/100 + cost*tip/100

#또 다른 예2
tax = 10.5
tip = 15
total = cost + cost*tax/100 + cost*tip/100

#또 다른 예3
total = cost + cost*0.205
