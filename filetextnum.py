#파일 내의 단어 출력 횟수 계산 함수

def word_count(filename):
    f = open(filename)
    counts = {}
    for line in f:
        list = line.split() #파일의 각 줄을 단어들의 리스트로 분리
        for word in list: #리스트 내의 각 단어에 대해서 
            if word in counts: #해당 단어가 사전 counts에 이미 있으면
                counts[word] += 1 #횟수를 하나 증가
            else:
                counts[word] = 1 #처음 나타났으므로 횟수 1
                #이후 바깥 for문으로 다른 line에서 같은 단어 나오면 횟수 올라감
    return counts

reply = 'y'
while reply == 'y':
    filename = input("검색할 파일 이름을 입력하세요: ")
    wc = word_count(filename)

    for word in sorted(wc):
        print(word, wc[word])

    reply = input("계속하시겠습니까(y/n)")
