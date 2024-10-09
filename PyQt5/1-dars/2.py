from PyQt5.QtWidgets  import  QApplication,  QWidget
from PyQt5.QtWidgets  import  QLabel,  QLineEdit,  QPushButton
from  PyQt5.QtGui  import  QFont

import sys 
app  =  QApplication(sys.argv)

class  Pilus(QWidget):
    def  __init__(self) :
        super().__init__()
        self.setWindowTitle("kankulyator")
        self.setGeometry(100, 100,  500,  500)
        self.start()
    
    def  font(self, obj,  x  ,  y):
        obj.setFont(QFont("Times", 15))
        obj.move(x, y)

    def  start(self):
        self.son1  =  QLabel("Son1 ==>  ",  self)
        self.font(self.son1, 50, 50)
        self.son2  =  QLabel("Son2 ==>  ",  self)
        self.font(self.son2, 50, 100)

        self.son1Input =  QLineEdit(self)
        self.font(self.son1Input, 150, 50)

        self.son2Input =  QLineEdit(self)
        self.font(self.son2Input, 150, 100)

        pilus =  QPushButton("+",  self)
        self.font(pilus, 370,  75 )
        pilus.clicked.connect(self.run)


        self.natija =  QLabel("Natija  ", self)
        self.font(self.natija,  50,  150)


    def  run(self):
        if self.son1Input.text() == "":
            a  = 0
        else :
            a  =  int(self.son1Input.text())
        if self.son2Input.text()  ==  "":
            b  =  0
        else: 
            b  =  int(self.son2Input.text())
        self.natija.clear()
        self.natija.setText("Natija ")
        self.natija.setText(self.natija.text() +  str(a)+  " + " + str(b) +  " = " +  str(a  + b))
        self.natija.adjustSize()

oyna  = Pilus()
oyna.show()
app.exec_()