import pyupbit
import time

# 변동성 전파 전략 구현

# # 매매가 조회
# while True :
#     price = pyupbit.get_current_price("KRW-BTC")
#     print(price)
#     time.sleep(0.2)

# 목표가 계산
df = pyupbit.get_ohlcv("KRW-BTC")
yesterday = df.iloc[-2]
print(yesterday)
today_open = yesterday['close']
yesterday_high = yesterday['high']
yesterday_low = yesterday['low']
target = today_open + (yesterday_high - yesterday_low) * 0.5
print(target)