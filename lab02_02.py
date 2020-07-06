name = input("이름을 입력하세요:")
time = int(input("음성 통화 시간(초)을 입력하세요:"))
data = int(input("데이터 사용량(MB)을 입력하세요:"))

base = 12100
timecash = time*1.98
datacash = data*55
total = base+timecash+datacash

print(name, "님의 3월 이용 금액은", total, "원 입니다.")

#다른 방법
total = 12100 + 1.98*time + 55*data

#또 다른 방법
voiceFee = 1.98
dataFee = 55
total = base + (voiceFee*time) + (dataFee*data)
