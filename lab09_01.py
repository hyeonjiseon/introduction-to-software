#Book class와 Book class를 상속하는 textbook class

#book class
# 1)속성(저자, 제목, 가격, 페이지 수)
# 2)메소드(속성들을 초기화, 정보 출력, 객체 삭제)
# 3)book class가 몇 개 생성됐는 지 세는 counter 변수 넣기(private로)
#   -초기화 메소드에서 counter 1증가, 소멸자 메소드에서 counter 1 감소
# 4)counter의 값을 불러오는 메소드 만들기

#textbook class
# 1)속성(교과목 명, 전공, 연도, 학기)
# 2)메소드(속성들을 초기화, 정보 출력, 교과목명 변경, 연도 변경, 학기 변경)
# 3)book class에 존재하는 책의 정보 출력하는 메소드 재정의

#1. book 4개, textbook 4개 생성한 뒤 출력 메소드 이용하여 출력
#2. 총 몇 개의 클래스 만들어졌는 지 출력
#3. 3번째 book "나미야 잡화점의 기적" 삭제
#4. 1번째 textbook "python 프로그래밍의 이해"의 과목명 "소프트웨어의 이해"로 수정
#5. 2번째 textbook "데이터베이스프로그래밍"의 연도 2017로 수정
#6. 3번째 textbook "Data Science for Business"의 학기 1로 수정
#7. 4번재 textbook "유닉스 리눅스 사용해서 프로그래밍까지" 삭제
#8. 수정된 책들과 총 개수 출력

class book():
    
    __counter = 0 #private 변수
    
    def __init__(self, auth, title, price, page):
        self.auth = auth
        self.title = title
        self.price = price
        self.page = page
        book.__counter += 1
        
    def printbk(self):
        print('''저자 : %s\n제목 : %s\n가격 : %d원\n페이지 수 : %d쪽\n''' %(self.auth, self.title, self.price, self.page))

    def __del__(self):
        book.__counter -= 1

    def accountinstances():
        return book.__counter


class textbook(book):

    def __init__(self, auth, title, price, page, subj, major, year, sem):
        self.subj = subj
        self.major = major
        self.year = year
        self.sem = sem
        book.__init__(self, auth, title, price, page)

    def printtb(self):
        print("저자 : %s\n제목 : %s\n가격 : %d원\n페이지 수 : %d쪽\n교과목명 : %s\n전공 : %s\n연도 : %d\n학기 : %d학기\n"
              %(self.auth, self.title, self.price, self.page, self.subj, self.major, self.year, self.sem))

#book 4개 생성
b1 = book('이기주', '언어의 온도', 13800, 308)
b2 = book('조남주', '82년생 김지영', 13000, 192)
b3 = book('히가시노 게이고', '나미야 잡화점의 기적', 14800, 456)
b4 = book('공지영', '할머니는 죽지 않았다', 12000, 272)

print("="*40)

#book 4개 출력
b1.printbk()
b2.printbk()
b3.printbk()
b4.printbk()


#textbook 4개 생성
t1 = textbook('유석종, 이상규, 창명모', 'Python 프로그래밍의 이해', 18000, 320, '프로그래밍의이해', '소프트웨어학부', 2017, 1)
t2 = textbook('심준호', '데이터베이스프로그래밍', 13000, 258, '데이터베이스프로그래밍', '컴퓨터과학전공', 2016, 1)
t3 = textbook('Roster Provost and Tom Fawcett', 'Data Science for Business', 37400, 414, '데이터사이언스개론', '소프트웨어융합전공', 2018, 2)
t4 = textbook('창병모', '유닉스 리눅스 사용해서 프로그래밍까지', 24000, 456, '리눅스시스템', '소프트웨어학부', 2014, 2)

#textbook 4개 출력
t1.printtb()
t2.printtb()
t3.printtb()
t4.printtb()

print("-"*40)
print("총 "+str(book.accountinstances())+"권\n")

print("="*13, "수정된 목록", "="*14)

#나미야 잡화점 삭제
del(b3)

#textbook 수정
t1 = textbook('유석종, 이상규, 창명모', 'Python 프로그래밍의 이해', 18000, 320, '소프트웨어의 이해', '소프트웨어학부', 2017, 1)
t2 = textbook('심준호', '데이터베이스프로그래밍', 13000, 258, '데이터베이스프로그래밍', '컴퓨터과학전공', 2017, 1)
t3 = textbook('Roster Provost and Tom Fawcett', 'Data Science for Business', 37400, 414, '데이터사이언스개론', '소프트웨어융합전공', 2018, 1)

t1.printtb()
t2.printtb()
t3.printtb()

#유닉스 삭제
del(t4)

print("-"*40)
print("총 "+str(book.accountinstances())+"권")
