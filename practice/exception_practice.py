import pybithumb
import time

# try, except 구문을 사용하여 예외처리
while True :
    price = pybithumb.get_current_price("BTC")
    try :
        print(price/10)
    except :
        print("error ", price)
    time.sleep(1)
