# 외부 모듈
# pip 기본 명령어
# pip install 모듈명 ( 특정 패키지 를 설치 합니다.)
# pip install --upgrade 모둘명 (최신 버전 으로 업그 레이드 합니다.)
# 자주 사용 하는 외부 모듈
# requests # HTTP # 요청을 쉽게 보낼수 있는 모듈
# Beautiful Soup  # 웹 크롤링 작업을 수행
# pandas
# num pai
# flask # API 서버 만들수 있다
# import pandas as pd

# import  requests
#
# response = requests.get("https://www.naver.com/")
# print(response.status_code) # 200 뜨면 정상 사이트, 404 오류
# print(response.text)

# import pandas as pd
#
# df = pd.read_csv("data.csv")
# # print(df)
# # print(df.describe()) # 데이터 요약 분석
#
# """
# count - 해당 열의 데이터 갯수
# mean - 평균값
# std - 표준 편차 (데이터 의 분산 정도)
# min - 최솟값
# 25% - 데이터 25% 지점
# 50% - 데이터 50% 지점
# 75% - 데이터 75% 지점
# mix - 최댓값
# """
#
# print(df["Age"])
# print(df[["Age", "Salary"]])

# import matplotlib.pyplot as plt # 문제 발생
# import pandas as pd
# from numpy.ma.core import zeros, filled
#
# df = pd.read_csv("your_data.csv")
#
# # 그룹화 및 평균 계산 후 시각화
# df.groupby("Age")["Salary"].mean().plot(kind="bar")
# plt.show()

# import numpy as np
#
# arr1 = np.array([1, 2, 3, 4, 5])
# print(arr1)
#
# # 0 으로 채운 다 차원
# zeros = np.zeros((3,4))
# print(zeros)
#
# # 1로 채운 다차원 배열
# ones = np.ones((3, 4))
# print(ones)
#
# # 특정한 값으로 채운 다 차원 배열
# filled = np.full((3, 4),5)
# print(filled)
#
# # 연속된 값으로 채운 다차원 배열
# arr = np.arange(1, 10, 2)
# print(arr)
#
# # 랜덤 값으로 채운 다차원 배열
# random_arr = np.random.randint(1, 100, (3, 4))
# print(random_arr)
#
# arr1 = np.array([1, 3, 5])
# arr2 = np.array([2, 5, 8])
#
# print(arr1 + arr2)
# print(arr1 - arr2)
# print(arr1 * arr2)
# print(arr1 / arr2)

# import matplotlib.pyplot as plt  # 오류 발생
# # seaborn
# import seaborn as sns
#
#
# df = pd.read_csv("tip.csv")
# plt.figure(figsize=(8, 5))
# sns.scatterplot(x="total_bill", y="tip", hue="sex", data=df, palette="set1" )
# plt.xlabel("Total Bill ($)")
# plt.ylabel("Tip ($)")
# plt.show()


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd  # pandas 라이브러리 추가


df = sns.load_dataset("tips") # seaborn 내장 데이터셋 로드
plt.figure(figsize=(8, 5))
sns.scatterplot(x="total_bill", y="tip", hue="sex", data=df, palette="set1")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.show()



