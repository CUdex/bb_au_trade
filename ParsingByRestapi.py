# restAPI를 이용하여 데이터를 구하는 코드
import requests
import datetime

url = "https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw"
r = requests.get(url)
# 반환 값은 기본적으로는 문자열 데이터이다.
print(r.text)

# 반환받은 response 값은 json 함수를 통해 json 데이터로 캐스팅한다.
bitcoin_data = r.json()
print(bitcoin_data)
# json 형태로 저장되어 key 값으로 데이터를 불러올 수 있다.
print(bitcoin_data['last'])

# timestamp의 경우 1970-01-01로부터 지난 시간을 나타내는 것인데 이를 사람이 읽기 쉬운 시간으로 표시하기 위해서는
# datetime 모듈을 이용한다.
date = bitcoin_data['timestamp']
realDate = datetime.datetime.fromtimestamp(date/1000)
print(realDate)


