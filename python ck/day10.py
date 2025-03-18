# 영어 단어장 만들기
# 기능 : 난이도 선택, 랜덤 으로 단어뜻 출력
# 해당 영어 단어를 입력 => 정답: 다음 으로
# 틀리면 오답 노트 리스트 만들 어서 데이터 셋
# 메뉴 에서 복습 하기 => 오답 노트에 있는 거 가져 온다
# 흐름
# 메뉴 선택 - 공부 하기 - 난이도 선택
# 정답 맞추기 - 틀리면 오답 리스트
# 메뉴 선택 - 복습 하기 - 틀렷던 오답 리스트 불러 오기 - 공부 하기
# import json
# import random
#
# def study(level):
#     review_list = []
#
#     with open("words.json", "r", encoding="utf-8") as file:
#         word_list = list(json.load(file))
#         filtered_word_list = list(filter(lambda x: x["level"] == level, word_list))
#
#
#
#         count = 0
#         while count < 10:
#             select_index = random.randint(0, len(filtered_word_list))
#             print("=============================")
#             print(f"{filtered_word_list[select_index]["meaning"]}")
#
#             input_eng = input("단어 :")
#             if input_eng == filtered_word_list[select_index]["word"]:
#                 print("정답 입니다 !!!")
#             elif input_eng != filtered_word_list[select_index]["word"]:
#                 print("오답 입니다.")
#                 print(f"정답 : {filtered_word_list[select_index]["word"]}")
#                 review_list.append(filtered_word_list[select_index])
#
#             count += 1
#
#         with open("review_note.json", "w", encoding="utf-8") as review_file:
#             json.dump(review_list, review_file, ensure_ascii=False, indent=4 )
#
# def review():
#     with open("review_note.json", "r", encoding="utf-8") as review_file:
#         word_list = list(json.load(review_file))
#         incorrect_cound = 0
#         for word_index in range(0, len(word_list)):
#             print("=============================")
#             input_eng = ("단어 :")
#             if input_eng == word_list[word_index]["word"]:
#                 print("정답 입니다.")
#             elif input_eng != word_list[word_index]["word"]:
#                 print("오답입니다.")
#                 print(f"정답 : {word_list[word_index]}")
#
#
#
#
# while True:
#     print("=======메뉴========")
#     print("""
#         1. 초등
#         2. 중고
#         3. 전문
#         4. 오답 노트
#         5. 종료
#     """)
#
#     choice = input("메뉴를 선택 하세요. : ")
#     if choice == "1":
#         study("초등")
#     elif choice == "2":
#         study("중고")
#     elif choice == "3":
#         study("전문")
#     elif choice == "4":
#         review()
#     elif choice == "5":
#         break
#     else:
#         print("다시 선택해 주세요.")
#         continue