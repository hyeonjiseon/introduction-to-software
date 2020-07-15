#커피샵의 고객 마족도 점 수를 관리하는 프로그램을 사전 리스트를 사용하여 만든다.
#커피샵의 평점을 입력받아 사전에 저장하고 탐색, 삭제하는 프로그램

def print_menu():
    print('1. Show all coffeeshop review')
    print('2. Add coffee shop review')
    print('3. Delete coffeeshop review')
    print('4. Search coffeeshop')
    print('5. Exit')

def show_review(reviews):
    print()
    print('Coffee Shop Review')
    print()
    print('Store \t\t Grade ')
    print('='*30)
    for store in reviews:
        print(store, ' \t ', reviews[store])
    print('='*30)
    print()

def add_review(reviews):
    print("Add new review")
    store = input("Store:")
    grade = float(input("Grade [1...5] :"))
    while (grade < 1 or grade > 5):
        print("enter your grade between 1..5")
        grade = float(input("Grade [1...5] :"))
    reviews[store] = grade
    show_review(reviews)

def delete_review(reviews):
    print("Delete Store data ")
    store = input("Store:")
    if store in reviews:
        del reviews[store]
    show_review(reviews)

def search_store(reviews):
    print("Search store review")
    store = input("Store:")
    if store in reviews:
        print(store, " : ", reviews[store])
    else:
        print(store, " is not found")

    
reviews = {}
choice = 0
print_menu()

while True:
    menu = int(input())
    if menu == 1:
        show_review(reviews)
    elif menu == 2:
        add_review(reviews)
    elif menu == 3:
        delete_review(reviews)
    elif menu == 4:
        search_store(reviews)
    if menu == 5:
        break
    print_menu()
