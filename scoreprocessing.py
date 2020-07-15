#성적을 입력받고 정렬하여 출력하는 프로그램

#메뉴 출력
def print_menu():
    print()
    print("1. Show ranking & mean of scores")
    print("2. Add scores")
    print("3. Delete a score")
    print("4. Exit")
    print()
    print("choice : ", end = ' ')

#점수와 순위를 출력
def show_ranking():
    print()
    print("Score board")
    print()
    print("="*30)
    if len(scores) == 0:
        print("empty list")
        return

    rank = 1
    total = 0
    scores.sort(reverse = True)
    for score in scores:
        print(rank, " \t ", score)
        rank += 1
        total += score
    print("="*30)
    mean = total/len(scores)
    print("Score mean : %.2f" % mean)

#점수 입력 받기
def add_score():
    global scores
    while True:
        print("enter a score between 0..100 (otherwise exit)")
        score = int(input("score: "))
        if score < 0 or score > 100:
            break
        scores.append(score)
        print(scores)

#입력 점수 삭제
def delete_score():
    global scores
    print(scores)
    score = int(input("Enter a score to delete : "))
    if score in scores:
        scores.remove(score)
        print(scores)
    else:
        print("no such score")

scores = []
choice = 0
print_menu()

while (choice != 4):
    choice = int(input())
    if choice == 1:
        show_ranking()
    elif choice == 2:
        add_score()
    elif choice == 3:
        delete_score()
    elif choice == 4:
        break
    print_menu()
