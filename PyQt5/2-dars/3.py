from  PyQt5.QtWidgets  import  QApplication,  QWidget,  QPushButton
from  PyQt5.QtWidgets  import  QRadioButton,  QLabel,  QMainWindow
from  PyQt5.QtGui import  QFont

import  sys
app  =  QApplication(sys.argv)

class  Yangi_Dastur(QWidget):
    def  __init__(self):
        super().__init__()
        self.setWindowTitle("QRadioButton")
        self.setGeometry(100, 100,  600,  600)
        self.dastur()
    
    def  dastur(self):
        self.t  = QLabel("Tanlang Guruhni", self)
        self.t.setFont(QFont("Times",  20))
        self.t.move(50,50)


        self.radio1  =  QRadioButton("Foundation",  self)
        self.radio1.setFont(QFont("Times",  20))
        self.radio1.move(50,100) 

        self.radio2  =  QRadioButton("Suniy  Intelekt",  self)
        self.radio2.setFont(QFont("Times",  20))
        self.radio2.move(50,150)         
    
oyna  = Yangi_Dastur()
oyna.show()
app.exec_()
