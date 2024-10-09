from  PyQt5.QtWidgets  import  QApplication,  QWidget,  QPushButton
from  PyQt5.QtWidgets  import  QComboBox,  QLabel ,  QMessageBox
from  PyQt5.QtGui import  QFont, QIcon

import  sys
app  =  QApplication(sys.argv)

class  Yangi_Dastur(QWidget):
    def  __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox")
        self.setGeometry(100, 100,  600,  600)
        self.start()
        # !=============================
    def  start(self):
        self.matn = QLabel("Siz  qaysi  yo'nalishni  tanlaysiz.?",self)
        self.matn.setFont(QFont("Times",  20))
        self.matn.move(50, 50)

        self.combo =  QComboBox(self)
        self.ls  = [ "Foundation", 'Flutter',  'Go', 'Java', '.Net']
        self.combo.addItems(self.ls)
        self.combo.setFont(QFont("Times",  20))
        self.combo.setGeometry(50,  120,  200,  50)

        ok =  QPushButton("Ok", self)
        ok.setFont(QFont("Times", 20))
        ok.setGeometry(300, 120,  216,  53)
        ok.clicked.connect(self.run)

        self.natija = QLabel("Salom",self )
        self.natija.setFont(QFont("Times",  20))
        self.natija.move(50, 250)

    def  run(self):
        ogoxlantir  =  QMessageBox(self)
        ogoxlantir.setFont(QFont("Times",  10))
        ogoxlantir.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        if  self.combo.currentText() == "":
            ogoxlantir.setText("Siz  Yo'nalish  tanlamadingiz !")
            ogoxlantir.show()
        else:
            ogoxlantir.setText('Siz  ' + self.combo.currentText() +  " yo'nalishni tanladingiz")
            n  =  ogoxlantir.exec_()
            if  n  ==  QMessageBox.StandardButton.Ok:
                tabrik  = "Najot  Ta'limda  Result  Bosqichi  Uchun \n"
                self.natija.setText(tabrik +  self.combo.currentText() + " ni Tanladingiz" )
            if   n  ==  QMessageBox.StandardButton.Cancel:
                print("Orqaga")
            ogoxlantir.show()
        self.natija.adjustSize()
        
        
        


    

oyna  = Yangi_Dastur()
oyna.show()
app.exec_()
