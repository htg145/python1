import json

todo_list = []  # 전역 변수로 todo_list를 선언 및 초기화

def load_todo_list():
    """JSON 파일에서 할 일 목록을 불러오는 함수"""
    global todo_list  # 전역 변수 todo_list를 사용한다고 선언
    try:
        with open("todo.json", "r", encoding="utf-8") as file:
            todo_list = json.load(file)
    except FileNotFoundError:
        todo_list = []  # 파일이 없을 경우 빈 리스트로 초기화

def save_todo():
    """할 일 목록을 JSON 파일에 저장하는 함수"""
    global todo_list  # 전역 변수 todo_list를 사용한다고 선언
    with open("todo.json", "w", encoding="utf-8") as file:
        json.dump(todo_list, file, indent=4, ensure_ascii=False)
    print("저장되었습니다.")

def add():
    """할 일을 추가하는 함수"""
    global todo_list  # 전역 변수 todo_list를 사용한다고 선언
    while True:
        todo_name = input("할 일(그만 할려면 종료) : ")
        if todo_name == "종료":
            save_todo()
            break
        todo_list.append({"todo_name": todo_name, "todo_complete": False})

def check():
    """할 일 목록을 조회하는 함수"""
    global todo_list  # 전역 변수 todo_list를 사용한다고 선언
    if not todo_list:
        print("할 일 목록이 비어 있습니다.")
        return
    for i in range(len(todo_list)):
        todo = todo_list[i]
        status = "[완료]" if todo["todo_complete"] else "[미완료]"
        print(f"{i + 1}. 할 일 : {todo['todo_name']} {status}")

def update():
    """할 일을 수정하는 함수"""
    global todo_list  # 전역 변수 todo_list를 사용한다고 선언
    if not todo_list:
        print("수정할 할 일이 없습니다.")
        return
    check()
    while True:
        try:
            choice_todo = int(input("몇 번째 Todo를 수정하시겠습니까? (종료: 0): "))
            if choice_todo == 0:
                break
            todo = todo_list[choice_todo - 1]
            todo["todo_name"] = input("할 일 수정: ")
            choice_complete = input("할 일 완료(y/n): ")
            if choice_complete == "y":
                todo["todo_complete"] = True
            elif choice_complete == "n":
                todo["todo_complete"] = False
            else:
                print("잘못된 입력입니다.")
            continue_choice = input("또 수정하시겠습니까?(y/n): ")
            if continue_choice != "y":
                break
        except (ValueError, IndexError):
            print("잘못된 입력입니다.")
    save_todo()

def delete():
    """할 일을 삭제하는 함수"""
    global todo_list  # 전역 변수 todo_list를 사용한다고 선언
    if not todo_list:
        print("삭제할 할 일이 없습니다.")
        return
    check()
    try:
        choice_todo = int(input("몇 번째 할 일을 삭제할까요? (종료: 0): "))
        if choice_todo == 0:
            return
        del todo_list[choice_todo - 1]
        save_todo()
        print("삭제되었습니다.")
    except (ValueError, IndexError):
        print("잘못된 입력입니다.")

load_todo_list()  # 프로그램 시작 시 할 일 목록 불러오기

while True:  # 계속 반복
    print("==========메뉴=========")
    print("""
    1. 할 일 추가
    2. 할 일 조회
    3. 할 일 수정
    4. 할 일 삭제
    """)

    choice = input("메뉴를 선택해 주세요. :")
    if choice == "1":
        add()
    elif choice == "2":
        check()
    elif choice == "3":
        update()
    elif choice == "4":
        delete()
    else:
        print("할 메뉴를 선택해 주세요.")
        break