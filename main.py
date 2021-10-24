import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pykorbit
from PyQt5.QtCore import *
import requests

form_class = uic.loadUiType("untitled.ui")[0]

class MyWindow(QMainWindow, form_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.timerSet = QTimer(self)
        self.timerSet.start(1000)
        self.timerSet.timeout.connect(self.inquiry)
        mysignal = MySigner()
        mysignal.signal1.connect(self.signal1_emitted)
        mysignal.signal2.connect(self.signal2_emitted)
        mysignal.run()

    @pyqtSlot()
    def signal1_emitted(self):
        print("signal1 emitted!")
    @pyqtSlot(int, int)
    def signal2_emitted(self, arg1, arg2):
        print("signal2 emitted", arg1, arg2)


    def inquiry(self):
        cur_timer = QTime.currentTime()
        str_timer = cur_timer.toString("hh:mm:ss")
        self.statusBar().showMessage(str_timer)
        price = pykorbit.get_current_price("BTC")
        self.lineEdit.setText(str(price))

class MySigner(QObject) :
    signal1 = pyqtSignal()
    signal2 = pyqtSignal(int, int)

    def run(self):
        self.signal1.emit()
        self.signal2.emit(1, 2)



# app = QApplication(sys.argv)
# window = MyWindow()
# window.show()
# app.exec_()

url = "http://www.naver.com"
res = requests.get(url)
print(res.text)
