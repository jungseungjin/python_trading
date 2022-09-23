# -*- coding: utf-8 -*-
# import sys 
# from PyQt5.QtWidgets import *

# # PyQt로 프로그래밍을 작성할 때는 일반적으로 다음의 두 가지가 필요합니다.
# # 1) QApplication 클래스의 인스턴스 
# # 2) 이벤트 루프 
# # PyQt에서 이벤트 루프는 QApplication 클래스의 exec_() 메서드를 호출함으로써 생성할 수 있습니다.  
# app = QApplication(sys.argv)# QApplication 객체 생성
# label = QLabel("Hello")
# label.show()
# app.exec_()# 이벤트 루프 생성

# 이번에는 QLabel 클래스 대신 QPushButton 클래스를 사용해봅시다.
#  QPushButton 객체를 바인딩하는 변수 이름은 변경하지 않아도 되지만 버튼을 바인딩하고 있으므로 변수 이름도 적당히 'btn'으로 변경했습니다.

# import sys
# from PyQt5.QtWidgets import *

# app = QApplication(sys.argv)         

# btn = QPushButton("Hello")    # 버튼 객체 생성
# btn.show()

# app.exec_()                          # 이벤트 루프 생성


import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        # MyWindow 클래스의 초기화자에 super().__init__() 이라는 코드가 있습니다. 
        # 여기서 super()는 파이썬의 내장 함수 (파이썬이 설치되면 기본적으로 제공되는 함수)입니다. 
        # MyWindow 클래스는 QMainWindow 클래스를 상속받는데 자식 클래스가 부모 클래스에 정의된 함수를 호출하려면 'self.부모클래스_메서드()' 처럼 적으면 됩니다. 
        # 그런데 __init__() 이라는 초기화자는 자식 클래스에도 있고 부모 클래스에도 있습니다. 
        # 이 경우 self.__init__() 이라고 적으면 자식 클래스 (MyWindow)의 초기화자를 먼저 호출하게 됩니다. 
        # 따라서 부모 클래스에 정의된 초기화자를 명시적으로 호출하려고 상속 구조에서 부모 클래스를 찾아서 리턴해주는 super()를 적은 후__init__() 메서드를 호출하는 겁니다.
        super().__init__()
        # 이거라고 생각하면 쉬움
        # 상속을 받는다고 항상 해야하는건 아니지만 QMainWindow클래스에서는 __init__을 해주지 않으면 오류남.
        # parent = super()
        # parent.__init__()


app = QApplication(sys.argv)
window = MyWindow()
window.show() #여기서에 사용하는 show메서드는 QMainWindow클래스에 있는것
app.exec_()