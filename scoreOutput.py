callname = input("불러올 파일 이름을 입력하세요: ")
mymemo=[]
f = open(callname)
while True:
    line = f.readline()
    if len(line) == 0:
        break
    line = line.strip()
    mymemo.append(int(line))

f.close()

for item in mymemo:
    msg = item
    print(msg)
print('-'*30)
print("평균:", sum(mymemo)/len(mymemo))
print("최고점:", max(mymemo))

