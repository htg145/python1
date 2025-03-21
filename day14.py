# 클래스 - 설계도, 설명서 (class) 구성: 속성(모델명, 가격, 종류)-생성자, 기능(앞으로, 뒤로)-메소드
# 객체 - 오브 젝트(object)  설계도 로 만들어 졌다 instance (인스 턴스) 라고 말할수 있다
# 클래스 정의와 생성자, 메서드
from numpy.f2py.crackfortran import crackline_re_1


# class 클래스 이름: 케이스 - 스네 이크 케이스
#     def __init__(self, 매개 변수): self 꼭 있어야 함 # 생성자, __init__(속성 정의)
#       self.변수1 = 매개 변수

# 소멸자 - 당장 소멸 시켜야 할 때, 소멸 되기 전 무언가 처리 해야할 때
# class 클래스 이름:
#     def __del__(self):
#        소멸자 코드

# 소멸자
# class Example:
#     def __init__(self, name):
#         self.name = name
#         print(f"{self.name} 객체가 생성됨.")
#
#     def __del__(self):
#         print(f"{self.name} 객체가 소멸됨.")
#
# # 객체 생성
# obj1 = Example("테스트") # 객체 생성
#
# # 객체 삭제 (명시적 으로 삭제 하지 않아도 자동 으로 삭제 합니다.)
# del obj # 객제 삭제 - 소멸자 삭제

# class Car:
#     pass # 일단 정의 한다 뭐 들어 갈지 모른다
#
# a = 10
# if a < 100:
#     pass # 일단 패스 그냥 지나감 오류 안뜨고
#
# while True:
#     pass

# class Car: # 클래스 정의
#     def __init__(self, model, price): # 생성자
#         self.model = model
#         self.price = price
#         print(f"모델 이름:{self.model}, 가격:{self.price} 객체 생성!!")
#
#     def __del__(self): # 소멸자
#         print(f"{self.model}의 객체가 소멸 됨!!")
#
#     def drive(self, speed, distance):
#         print(f"{self.model}가 {speed}의 속도가 {distance}km 만큼 전진")
#
#
#
# car1 = Car("avante", 2400) # car1 객체 생성 (Car 클래스 의 인스 턴스)
# car1.is_n = False,"아님" # 멤버 변수
# print(car1.is_n)
#
# print(f"car1의 모델명: {car1.model}")
# print(f"car1의 가격: {car1.price}")
# car1.drive(80, 1)
# Car.drive(car1, 120, 5)
#
# # print(isinstance(car1, Car)) # Car 로 만들 어진 인스 턴스가 맞다
# car2 = Car("santafe", 4000) # car2 객체 생성 (Car 클래스 의 인스 턴스)
# car2.drive(50, 10)

# class Player:
#     def __init__(self, nickname, hp, gold=0, level=0):
#         self.nickname = nickname
#         self.hp = hp
#         self.level = level
#         self.gold = gold
#         print(nickname, hp, gold, level)
#
#     def __del__(self):
#         print("저장 중")
#         print("저장 되었 습니다.")
#
#     def del_player(self):
#         print("케삭 되었 습니다.")
#
#     def change_nickname(self, new_nickname):
#         self.nickname = new_nickname
#
# player1 = Player("yoon", 5000,  1000,  100)
# player1.change_nickname("doog")
# print(player1.nickname)

# def func(age ,name ="홍길동"):
#     print(age, name)
#
# func(27)

class Person:
    def __init__(self, age, email, name="홍길동"):
        self.name = name
        self.age = age
        self.email = email
    def introduce(self):
        print(f"이름은{self.name}이고 나이는 {self.age}이고 이메일은 {self.email}")
person1 = Person(27, "htg145@naver.com")

print(person1)


# 상속 다음주 수업
# 상속 개념
# 부모 클래스(Parent Class, Superclass): 속성과 메서드 를 물려 주는 기존 클래스 입니다.
# 자식 클래스(Child Class, Subclass): 부모 클래스 속성과 메서드 를 물려 받아 새로운 클래스 를 정의 합니다.


# 제미 나이

class Movie:
    def __init__(self, title, director, actors, year, genre, rating):
        self.title = title
        self.director = director
        self.actors = actors
        self.year = year
        self.genre = genre
        self.rating = rating

    def __str__(self):
        return f"{self.title} ({self.year}), 감독: {self.director}, 장르: {self.genre}, 평점: {self.rating}"

    def get_actors(self):
        return ", ".join(self.actors)

    def get_info(self):
        print(f"제목: {self.title}")
        print(f"감독: {self.director}")
        print(f"배우: {self.get_actors()}")
        print(f"개봉 연도: {self.year}")
        print(f"장르: {self.genre}")
        print(f"평점: {self.rating}")

# 영화 객체 생성
movie1 = Movie("기생충", "봉준호", ["송강호", "이선균", "조여정"], 2019, "드라마", 8.6)
movie2 = Movie("어벤져스: 엔드게임", "루소 형제", ["로버트 다우니 주니어", "크리스 에반스", "스칼렛 요한슨"], 2019, "액션", 8.4)

# 영화 정보 출력
print(movie1)
movie2.get_info()







