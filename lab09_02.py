#책을 추가, 삭제, 조회하는 프로그램
#책들을 관리하는 리스트 생성
#book class: 실습문제 2번에서 작성한 book class 사용
#책 추가: 작가, 제목, 가격, 페이지수 입력하여 book 생성,
#         생성된 book 클래스를 리스트에 집어 넣기(append 사용)
#책 삭제: 리스트 인덱스 번호를 입력 받음,
#         리스트에서 입력 받은 번호의 자리에 있는 책 삭제
#전체 책 출력: 리스트에 들어 있는 모든 책의 정보 출력
#              각각의 책 정보는 book 클래스 안에 있는 출력 메소드 사용
#              전체 책 개수 출력(book 클래스의 counter값 출력하는 메소드 사용)

b = []

class book():
    __counter = 0

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
                                                                

def addBook():
    print()
    author = input("저자 : ")
    title = input("제목 : ")
    price = int(input("가격 : "))
    page = int(input("페이지 수 : "))

    b.append(book(author, title, price, page))

def delBook():
    print()
    index = int(input("삭제할 책의 인덱스를 입력하세요: "))

    del(b[index])

def printBook():
    print()
    for i in range(book.accountinstances()):
        b[i].printbk()
    print("전체 책의 개수는 "+str(book.accountinstances())+"개 입니다.")

while True:
    print("="*40)
    print("1. 책 추가\n2. 책 삭제\n3. 전체 책 출력\n4. 종료")
    print("-"*40)
    select = int(input("선택 : "))
    
    if select == 1:
        addBook()
    elif select == 2:
        delBook()
    elif select == 3:
        printBook()
    elif select == 4:
        print("\n이용해주셔서 감사합니다.")
        break
    else:
        print("\n잘못 입력했습니다.")
        continue
