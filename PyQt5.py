import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 200, 300, 400)#메서드의 인자로 4개의 정숫값을 넘겨주는데 순서대로 모니터에 왼쪽 상단으로부터 윈도우가 출력되는 x축 위치, y축 위치, 윈도우의 너비, 윈도우의 높이를 의미합니다. 
        
        self.setWindowTitle("PyQt")#타이틀바 타이틀 변경
        
        self.setWindowIcon(QIcon("icon.png"))#실행되는 창의 아이콘 변경
        
        
        #버튼생성
        btn = QPushButton("버튼1", self)
        btn.move(10, 10)
        btn.clicked.connect(self.btn_clicked)#버튼에 클릭이벤트 추가

        btn2 = QPushButton("버튼2", self)
        btn2.move(10, 40)

    def btn_clicked(self):
        print("버튼 클릭")

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()