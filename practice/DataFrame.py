# series 타입의 경우 1차원 데이터를 다루지만 Pandas의 DataFrame은 2차원 데이터를 저장하는 구조를 가지고 있다.
# 이를 활용하여 딕셔너리 등에 다양한 활용이 가능

# import data frame
from pandas import DataFrame
from pandas import Series

# 딕셔너리를 통해 data Frame 객체 생성
data = {"open" : [200, 220], "high" : [400, 420], "low" : [100, 200], "close" : [350, 330]}
# 인덱스를 문자열로 설정하여 data frame 객체 생성
df = DataFrame(data, index = ["2021-01-02", "2021-01-03"])
print(df)

# 엑셀에 저장된 데이터를 이용하여 data frame 객체 생성
# pandas에서 사용하는 read_excel 함수 사용
# pandas를 pd로 이름 변경
import pandas as pd

df2 = pd.read_excel("/Users/ryuchan-ul/Desktop/test/ohlc.xlsx")
print(df2)

# 자동으로 생성된 index 번호를 data로 맵핑
df2 = df2.set_index('data')
print(df2)

# 열 조회
print("열 조회")
print(df2["open"])
# 행 조회
print("행 조회")
print(df2.loc["2021-01-22"])
# 열 추가
s = Series([300, 400])
df2["volume"] = s

# 데이터를 엑셀로 변환
df2.to_excel("/Users/ryuchan-ul/Desktop/test/ohlc2.xlsx")

# html의 정보를 가져와서 data frame 데이터 생성
# 일별 시세 정보가 있는 웹페이지
print("html 시작")
url = "https://finance.naver.com/item/sise_day.nhn?code=000660"
# 네이버 시세는 웹페이지 요청이 아니면 응답을 하지 않기 때문에 requests 모듈을 통해 요청
import requests

headers2 = {'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'}
df_html = pd.read_html(requests.get(url, headers=headers2).text)
print(df_html[0])

# NaN의 경우 네이버의 숨겨진 table 때문에 출력되는데 이는 axis = 0 을 파라미터로 전달하는데 이를 이용하여 NaN 값을 삭제
print(df_html[0].dropna(axis=0))


