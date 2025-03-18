# 사용자 정의 함수
# 사용자 가 직접 만들어 사용 하는 함수
# def 함수 이름():
    # 수행할 코드
# 기본 적인 사용자 정의 함수
# def func1():
#     print("Hello World")
#
# func1()
# func1()
# func1()

# def plus():
#     a = 2  # 지역 변수
#     b = 3
#     print(a + b)
#
# plus()

# 매개 변수가 있는 사용자 정의 함수

# 매개 변수
# 함수를 호출 할때 전달 되는 값을 저장 하는 변수
# 함수 내에서 계산한 결과를 함수 외부로 반환
# def 함수 이름(매개 변수1, 매개 변수2):
    # 수행할 코드

# def hello(name): # name 매개 변수
#     print(f"안녕 하세요 저는 {name} 입니다.")
#
# hello("123")

# def plus(x, y):
#    print( x + y )

# plus(5, 6)

# def hello(name="홍길동"):
#     print(f"안녕 하세요 {name}입니다.")

# hello()
# hello("찬호")


# def introduce(name, age):
#     print(f"제 이름은 {name}이고 나이는 {age}입니다.")
#
# introduce(26, "찬호")
# introduce(age=26, name= "찬호") # 직접 지정 가능

# 리턴 값이 있는 사용자 정의 함수

# def plus(x, y):
#     return  x + y
#
# result = plus(1, 2) # 방법 1
# print(result)
#
# print(plus(1, 2)) # 방법 2

# def multiple_seven(num):
#     return  num * 7
# print(multiple_seven(3))

# def check_divide_seven(num):
#     if num % 7 == 0:
#         return True
#     else:
#         return False
#
# print(check_divide_seven(7))

# def factorial(num):
#     sum = 1
#     print(list(range(num))) # 확인용
#     for n in range(num):
#         print(f"n = {n}") # 확인용
#         sum = sum * (n + 1)
#         print(f"sum = {sum}") # 확인용

#     return  sum

# print(factorial(7))
# 7! = 7 × 6 × 5 × 4 × 3 × 2 × 1 = 5040 # !가 factorial 팩토 리얼
# factorial 7까지 쭉 곱 하는거

# def cal_average(scores):
#     sum = 0
#
#     for score in scores:
#         sum += score
#
#     return sum / len(scores)
#
# scores_list1 = [55, 70, 100]
# scores_list2 = [100, 99, 88]
# scores_list3 = [80, 70, 60]
#
# print(cal_average(scores_list1))
# print(cal_average(scores_list2))
# print(cal_average(scores_list3))

# 콜백 함수
# 함수를 매개 변수 로 전달 하여 필요 할때 호출 하도록 하는 개념
# 어떤 함수가 실행 되는 동안 미리 정의된 다른 함수를 호출 하여 실행 하는 역할

# def calculator(x, y, operation):
#     return operation(x, y)
#
# def plus(x, y):
#     return x + y
#
# def minus(x, y):
#     return x - y
#
# def multiple(x, y):
#     return x * y
#
# def divide(x, y):
#     return x / y
#
# print(calculator(4, 8, plus))
# print(calculator(8, 4, minus))
# print(calculator(4, 8, multiple))
# print(calculator(4, 8, divide))
# import time
#
# def timer(pause_second, callback):
#     print(f"{pause_second}초 타이머 가 시작 되었 습니다.")
#     print(f"{pause_second}초 뒤에 함수가 시작 됩니다.")
#
#     time.sleep(pause_second)  # time.sleep() 함수를 먼저 호출
#
#     callback()
#     print("타이머 가 종료 됩니다.")
#
# def hello():
#     print("안녕")
#
# timer(3, hello) #예시

# lambde 함수 (익명 함수, 미시 함수)
# 특정 범위 내에 서만 사용 되거나 호출 되는 횟수가 한번인 경우에 유용 하다
# lambda 매개 변수1, 매개 변수 2 ... : 함수 내부 코드

# def plus(x, y):
#     return x + y
# print(plus(4, 5))
#
# add_lambda = lambda x, y: x + y # 꼬리 + 털 = 고양이
# print(add_lambda(4, 5))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# double =list(map(lambda x: x * 2, numbers ))
# print(double)

# parity = lambda a: "짝수" if a % 2 == 0 else "홀수" # 삼항 연산자 참이면 앞 거짓 이면 뒤
#
# print(parity(2))

#1. 두 수를 입력 받고 두수의 합을 출력 하는 함수

# 내가 한거

# num1 = int(input("숫자를 입력해 주세요."))
# num2 = int(input("숫자를 입력해 주세요."))
#
# def plus (x ,y):
#     print(x + y)
# plus(num1, num2)

# 답
# a = int(input("첫번째 숫자 : "))
# b = int(input("두번째 숫자 : "))
#
# def add_func(x, y):
#     print(x + y)
# add_func(a, b)

# 숫자 하나를 입력 받고 해당 숫자가 짝수 이면 짝수를 출력 하고
# 홀수 이면 홀수를 출력 하는 함수

# 답
# a = int(input("숫자 : "))
# def 홀짝(v):
#     if v % 2 == 0 :
#         print("짝수")
#     else:
#         print("홀수")
#
# 홀짝(a)










