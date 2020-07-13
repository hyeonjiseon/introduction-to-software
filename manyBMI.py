#여러 사람의 체질량지수를 계산하는 프로그램

height_weight_list = [('가연', 160, 52), ('나리', 162, 65), ('다슬', 170, 60),
                      ('미라', 157, 50), ('가을', 165, 48)]

bmi_list=[]
for(name, h, w) in height_weight_list:
    bmi = w/(h/100*h/100)
    bmi_list.append((name, bmi))
for(name, bmi) in bmi_list:
    print(name, " 체질량지수: %4.1f " %bmi, end=" ")
    if bmi < 18.5:
        print("저체중")
    elif bmi < 23:
        print("정상")
    elif bmi < 25:
        print("과제중")
    elif bmi < 30:
        print("비만")
    else:
        print("고도비만")
