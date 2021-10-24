import requests
from bs4 import BeautifulSoup

# requests 모듈 및 soup 모듈을 이용하여 웹에서 원하는 정보를 가져오는 코드
# response 값을 text로 파싱
url = "https://finance.naver.com/item/main.nhn?code=000660"
html = requests.get(url).text

# soup 모듈을 통해 per 값을 표현
soup = BeautifulSoup(html, "html5lib")
tags = soup.select("#_per") # CSS 셀렉터를 설정하여 해당 셀렉터의 데이터 값을 tags에 바인딩
tag = tags[0] # 구한 값 중 첫번째 값을 바인딩
print(tag)
print(tag.text) # text 속성 표현

#수익배당률 표현
tags_Befit = soup.select("#_dvr") # 수익배당률 id 값
print(tags_Befit[0].text) # 값 출력













