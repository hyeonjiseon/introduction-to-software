#할인 가격 계산 함수를 활용하는 프로그램

rate = 20

#할인율을 전역 변수로 사용한 할인 가격 계산 함수
def salePrice(price):
    #global rate
    #이걸 안 해 주면 값을 지정해 주기 전에 읽으려 해서X
    #rate = rate + 10
    #함수 내에서 전역 변수 값을 수정하려면 전역 변수를 먼저 global 선언
    result = price * (1 - rate/100)
    return result

original = int(input("가격을 입력하세요:"))
print("원래 가격:", original)
print(rate, "%할인 가격:", salePrice(original))
rate = 30
print(rate, "% 할인 가격", salePrice(original))
