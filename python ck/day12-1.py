# 모듈화 : 복잡한 프로 그램을 작은 단위로 나누어 관리 하고 개발 하는 것
# 모듈 : 함수나 변수 또는 클래스 를 모아 놓은 파이썬 파일
# 사용 하는 이유: 코드 재 사용성
# 표준 모듈 : 파이썬 에서 기본적 으로 제공 하는 내장 모듈
# 별도의 설치 없이 import 문을 사용 하여 바로 활용 가능 json(데이터 처리 모듈), random, type, re(정규 표준식 모듈)
import math
# math - 수학 관련 모듈

# ceil - 올림
# print(math.ceil(3.14))

# copysign = 두 번쨰 인자의 부호만 취해 첫 번째 인자에 적용
# print(math.copysign(3.14, -+1))

# fabs - 절댓값 을 반환 하는 매소드
# print(math.fabs(-3.14))

#factorial - 팩토 리얼 구한는 메소드
# print(math.factorial(7))

#floor - 내림
# print(math.floor(3.14))

# gcd - 두 수의 최대 공약수
# print(math.gcd(6, 8))

# modf - 정수 부분과 소수 부분을 분리 해서 리턴 # 부동 소수점 의 오류
# print(math.modf(3.14))

# trunc - 내림 0쪽으로 내림
# print(math.floor(-3.14)) # 무조건 아래로 내림
# print(math.trunc(-3.14)) # 0으로 향해서 내림

# log(a, b) - b를 밑으로 하는 log a에 대한 로그 값
# print(math.log(10, 10))

# 원주율
# print(math.pi)

import random

# 난수
# print(random.random())
#
# print(random.randint(1, 10))
#
# print(random.randrange(1, 10, 2))

# shuffle 썩는다
# abc = ["a","b","c","d","e"]
# random.shuffle(abc)
# print(abc)

# choice 썩어서 하나 뽑는다
# abc = ["a","b","c","d","e"]
# print(random.choice(abc))
#
# meun = "삼겹살", "된장 찌개", "맥주", "소주"
# print(random.choice(meun))

from datetime import datetime, time, timedelta
from time import strftime

# 현재 날짜
# now = datetime.now()
# print(now)
#
# one_week_later = now + timedelta(days=7)
# print(one_week_later)
#
# formatter_date = now.strftime("%Y-%m,%d,%H:%M,%S")
# print(formatter_date)

# import os
#
# # print(os.getcwd()) # 현재 디렉 토리
# # print(os.listdir()) # 현재 폴더의 파일 목록
#
# if not os.path.exists("new_folder"):
#     os.mkdir("new_folder") # 폴더 생성

import re # 정규 표현식
def validate_email(email):
    """이메일 주소 유효성 검사"""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$" # ai 물어 봐라
    if re.match(pattern, email):
        return True
    else:
        return False

email1 = "htg145@naver.com"

print(f"{email1}: {validate_email(email1)}")




