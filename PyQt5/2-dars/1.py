from  PyQt5.QtWidgets  import  QApplication,  QWidget,  QPushButton
from  PyQt5.QtWidgets  import  QCheckBox,  QLabel
from  PyQt5.QtGui import  QFont

import  sys
app  =  QApplication(sys.argv)

class  Yangi_Dastur(QWidget):
    def  __init__(self):
        super().__init__()
        self.setWindowTitle("CheckBox")
        self.setGeometry(100, 100,  600,  600)
        self.boshla()
    def  boshla(self):
        self.text  = QLabel("Siz  Qaysi  Dasturlash  tilini Bilasiz  ?",  self)
        self.text.setFont(QFont("Times",  24))
        self.text.move(50, 50)
        self.text.adjustSize()
        # !=====================================================================
        self.javob_1 =  QCheckBox("C  Dasturlash  tili", self)
        self.javob_1.setFont(QFont('Times', 20))
        self.javob_1.move(50, 100)

        self.javob_2 =  QCheckBox("Dart  Dasturlash  tili", self)
        self.javob_2.setFont(QFont('Times', 20))
        self.javob_2.move(50, 150)

        self.javob_3 =  QCheckBox("Python  Dasturlash  tili", self)
        self.javob_3.setFont(QFont('Times', 20))
        self.javob_3.move(50, 200)

        self.natija =  QPushButton("Natija", self)
        self.natija.setFont(QFont('Times', 20))
        self.natija.setGeometry(50,  270,  300, 50)
        self.natija.clicked.connect(self.run)

        self.text1  = QLabel("",  self)
        self.text1.setFont(QFont("Times",  24))
        self.text1.move(50, 350)
    def  run (self):
        if  not  (self.javob_1.isChecked()) and  not  (self.javob_2.isChecked()) and not  (self.javob_3.isChecked()):
            self.text1.setText("Dasturlash  tilini  bilmayman\n")
        else :
            self.text1.setText("Quidagilar\n")
            if  self.javob_1.isChecked():
                self.text1.setText(self.text1.text() +  self.javob_1.text() + '\n')
            if  self.javob_2.isChecked():
                self.text1.setText(self.text1.text() +   self.javob_2.text()+ "\n")
            if  self.javob_3.isChecked():
                self.text1.setText(self.text1.text() +  self.javob_3.text() + '\n')
        self.text1.adjustSize()
oyna  = Yangi_Dastur()
oyna.show()
app.exec_()
