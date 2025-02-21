# 딕셔너리
# from collections.abc import async_generator
#
# person = {
#     "이름":"철수",
#     "나이":25,
#     "취미":["독서","영화감상",]
# }
# print(person)
#
# profile = {
#     "name" : "박찬호",
#     "age" : 25,
#     "hobby" : ["여행하기", "영화보기"]
# }
# profile["age"] = 28 #키가 존재 하면 수정 된다
# print(profile)
#
# profile["jod"] = "강사" #키가 존재 하지 않는 것은 추가 된다
# print(profile)
#
# del profile["jod"] #삭제
# print(profile)
#
# key_list = list(profile.keys())
# key_list.append("jod")
# print(key_list)
#
# profile.values() #값만 뽑아내기
# value_list = list(profile.values())
# print(value_list)
#
# profile.items() #키-값 형태로 나온다
# itme_list = list(profile.items())
# itme_list.append(("jod", "강사"))
# print(itme_list)
from operator import index
from platform import java_ver
from tkinter.font import names

# python_grade = {
#     "찬호" : "b",
#     "길동" : "c",
#     "준식" : "a",
#     "창식" : "d"
# }
# print(sorted(python_grade.items())) #키 기준 오름 차순
# print(sorted(python_grade.items(), reverse=True)) #키 기준 내림 차순
#
# print(sorted(python_grade.items(),key=lambda x: x[1])) #값 기준 오름 차순
# print(sorted(python_grade.items(), key=lambda x: x[1], reverse=True)) #값 기준 내림 차순
#
# student = {}
# # 이름 입력 받고 점수도 입력 받고 딕셔너리에 저장
# # {"name": "박찬호", "score": 80}
#
# # 첫번째 방법
# # student = {
# #     "name": input("이름 : "),
# #     "score": input("점수 :")
# # }
#
# # 두번째 방법 쉬움
# student["name"] = input("이름 :")
# student["score"] =int(input("점수 :"))
# print(student)

# # 세트 중복 허용 하지 않는다
# fruits = {"사과", "딸기", "귤", "귤"} # 세트
# print(fruits)
# apple_str = str("apple")
# print(apple_str)
#
# num= {1, 2, 3, 4, 5, 5}
# num.add(8) # 하나씩 추가
#  #num.remove(19) # 삭제 #삭제 오류냄
# num.discard(19) # 삭제 오류안냄
# # num.update([10, 11, 12]) # 여러게 요소 추가


# print(num)
#
# empty_set = set() #빈 세트를 선언
#
# num.clear() # 요소 전체 제거
# print(num)
#
# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}
# #합집합
# print(a.union(b))
# print(a|b)
#
# #교집합
# print(a.intersection(b))
# print(a & b)
#
# #차집합
# print(a.difference(b))
# print(a - b)

# color = {"b", "l", "u", "e"}
# print(color.pop())
# print(color)

# a = [21, 22, 23, 25, 26]
# b = [22, 24, 27]
# common = set(a) & set(b)
# print(common)

python_class = ["수현", "현호", "지니", "가인"]
java_class = ["현호", "지니", "홍수", "찬호"]

#공통으로 출석한 학생:
common_class = set(python_class) & set(java_class)
print(common_class)
#파이썬만 출석한 학생:
python = set(python_class) - set(java_class)
print(python)
#자바만 출석한 학생:
jave = set(java_class) - set(python_class)
print(jave)


# common = set(python_class) & set(java_class)
# print(common)











































