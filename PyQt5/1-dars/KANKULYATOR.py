from os import system
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
import  sys

class  Button(QPushButton):
    models  = {
        "raqam": "grey",
        "operator": "orange",
        "symbol": "lightgrey"
    }

    def  __init__(self,  text :str,  mode =  "raqam" ):
        super().__init__()
        self.setText(text)
        self.setFixedSize(80, 80)
        self.setStyleSheet(f"""
    background-color: {self.models[mode]}
    color: {"black"  if  mode  == "symbol"  else "white"};
    font-size: 40px;
    border-radius: 40%;""")
        


app  =  QApplication(sys.argv)
class   Kalkulyator(QWidget):
    def  __init__(self):
        super().__init__()
        self.setGeometry(100, 100,  400,  600)
        self.setWindowTitle("Kalkulyator")

        self.input  =  QLineEdit("")
        self.input.setGeometry(0, 0, 150,  200)

        self.AC  = Button("AC",  "symbol")
        self.pilus_minus  = Button("+/-",  "symbol")
        self.foiz_bolish = Button("%",  "symbol")

        self.bt0 =  Button("0")
        self.bt1 =  Button("1")
        self.bt2 =  Button("2")
        self.bt3 =  Button("3")
        self.bt4 =  Button("4")
        self.bt5 =  Button("5")
        self.bt6 =  Button("6")
        self.bt7 =  Button("7")
        self.bt8 =  Button("8")
        self.bt9 =  Button("9")
        

        
        self.nolinchi  =  QHBoxLayout()
        self.nolinchi.addWidget(self.AC)
        self.nolinchi.addWidget(self.pilus_minus)
        self.nolinchi.addWidget(self.foiz_bolish)
 
        self.birinchi  =  QHBoxLayout()
        self.birinchi.addWidget(self.bt7)
        self.birinchi.addWidget(self.bt8)
        self.birinchi.addWidget(self.bt9)


        self.ikkinchi  =  QHBoxLayout()
        self.ikkinchi.addWidget(self.bt4)
        self.ikkinchi.addWidget(self.bt5)
        self.ikkinchi.addWidget(self.bt6)


        self.uchinchisi  =  QHBoxLayout()
        self.uchinchisi.addWidget(self.bt1)
        self.uchinchisi.addWidget(self.bt2)
        self.uchinchisi.addWidget(self.bt3)



        self.sonlar  = QVBoxLayout()
        self.sonlar.addWidget(self.input)
        self.sonlar.addLayout(self.nolinchi)
        self.sonlar.addLayout(self.birinchi)
        self.sonlar.addLayout(self.ikkinchi)
        self.sonlar.addLayout(self.uchinchisi)

        self.setLayout(self.sonlar)



k  =  Kalkulyator()
k.show()
app.exec_()

    