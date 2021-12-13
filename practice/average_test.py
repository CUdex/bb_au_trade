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

upbit = pyupbit.Upbit(access_key, secret_key)
print(upbit.get_balances())
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

