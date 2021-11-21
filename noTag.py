# 태그가 없는 데이터를 파싱하는 파일입니다.

import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.nhn?code=000660"
html = requests.get(url).text

soup = BeautifulSoup(html, "html5lib")
tags = soup.select("table tbody tr td em")

# 겹치는 셀렉터 값이 많아 무수히 많은 데이터가 출력
# for tag in tags :
#     print(tag.text)

# 좀 더 구체화된 데이터 셀렉트
tags = soup.select("#tab_con1  div:nth-child(3)  table  tbody  tr.strong  td  em")
for tag in tags :
    print(tag.text)
