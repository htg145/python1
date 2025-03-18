# 내장 함수
# 파이썬 에서 기본적 으로 지원 하는 함수 (built_in function)

#abs()
# 숫자의 절댓값 을 리턴 하는 함수
# print(abs(-10))
# print(abs(-1.2))

#all()
#all(x)는 반복 가능한 데이터 (리스트, 튜플, 딕셔 너리, 튜플) x를 입력값 으로 받으면
# 이 x의 요소가 모두 참이면 True, 거짓이 하나 라도 있으면 False 를 리턴
# num_list = [1,2,0,4]
# print(all(num_list))
# num_list = []
# print(all(num_list))

#any()
# 애는 그냥 all 의 반대
#all(x)는 반복 가능한 데이터 (리스트, 튜플, 딕셔 너리, 튜플) x를 입력값 으로 받으면
# 이 x의 요소가 하나 라도 참이면 True, 요소가 모두 거짓 이면 False 를 리턴
# num_list = [1,2,0,4]
# print(any(num_list))
# num_list = [0,0,0,0]
# print(any(num_list))

#chr()
#chr(i)는 유니 코드 를 넣으면 해당 문자로 리턴 하는 함수
# print(chr(97)) #a
# print(chr(44032)) #가

#dir()
# 객체가 지닌 변수나 함수를 보여 주는 함수
# name = "python"
# print(dir(name))
# name. 찍으면 나오 는거


#divmod()
# 2개의 숫자 a,b를 입력 받고 그리고 a를 b로 나눈 몫과 나머지 를 튜플로 리턴
# print(divmod(7,3))

# enumerate()
# 순서가 있는 데이터(리스트, 튜플, 문자열)를 입력 받아서 인덱스 값을 포함 하는
# a_list = ["name", "age", "birth"]
# for i, name in enumerate(a_list):
#     print(i, name)

#evel()
# 문자열 로 구성 되어 있는데 해당 문자열 을 실행한 값
# print(eval("1+2"))
# print(eval("div mod(7,2)"))

# filter() # 자주 쓰임
# 첫번째 인수로 함수, 두번째 인수로 반복 가능한 데이터
# 그리고 반복 가능한 데이터 의 요소 순서 대로 함수를 호출 했을때
# 리턴 값이 참인 것만 묶어서 리턴
# def positive(x): # ()매개 변수
#     return x > 0
# print(list(filter(positive, [1, -2, 5, -3, 8])))

#hex()
# 정수를 입력 받아 16진수 문자열 로 변환 하여 리턴 하는 함수
# print(hex(234))
# print(hex(3))

#id()
# 객체를 입력 받아서 고유 주솟값 (래퍼 런스)를 리턴 하는 함수
# a = 3
# print(id(a))

#map 많이 쓰임
#map은 입력 받은 데이터 의 각 요소에 함수 f를 적용한 결과를 리턴
# def tow_time(x):
#     return  x*2
# print(list(map(tow_time, [1, 2, 3, 4])))

#max()
# 반복 가능한 데이터 중에서 최댓값 리턴
# num_list = [1, 3, 13, 15, 45]
# print(max(num_list))

#min()
# 반복 가능한 데이터 중에서 최솟값 리턴
# print(min(num_list))

#oct()
#oct()는 정수를 8진수 문자열 로 바꾸어 리턴 하는 함수
# print(oct(34))
# print(oct(500))

#open()
#open(fileName, [mode])은 "파일 이름"과 "읽기 방법"을
# 입력 받아 파일 객체를 리턴 하는 함수
# w 쓰기 모드
# r 읽기 모드
# a 추가 모드
# b 바이 너리 모드
# file = open("as.text", "r", encoding="utf-8")
# print(file)
# content = file.read()
# print(content)
# # 닫는것
# file.close()

# 닫는 것 까지 한다 with 같이 쓴다
# with open("as.text", "r", encoding="utf-8") as file:
#     content = file.read()
#     print(content)

#ord()
#ord()는 문자의 유니 코드 불러 오기
# print(ord("라"))

#pow()
# 첫번째 인수의 두번째 인수 만큼 거듭 제곱 한 값을 리턴
# print(pow(2, 10))

# range()
#range(시작, 끝, 간격) for 문 과 함께 자주 사용
#이 함수는 입력 받은 숫자에 해당 하는 범위 값을 반복 가능한 객체로 만들어 리턴
# print(list(range(5, 10, 2)))

# round()
# 반올림
# print(round(4.4))
# print(round(5.152, 2))

# sum()
# 합계
# num_list = [1234, 24154, 4124, 2312]
# print(sum(num_list))

# 공식 문서 보는법 숙지 파이션 사이트 docs , 넘파이, 리액트(자바), 플럭터, 스위 프트




# 메소드 (.찍으면 나오 는거)
# object(객체)와 연관 되어 사용
# object.method_name()


