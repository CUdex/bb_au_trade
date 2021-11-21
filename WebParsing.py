# 태그가 존재하는 데이터를 파싱하는 코드입니다.


import requests
from bs4 import BeautifulSoup

# # requests 모듈 및 soup 모듈을 이용하여 웹에서 원하는 정보를 가져오는 코드
# # response 값을 text로 파싱
# url = "https://finance.naver.com/item/main.nhn?code=000660"
# html = requests.get(url).text
#
# # soup 모듈을 통해 per 값을 표현
# soup = BeautifulSoup(html, "html5lib")
# tags = soup.select("#_per") # CSS 셀렉터를 설정하여 해당 셀렉터의 데이터 값을 tags에 바인딩
# tag = tags[0] # 구한 값 중 첫번째 값을 바인딩
# print(tag)
# print(tag.text) # text 속성 표현
#
# #수익배당률 표현
# tags_Befit = soup.select("#_dvr") # 수익배당률 id 값
# print(tags_Befit[0].text) # 값 출력

# PER값을 구하는 함수
def get_per(code) :
    url = "https://finance.naver.com/item/main.nhn?code=" + code
    html = requests.get(url).text

    soup = BeautifulSoup(html, "html5lib")
    tags = soup.select("#_per")
    tag = tags[0]
    return float(tag.text)

#수익배당률을 구하는 함수 구현
def get_diviend(code) :
    url = "https://finance.naver.com/item/main.nhn?code=" + code
    html = requests.get(url).text

    soup = BeautifulSoup(html, "html5lib")
    tags = soup.select("#_dvr")
    tag = tags[0]
    return float(tag.text)



#PER 출력
print(get_per("000660"))

#수익배당률 출력
print(get_diviend("000660"))
