# 에러와 예외
# 예외 처리
# try-except
# 에러 : 프로 그램 오류 또는 시스템 문제로 발생 하는 예외
# 예외 : 사용자 의 입력 오류에 따라 발생 하는 예외, 예상치 못한 상황
# 예외 처리 : 프로 그램이 실행 될때 발생될 에러를 미리 예측 하고 처리 해주는 것
# try-except
# try:
#      에러가 발생할 수 있는 코드 블록
# except 예외 유형:
#      예외가 발생할 수 있는 코드 블록


# try-except[발생 예외]
# try:
#      에러가 발생할 수 있는 코드 블록
# except [발생 예외]:
#      발생 예외1에 해당 하면 수행 되는 코드 블록

# c[발생 예외] as 예외 메시지 변수
# try:
#      에러가 발생할 수 있는 코드 블록
# except [발생 예외1] as 변수1:
#      발생 예외1에 해당 하면 수행 되는 코드 블록
# except [발생 예외2] as 변수2:
#      발생 예외2에 해당 하면 수행 되는 코드 블록

# try-finally, else
# try:
#      에러가 발생할 수 있는 코드 블록
# except [발생 예외]:
#      발생 예외1에 해당 하면 수행 되는 코드 블록
# finally:
#      예외 발생과 상관 없이 항상 실행 되는 블록
# else:
#         에러가 없을때 정상적 일때 실행됨

# 커스텀 예외 클래스
# try:
#      에러가 발생할 수 있는 코드 블록
# if 에러가 발생할 조건:
#     raise Exception("에러 메시지") # raise 해당 조건이 되면 에러를 띄울수 있다. 메시지 가 뜬다

# 커스텀 예외 클래스
# class 예외 클래스명(Exception): Exception 부모 클래스, 클래스명 자식 클래스
# super().__init__("에러 메시지")
# 에러 메시지 띄운다

# print(10/0)
# num = int(input("숫자를 입력해 주세요."))
# print(10/num)

# try-except
# try:
#     num = int(input("숫자를 입력해 주세요."))
#     print(10/num)
# except:
#     print("예외 발생")

# try-except[발생 예외]
# try:
#     num = int(input("숫자를 입력해 주세요."))
#     print(10/num)
# except ValueError:
#     print("문자 말고 숫자 넣어라")
# except ZeroDivisionError:
#     print("0 말고 다른거 넣어라")

# try:
#     my_list = [1, 2, 3]
#     index = int(input("리스트 에서 가져올 인덱스 : "))
#     print(my_list[index])
# except IndexError:
#     print("인덱스 범위가 아닙 니다.")
# except ValueError:
#     print("숫자만 입력 하시오")

# try:
#     with open("hi.txt", "r") as file:
#         content = file.read()
# except FileNotFoundError:
#     print("파일 없음")

# try-finally # 오류 발생
# try:
#     file = open("hi.txt", "r")
#     content = file.read()
# except FileNotFoundError:
#     print("파일 없음")
# finally:
#     file.close()

# try:
#     num1 = int(input("숫자1 : "))
#     num2 = int(input("숫자2 : "))
#     result = num1 / num2
# except ValueError:
#     print("숫자만 입력 하시오")
# except ZeroDivisionError:
#     print("0 이상 숫자만 입력 하시오")
# else:
#     print(result)

# try: # 오류 발생
#     file = open("hello.txt", "r")
#     content = file.read()
# except FileNotFoundError:
#     print("파일이 존재 하지 않습 니다.")
# else:
#     print(content)
# finally:
#         file.close()

# 리스트 요소 5개 선언 하고 index 찾는 로직
# 예외 처리 => "해당 인덱스 가 존재 하지 않습 니다" 출력
# 정상 이면 해당 인덱스 값 출력
# 마지막 은 항상 "끝!!"을 출력

# my_list = [1, 2, 3, 4, 5] # 내가 한거
#
# try:
#     index = int(input("인덱스 입력"))
#     list = my_list[index]
#
# except IndexError:
#     print("인덱스 가 존재 하지 않는다")
# else:
#     print(list)
# finally:
#     print("끝")


# my_list = [1, 2, 3, 4, 5]
# try:
#     index = int(input("인덱스 를 입력해 주세요"))
#     result = my_list[index]
# except IndexError:
#     print("인덱스 범위 벗어남")
# else:
#     print(result)
# finally:
#     print("끝!")


# try:
#     age = int(input("나이를 입력 하시오 : "))
#
#     if age < 0 or age > 150:
#         raise  Exception("0 이상 150 미만 숫자만 입력 하시오")
# except Exception as e:
#     print(e)
# else:
#     print(age)
# finally:
#     print("끝")

# class AgeException(Exception):
#     def __init__(self):
#         super().__init__("0 이상 150 미만 숫자만 입력 하시오")
#
# try:
#     age = int(input("나이를 입력 하시오 : "))
#
#     if age < 0 or age > 150:
#         raise  AgeException()
# except AgeException as e:
#     print(e)
# else:
#     print(age)
# finally:
#     print("끝")

# 계좌 시스템

# class FundsError(Exception):
#     def __init__(self, balance, amount):
#         super().__init__(f"출금 잔액이 부족 현재 잔액은:{balance} 출금 금액: {amount}.")
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance
#     def withdraw(self, amount):
#         try:
#             if amount > self.balance:
#                 raise FundsError(self.balance, amount)
#         except FundsError as e:
#             print(e)
#         else:
#             self.balance - amount
#             print(f"정상적 으로 출금 되었 습니다. 남은 금액: {self.balance - amount}")
# account = BankAccount(10000)
# account.withdraw(500)


# 숙제
my_dict = {1: "사과", 2: "바나나", 3: "딸기", 4: "포도", 5: "수박"}
# 딕셔 너리 키를 입력 받음(숫자로)
# result 변수에 해당 키의 값을 넣음
# 예외 처리는 해당 키가 존재 하지 않을 때 => 해당 키는 존재 하지 않습 니다.
# 그리고 숫자가 아닌 문자를 넣었을 때 => 숫자를 입력해 주세요.
# 정상적 으로 실행 되면 해당 키의 값을 넣어둔 result 출력
# 마지막 은 항상 완료를 출력







