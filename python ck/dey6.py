# 제어문
"""
조건문
반복문 (for, while)
"""


# 조건문 : 어떤 조건에 따라 실행이 분기 되도록 하는 기준이 되는 식
# num = int(input("숫자를 입력해 주세요."))
# if num > 0:
#     print("양수 입니다.")
# else:
#     print("음수 입니다.")

# score = int(input("점수를 입력해 주세요:"))
#
# if score >= 90:
#     print("A 입니다.")
# elif score >= 80:
#     print("B 입니다.")
# elif score >= 70:
#     print("C 입니다.")
# else:
#     print("D 입니다.")

# 숫자를 입력 받고 짝수 인지 홀수 인지
# num = int(input("숫자를 입력 하시오:"))
#
# if num %2 == 0:
#     print("짝수")
# elif num :
#     print("홀수")

# 나이랑 학생 인지 아닌지 두가지 질문
# 성인 이면서 학생 이면 성인 학생 입니다.
# 성인 학생이 아닙 니다.
# elif 중간 에 else 마지막 에
# age = int (input("나이를 입력 하시오."))
# student = input("학생 입니까? (y/n)")
#
# if age >= 18 and student == "y":
#     print("성인 학생 입니다.")
# else:
#     print("성인 학생이 아닙 니다")


# 반복문 (While) 정해져 있지 않다
# 조건이 참(True)인 동안 계속 반복
# 특정 조건을 만족할 때까지 계속 실행 해야 하는 경우
# num = 0
# while num < 10:
#     num += 1
#     if num % 3 == 0:
#         continue
#
#     print(num)

# 구구단
# dan = 1
# while dan <= 9:
#     n = 1
#     while n <= 9:
#         print(f"{dan}x{n}={dan*n}")
#         n += 1
#     dan += 1

# 5부터 5의 배수를 50 이하 까지 조건
# 근대 30일때 멈출 게요

# num = 5
# while num <= 50:
#     print(num)
#     if num == 30:
#         break
#     num += 5

# 반복문 (for) 정해져 있다

# 특정 조건을 만족할 때까디 계속 실행 하는 경우
# 반복 해야 할 횟수가 정해져 있거나, 반복 해야 할 대상이 명확 하게 정의 되어 있는 겨우

# for 문
# fruits = ["사과", "바나나", "체리", "딸기"]
# for fruit in fruits:
#     print(fruit)
# 전역 변수, 지역 변수

# score = {
#     "동윤": 80,
#     "종원": 70,
#     "지니": 100
# }
# for key in score:
#     print(f"{key}의 점수는{score[key]}")

# a_tuple = ("안녕", "하세요", "반갑습니다")
# for a in a_tuple:
#     print(a)
#
# a_set ={3, 1, 1, 2, 4, 6, 2}
# print( sorted(a_set))
# for a in a_set:
#     print(a)

# word = "python"
# for i in word:
#     print(i)
# for i in range(1, 10, ):
#     print("1...",i)
#     if  i == 5:
#         continue
#     print("2...",i)
#
# for i in range(2, 101, 2): # 짝수가 100까지 나온다
#     print(i)

# 리스트 합 구하기
# 전역 함수 지역 안에 쓸수 있다

# total = 0
# num_list = [10, 20, 40, 60, 80]
#
# 내가 한거
# for a in num_list:
#     total += a
#     print(total)

# 답
# for num in num_list:
#     total += num
# print(total)

# for num in num_list:
#     print("num", num)
#     total += num
#     print("total",total)

# 구구단
for dan in range(1, 10):
    for n in range(1, 10):
        print(f"{dan}x{n}={dan*n}")























