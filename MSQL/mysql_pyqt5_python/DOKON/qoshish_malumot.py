from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import  mysql.connector

class Malumot_Qoshish(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500,  800)
        self.setWindowTitle("Malumot Qo'shish")
        # !===================================
        self.mydb =  mysql.connector.connect(
            host =  "localhost",
            user  = "root",
            password = "root1"
        )
        self.kursor  = self.mydb.cursor()
        self.uzatilgan_table_nomi = ""
        # !===================================
        self.create_DATABES()
        self.start()

    def  Ozimizni_font(self,  ob,  x,  y, size):
        ob.setFont(QFont("Times", size))
        ob.move(x,  y)       

    def  start(self):
        self.tekshir  =  QLabel("", self)
        self.Ozimizni_font(self.tekshir,  30, 370, 20)
        
        self.malumot_korish = QPushButton("Table Malumoti Ko'rish", self)
        self.malumot_korish.setFont(QFont("Times", 20))
        self.malumot_korish.setGeometry(30, 700, 440, 50)
        self.malumot_korish.setStyleSheet("""            
             QPushButton{ border-radius: 10px; 
            border : 2px solid red; }""")
# //!==================================================================

    def  create_DATABES(self):
        self.kursor.execute("CREATE  DATABASE  IF  NOT  EXISTS  DOKON")
        self.kursor.execute("USE  Dokon")
