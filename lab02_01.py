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
