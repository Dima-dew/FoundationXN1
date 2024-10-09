from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget,  QApplication,  QPushButton
from  malumotlar  import  Malumot_Amallar
from asosiy import  Asosiy
import  os; os.system("cls")


app = QApplication([])
class Boshqarish(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500,  800)
        self.setWindowTitle("Dokon  Loyixasi")
        #!========================================
        self.start()
    def  start(self):   

# //!=========================================================

        self.table_yaratish = QPushButton("Table  yaratish", self)
        self.table_yaratish.setFont(QFont("Times", 20))
        self.table_yaratish.setGeometry(30, 540, 440, 50)
        self.table_yaratish.setStyleSheet("""            
             QPushButton{ border-radius: 10px; 
            border : 2px solid red; }""")
        self.table_yaratish.clicked.connect(self.run_table)
# //!=========================================================

        self.kirish  = QPushButton("Amallar", self)
        self.kirish.setFont(QFont("Times", 20))
        self.kirish.setGeometry(30, 600, 440, 50)
        self.kirish.setStyleSheet("""            
             QPushButton{ border-radius: 10px; 
            border : 2px solid red; }""")    
        self.kirish.clicked.connect(self.run_malumot)

# //!=========================================================
    def  run_malumot(self):
        return  self.malomotlar()

    def  malomotlar(self):
        self.m  = Malumot_Amallar()
        self.m.show()

    def  run_table(self):
        return  self.table()

    def  table(self):
        self.m  = Asosiy()
        app.exec()
        self.close()
        self.m.show()

    
        
b = Boshqarish()
b.show()
app.exec_()
        
