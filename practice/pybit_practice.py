# pybithumb 모듈을 활용하여 상승장 알리미를 만들어보자
# 빗썸의 경우 public과 private API를 제공한다.
# private의 경우 회원가입이 필요한 서비스에 대한 API 제공
# pip 명령어를 이용하여 pybithumb 모듈을 설치
import datetime
import time

import pybithumb

# 비트코인 종목 이름인 ticker 조회
tickers = pybithumb.get_tickers()
print(tickers)
print(len(tickers))

# 현재가 조회
# price = pybithumb.get_current_price("BTC")
# print(price)
# # API는 초당 20개의 호출가능 이를 이용하여 1초에 한번씩 최신 값 조회
# i = 1
# while i < 21:
#     istr = str(i)
#     print(str(pybithumb.get_current_price("BTC")) + " 횟수 " + istr)
#     time.sleep(1)
#     i = i + 1

# 코인별 현재 시세 조회

# ticker = pybithumb.get_tickers()
#
# for tic in ticker :
#     price = pybithumb.get_current_price(tic)
#     print(price, tic)
#     time.sleep(1)
#
# # 해당 코인 디테일 확인
# detail = pybithumb.get_market_detail("BTC")
# # 시가, 고가, 저가, 종가, 거래량 순으로 튜플 형태로 데이터 반환
# print(detail)
#
# # 호가 정보 확인
# orderbook = pybithumb.get_orderbook("BTC")
# # 딕셔너리 타입의 데이터로 반환
# print(orderbook)
#
# # 호가 정보 키 값 확인
# for k in orderbook :
#     print(k)
#
# # timestamp 시간 계산
# nowms = int(orderbook['timestamp'])
# nowtime = datetime.datetime.fromtimestamp(nowms/1000)
# print(nowtime)
#
#
# orderbook = pybithumb.get_orderbook("BTC")
# # 매수 호가 확인
# bids = orderbook['bids']
# # 매도 호가 확인
# asks = orderbook['asks']
# print(bids)
# print(asks)
#
# for bid in bids :
#     price = bid['price']
#     quantity = bid['quantity']
#     print("매수호가 : ", price, " 매수잔량 : ", quantity)
#
# for ask in asks :
#     print(ask)
# 여러 가상화폐를 한번에 받아오기
all = pybithumb.get_current_price("ALL")
print(all)
for ticker, data in all.items() :
    print(ticker, data['closing_price'])





