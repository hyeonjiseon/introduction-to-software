
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
