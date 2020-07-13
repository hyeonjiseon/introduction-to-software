#학생별 국영수 점수 합을 계산하는 프로그램

scores = [[89,89,85], [70,80,80], [90,90,95], [60,70,65], [90,80,75]]
stud = []
for lst in scores:
    sum = 0
    for score in lst:
        sum += score
    stud.append(sum)
print(stud)

#scores = list of lists
#lst = list of integers
#score = integer
