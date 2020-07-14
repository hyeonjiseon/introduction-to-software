#은행 ATM
#계좌 소유주 이름과 원하는 업무(입금/출금/잔액확인/종료)를 입력 받아 계산하는 프로그램
#현재 잔액: 100,000원
#반복문 이용하여 업무 선택

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
    else:
        print("1~4 중에서 입력해주세요")


#다른 풀이
print('◆'*40)
print("           숙명은행 ATM            ")
print('◆'*40)
name = input("계좌 소유자 이름을 입력하세요: ")
total = 100000
select = 0

while True:
    print('='*40)
    print("1. 입금\n" + "2. 출금\n" + "3. 잔액 확인\n" + "4. 종료\n" + '-'*40)
    select = int(input("선택: "))
    print('='*40)
    if select == 1:
        money_in = int(input("입금액: "))
        total = total + money_In
        print(str(money_in)+"원이 입금되었습니다.")
    elif select == 2:
        money_out = int(input("출금액: "))
        if money_out > total:
            print("잔액이 부족합니다. 인출이 이루어지지 못했습니다.")
        elif money_out <=0:
            print("출금액을 정확히 입력하세요")
        else:
            total = total - money_out
            print(str(money_out)+"원이 인출되었습니다.")
    elif select == 3:
        print(name + "님의 현재 잔액은 "+str(total)+"원입니다.")
    elif select == 4:
        print("이용해 주셔서 감사합니다.")
        break
    else:
        print("1~4 중에서 입력해주세요")
