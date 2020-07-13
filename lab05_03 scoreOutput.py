#mymemo=[]
kscore=[]
escore=[]

callname=input("불러올 파일 이름을 입력하세요:")
print('='*38)

f=open(callname)
while True:
    line = f.readline()
    if len(line) == 0:
        break
    
    line = line.strip().split(' ')
    #mymemo.append(line)
    #[['90', '85'], ['80', '90'], ['75', '66'], ['40', '30'], ['99', '100']]

    kscore.append(int(line[0])) #[90, 80, 75, 40, 99]
    escore.append(int(line[1])) #[85, 90, 66, 30, 100]

    #다른 방법
    #line = line.strip() #문자열의 맨 앞과 맨 뒤에 있는 whitespace(' ', \t, \n) 제거
    #mymemo.append(line) #['90 85', '80 90', '75 66', '40 30', '99 100']
    #temp = line.split(' ')
    #kscore.append(int(temp[0]))
    #escore.append(int(temp[1]))    

f.close()

kav = sum(kscore)/len(kscore)
eav = sum(escore)/len(escore)
tav = (kav+eav)/2

print("국어 평균: %.2f" % kav)
print("영어 평균: %.2f" % eav)
print("총 평균: %.2f" % tav)
    
