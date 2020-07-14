#과세 표준 금액을 입력 받아 근로소득세를 계산하는 프로그램
#빈칸을 입력했을 시 프로그램 종료
#계산 예시: 2000만원을 입력 시 72+(2000-1200)*0.15

while True:

    cash = input("과세 표준 금액을 입력하세요(만원 단위):")

    if len(cash) == 0:
        print("프로그램을 종료합니다.")
        break
    
    else:
        cash = int(cash)

        if 0 <= cash <= 1200:
            cash = cash*0.06
            print("근로소득세는", int(cash), "만원 입니다.")
            print('='*30)
            
        elif 1200 < cash <= 4600:
            cash = 72 + (cash - 1200) * 0.15
            print("근로소득세는", int(cash), "만원 입니다.")
            print('='*30)
            
        elif 4600 < cash <= 8800:
            cash = 582 + (cash - 4600)*0.24
            print("근로소득세는", int(cash), "만원 입니다.")
            print('='*30)
            
        elif 8800 < cash < 30000:
            cash = 1590 + (cash - 8800) * 0.35
            print("근로소득세는", int(cash), "만원 입니다.")
            print('='*30)
            
        elif cash > 30000:
            cash = 9010 + (cash - 30000)*0.38
            print("근로소득세는", int(cash), "만원 입니다.")
            print('='*30)

        else:
            print("잘못 입력했습니다.")
            print('='*30)

           
#다른 풀이
            
while True:

    cash = input("과세 표준 금액을 입력하세요(만원 단위):")

    if len(cash) == 0:
        print("프로그램을 종료합니다.")
        break
    
    else:
        cash = int(cash)

        if cash <= 1200:
            cash = cash*0.06
            
        elif 1200 < cash <= 4600:
            cash = 72 + (cash - 1200) * 0.15
            
        elif 4600 < cash <= 8800:
            cash = 582 + (cash - 4600)*0.24
            
        elif 8800 < cash < 30000:
            cash = 1590 + (cash - 8800) * 0.35
            
        elif cash > 30000:
            cash = 9010 + (cash - 30000)*0.38
           
        print("근로소득세는", int(cash), "만원 입니다.")
        print('='*30)
       
       




