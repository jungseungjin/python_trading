import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
#qt designer로 만든 ui 파일을 사용해보자.

#uic 모듈의 loadUiType() 메서드는 Qt Designer의 결과물인 mywindow.ui 파일을 읽어서 파이썬 클래스 코드를 만듭니다.
form_class = uic.loadUiType("window.ui")[0]

#MyWindow 클래스는 QMainWindow와 form_class로부터 다중 상속을 받고, 
# 초기화자 (__init__)에서 setupUi() 메서드를 호출합니다. setupUi()는 form_class에 정의된 메서드로 Qt Designer에서 만든 클래스들을 초기화합니다.
class MyWindow(QMainWindow,form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        self.customPushButton.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        print("버튼 클릭")

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()

#하지만 Qt Designer를 통해 위젯을 생성하면, XML로 작성되는 위젯을 파이썬 변수에 바인딩할 수 없게 됩니다. 
# 이러한 문제를 해결하기 위해 Qt Designer는 위젯을 바인딩할 변수를 지정하는 기능을 제공합니다. 
# 그림 3-42와 같이 버튼 위젯을 선택한 후 '속성 편집기' 항목을 보면 objectName에 'pushButton'이라고 되어 있는 것을 확인할 수 있습니다. 
# 이 값이 파이썬에서 버튼 이벤트를 정의할 때 사용할 변수의 이름입니다.