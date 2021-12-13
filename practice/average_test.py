import time
import pybithumb
import pyupbit
import sys
# getOhlc = pybithumb.get_ohlcv("BTC")
# close = getOhlc['close']
# print(getOhlc)
# print(close)
#
# # 5일치 이동평균 구하기
# window = close.rolling(5).mean()
# print(window)
#
# # 전일 이동 평균가
# ma5 = window[-2]
# # 현재가
# price = pybithumb.get_current_price("BTC")
#
# if price > ma5 :
#     print("상승장")
# else:
#     print("하락장")
#
# 해당 ticker의 상승장 하락장을 판단하는 함수 구현


f = open("../../get_token", "rt")
get_key = f.read().splitlines()
access_key = get_key[1]
secret_key = get_key[3]
f.close()
# 해당 코인의 내 잔고 확인
# upbit = pyupbit.Upbit(access_key, secret_key)
# print(upbit.get_balances())
# balance = upbit.get_balance("KRW-SAND")
# print(balance)

# 각 코인별 내 잔고 조회
upbit = pyupbit.Upbit(access_key, secret_key)
# tickers = pyupbit.get_tickers(fiat="KRW")
# for ticker in tickers:
#     balance = upbit.get_balance(ticker)
#     if balance > 0:
#         print(ticker, " : ", balance)
#     time.sleep(0.5)
print("end")

# 현재 잔고와 코인의 호가를 조회하여 매수할 수 있는 수량을 계산하는 코드
price = upbit.get_balances()
krw = price[0]['balance']
orderbook = pyupbit.get_orderbook("KRW-BTC")
ask = orderbook['orderbook_units']
sell_price = ask[0]['ask_price']
print(sell_price)
unit = float(krw) / sell_price

print(unit)

# 매수 수량 확인 후 수량만큼 매수
# order = upbit.buy_market_order("KRW-BTC", 20000)
# print(order)

# 매도 진행






# def bull_market(ticker):
#     get_ohlc = pyupbit.get_ohlcv(ticker)
#     close = get_ohlc['close'].rolling(window=5).mean()
#     get_current_ma5 = close[-2]
#     current_bill = pyupbit.get_current_price(ticker)
#     if current_bill > get_current_ma5:
#         return True
#     else:
#         return False
#
#
# tickers = pyupbit.get_tickers(fiat="KRW")
# for ticker in tickers:
#     if bull_market(ticker):
#         print(ticker, "상승장")
#     else:
#         print(ticker, "하락장")
#     time.sleep(1)
#

