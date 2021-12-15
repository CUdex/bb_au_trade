import pyupbit

# 목표가 계산
def get_target_price(ticker):
    df = pyupbit.get_ohlcv(ticker)
    yesterday_value = df.iloc[-2]

    open_value = yesterday_value['close']
    high_value = yesterday_value['high']
    low_value = yesterday_value['low']

    target_value = open_value + (high_value - low_value) * 0.5
    return target_value

# 자정에 목표가 갱신


get_target_price("KRW-BTC")