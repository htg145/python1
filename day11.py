# todo list
# 기능
# 할 일 추가 c
# 할 일 조회 r
# 할 일 완료 u
# 할 일 삭제 d
import json


# 기능
# 메뉴 - 메뉴 선택 - 해당 함수
# 할일 데이터 ---> json
# open()
def save_todo(todo_list):
    with open("todo.json", "w", encoding="utf-8") as file:
        json.dump(todo_list, file, indent=4, ensure_ascii=False)
    print("저장 되었 습니다.")

def add():
    todo_list = []
    while True:
        todo_name = input("할 일(그만 할려면 종료) : ")
        todo_complete = False
        if todo_name == "종료":
            save_todo(todo_list)
            # 저장
            break
    todo_list.append(
        {
            "todo_name": todo_name,
            "todo_complete":todo_complete
        }
    )

def check():
    with open("todo.json", "r", encoding="utf-8") as file:
        todo_list = list(json.load(file))

    for i in range(0, len(todo_list)):
        print(f"{i + 1}. 할 일 : {todo_list[i]["todo_name"]}")
        print(f"완료 상태 : {"완료" if todo_list[i]["todo_complete"] else "미완료"}")
        return todo_list

def update():
    todo_list = check()
    while True:
        choice_todo = int(input("몇 번째 Todo?"))
        todo = todo_list[int(choice_todo - 1)]

        todo["todo_name"] = input("할 일 수정 : ")
        choice_complete = input("할 일 완료(y/n) : ")
        if choice_complete == "y":
            todo["todo_complete"] = True
        elif choice_complete == "n":
            todo["todo_complete"] = False
        continue_choice = input("또 수정 하시 겠습 니까?(y/n)")
        if continue_choice == "y":
            todo["todo_complete"] = True
        elif choice_complete == "n":
            save_todo()

def delete():
    todo_list = check()
    if len(todo_list) == 0:
        print("삭제 할게 없음")
    else:
        choice_todo = int(input("몇 번째 할 일을 삭제 할까?"))
        del todo_list[choice_todo - 1]

        save_todo(todo_list)

while True: # 계속 반복
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
