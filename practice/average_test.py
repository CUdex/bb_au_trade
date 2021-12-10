import pybithumb

getOhlc = pybithumb.get_ohlcv("BTC")
close = getOhlc['close']
print(getOhlc)
print(close)

# 5일치 이동평균 구하기
window = close.rolling(5).mean()
print(window)