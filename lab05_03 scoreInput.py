#국어와 영어 점수를 입력 받아 텍스트 파일로 저장한 후,
#텍스트 파일을 불러와 각 평균과 총 평균을 계산하여 출력하는 프로그램
#파일 쓰기 1) 확장자(.txt)까지 입력 받기
#          2) 점수를 입력 받아 리스트에 저장(int로 변환 안 해도 됨)
#          3) len(score) == 0일 때 파일 저장
#파일 읽고 평균 계산 1) 국어와 영어 점수를 각각 담을 리스트 변수 선언
#                    2) strip: '\n'을 제거한 후 반환
#                    3) split(''): 띄어쓰기 기준으로 분할
#                     예) sentence = "this is a plain sentence."
#                         sentence.split('')
#                         ['this', 'is', 'a', 'plain', 'sentence.']
#                    4) append하면서 int로 형 변환
#                    5) 평균은 소수점 둘째 자리까지

name = input("저장할 파일 이름을 입력해 주세요: ")

def write_file():
    f=open(name, 'w')
    for item in mymemo:
        msg = item + '\n'
        f.write(msg)
    f.close()

mymemo = []

while True:
    score = input("국어와 영어 점수를 입력해주세요\n예)90 85\n")
    if len(score) == 0:
        break
    mymemo.append(score)

write_file()
print(name, "저장 완료")
