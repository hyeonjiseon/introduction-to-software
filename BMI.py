#체질량지수 계산 프로그램
print("키와 몸무게를 입력하면 체질량지수를 계산합니다.")
height = float(input("키(cm) :"))
weight = float(input("몸무게(kg) :"))
BMI = weight / (height/100 * height/100)

print("* 체질량지수 : %4.1f " % BMI)

#4는 정수 범위 자리수인데 부족하면 앞에 0으로 채워지지만 굳이 나타나진 않고
#1은 소수점 아래 자리수이고 넘으면 반올림

if BMI < 18.5:
    print("* 저체중")
elif BMI < 23:
    print("* 정상")
elif BMI < 25:
    print("* 과체중")
elif BMI < 30:
    print("* 비만")
else:
    print("* 고도비만")
