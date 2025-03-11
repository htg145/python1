import json
import random

def study(level):
    review_list = []

    with open("words.json", "r", encoding="utf-8") as file:
        word_list = json.load(file)  # 수정: json.load() 결과를 list()로 변환할 필요 없음
        filtered_word_list = [word for word in word_list if word["level"] == level]  # 수정: list comprehension 사용

        if not filtered_word_list:  # 추가: 해당 난이도 단어 없는 경우 처리
            print(f"'{level}' 난이도의 단어가 없습니다.")
            return

        count = 0
        while count < 10:
            select_index = random.randint(0, len(filtered_word_list) - 1)  # 수정: 범위 오류 수정
            print("=============================")
            print(f"{filtered_word_list[select_index]['meaning']}")

            input_eng = input("단어 : ")
            if input_eng == filtered_word_list[select_index]["word"]:
                print("정답 입니다 !!!")
            else:
                print("오답 입니다.")
                print(f"정답 : {filtered_word_list[select_index]['word']}")
                review_list.append(filtered_word_list[select_index])

            count += 1

        with open("review_note.json", "w", encoding="utf-8") as review_file:
            json.dump(review_list, review_file, ensure_ascii=False, indent=4)

def review():
    try:
        with open("review_note.json", "r", encoding="utf-8") as review_file:
            word_list = json.load(review_file)
            incorrect_count = 0
            for word in word_list:
                print("=============================")
                print(f"뜻: {word['meaning']}")  # 수정: 뜻을 먼저 보여주도록 변경
                input_eng = input("단어: ")
                if input_eng == word["word"]:
                    print("정답 입니다.")
                else:
                    print("오답입니다.")
                    print(f"정답: {word['word']}")
                    incorrect_count += 1

            if incorrect_count == 0:
                print("오답이 없습니다. 모두 맞추셨습니다!")
            else:
                print(f"총 {len(word_list)}문제 중 {incorrect_count}문제를 틀렸습니다.")

    except FileNotFoundError:
        print("오답 노트 파일이 없습니다.")
    except json.JSONDecodeError:
        print("오답 노트 파일 형식이 올바르지 않습니다.")

while True:
    print("=======메뉴========")
    print("""
        1. 초등
        2. 중급
        3. 전문
        4. 오답 노트 복습
        5. 종료
    """)

    choice = input("메뉴를 선택 하세요. : ")
    if choice == "1":
        study("초등")
    elif choice == "2":
        study("중급")
    elif choice == "3":
        study("전문")
    elif choice == "4":
        review()
    elif choice == "5":
        break
    else:
        print("다시 선택해 주세요.")
        continue