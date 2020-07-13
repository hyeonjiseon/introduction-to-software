#학생의 점수를 입력 받고 텍스트 파일로 저장 후,
#저장된 텍스트 파일을 읽어서 성적의 평균과 최고점 출력
#파일을 저장하고 불러올 때 확장자(.txt) 붙이기
#line: 텍스트 파일에 포함된 각 문장을 읽어 리스트로 저장하는 변수
#scoreRead.append(int(line)): line을 int형으로 바꾸어 리스트로 저장
#len(line): 글자 길이 측정. 이걸로 사용자가 숫자를 입력했는지, 엔터만 눌렀는지 확인
#line = f.readline() 이건 문자로 보고 라인 별로 읽은 것이기 때문에
#mymemo.append(line)으로 그대로 가면 sum(mymemo)/len(mymemo)를 숫자로 계산X
#따라서 mymemo.append(int(line))로 바꿔줘야 함

name = input("파일명을 입력하세요:")

def write_file():
    f=open(name, 'w')
    for item in mymemo:
        msg = item + '\n'
        f.write(msg)
    f.close()

mymemo = []
while True:
    print("점수를 입력해 주세요. 끝내시려면 엔터키 두 번 눌러주세요.")
    item = input()
    if len(item) == 0:
        break
    mymemo.append(item)

write_file()
print(name,"저장 완료")
