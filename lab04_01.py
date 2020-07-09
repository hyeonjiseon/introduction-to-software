print('◆'*25)
print("                 숙명은행 ATM")
print('◆'*25)

name = input("계좌 소유자 이름을 입력하세요: ")
print("="*49)
money = 100000


while True :

    print("1. 입금\n2. 출금\n3. 잔액 확인\n4. 종료")
    print('-'*49)

    choice = int(input("선택: "))
    print("="*49)

    if choice == 1:
        inmoney = int(input("입금액: "))
        money = money + inmoney
        print(str(inmoney)+"원이 입금되었습니다.")
        print("="*49)
    
    elif choice ==2:
        outmoney = int(input("출금액: "))
        if outmoney > money and outmoney >0:
            print("잔액이 부족합니다. 인출이 이루어지지 못했습니다.")
            print('-'*49)

        elif outmoney <= money and outmoney > 0:
            money = money - outmoney
            print(outmoney, '원이 인출되었습니다.')
            print('-'*49)

        elif outmoney <= 0:
            print("출금액을 정확히 입력하세요.")
            print("="*49)
        
    elif choice == 3:
        print(name, "님의 현재 잔액은", money, "원 입니다.")
        print("="*49)

    elif choice == 4:
        print("이용해 주셔서 감사합니다.")
        break
