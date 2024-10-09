
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget,  QApplication,  QLineEdit,  QPushButton
from PyQt5.QtWidgets import QLabel, QComboBox ,  QTableWidgetItem,  QTableWidget
import  mysql.connector
import  os; os.system("cls")

from  tablega_malumot import Main
from  qoshish_malumot import Malumot_Qoshish


app = QApplication([])
class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500,  800)
        self.setWindowTitle("Dokon  Loyixasi")
        #!========================================
        self.mydb =  mysql.connector.connect(
            host =  "localhost",
            user  = "root",
            password = "root1"
        )
        self.kursor  = self.mydb.cursor()
        self.table_ls = []
        # !===================================
        self.create_DATABES()
        self.start()
        self.malumot_TABLE()
    def  Ozimizni_font(self,  ob,  x,  y, size):
        ob.setFont(QFont("Times", size))
        ob.move(x,  y)

# //!=========================================================

    def  start(self):   

        self.tekshir  =  QLabel("", self)
        self.Ozimizni_font(self.tekshir,  30, 70, 15)
    
        self.table_nomi  =  QLineEdit(self)
        self.table_nomi.setFont(QFont("Times", 20))
        self.table_nomi.setGeometry(30, 100, 440, 50)
        self.table_nomi.setPlaceholderText("Yangi  table  nomi ")
        self.table_nomi.setStyleSheet("""            
            QLineEdit { border-radius: 10px; 
            border : 2px solid red; }""")
        
# //!=========================================================

        self.table_yaratish = QPushButton("Yaratish", self)
        self.table_yaratish.setFont(QFont("Times", 20))
        self.table_yaratish.setGeometry(30, 540, 440, 50)
        self.table_yaratish.setStyleSheet("""            
             QPushButton{ border-radius: 10px; 
            border : 2px solid red; }""")
        # self.table_yaratish.clicked.connect(self.create_TABLE)
# //!=========================================================

        self.kirish  = QPushButton("Kirish", self)
        self.kirish.setFont(QFont("Times", 20))
        self.kirish.setGeometry(30, 600, 440, 50)
        self.kirish.setStyleSheet("""            
             QPushButton{ border-radius: 10px; 
            border : 2px solid red; }""")    
        # self.kirish.clicked.connect(self.boshqarish )
# //!=========================================================

        self.malumot_qosh = QPushButton("Malumot  Qo'shish", self)
        self.malumot_qosh.setFont(QFont("Times", 20))
        self.malumot_qosh.setGeometry(30, 660, 440, 50)
        self.malumot_qosh.setStyleSheet("""            
             QPushButton{ border-radius: 10px; 
            border : 2px solid red; }""")
        self.malumot_qosh.clicked.connect(self.tablega_malumot_qosh)
# !====================================================================
        self.jadval = QTableWidget(self) 
        self.jadval.setGeometry(30, 170,  440, 200)
        self.jadval.setFont(QFont("Times",  18))
        # self.jadval.setVisible(False)

# //!=========================================================
 

    def  create_DATABES(self):
        self.kursor.execute("CREATE  DATABASE  IF  NOT  EXISTS  DOKON")
        self.kursor.execute("USE  Dokon")
    
    def  create_TABLE(self):
        try:
           if self.table_nomi.text() != "":
               t = self.table_nomi.text()
               self.kursor.execute(f"CREATE TABLE IF NOT EXISTS {t} (id Int, Nomi Text, narx Float)")
               self.tekshir.setText("Table yaratildi 👍✅✅✅")
               self.tekshir.setStyleSheet('color: green')
               self.tekshir.adjustSize()
               self.kursor.execute("SHOW TABLES;")
               t = self.kursor.fetchall()
               print(t)
               self.malumot_TABLE()
           else:
               self.tekshir.setText("Tableni kiriting.")
               self.tekshir.setStyleSheet('color: red')
               self.tekshir.adjustSize()
        except mysql.connector.Error as err:
            self.tekshir.setText(f"MySQL xatosi: {err}")
            self.tekshir.setStyleSheet('color: red')
            self.tekshir.adjustSize()

    def boshqarish(self):
        return self.otish()

    def otish(self):
        self.main = Main()
        self.close()
        self.main.show()
    
    def tablega_malumot_qosh(self):
        return   self.malumot_qosh_otish()
    
    def  malumot_qosh_otish(self):
        self.m =  Malumot_Qoshish()
        self.m.show()
        
    def malumot_TABLE(self):
        self.kursor.execute("SHOW  TABLES;")
        l  =  self.kursor.fetchall()
        for  i in  l:
            self.table_ls.append(str(i[0]))
        
        # self.combo =  QComboBox(self)
        # self.combo.addItems(self.table_ls)
        # self.combo.setFont(QFont("Times",  20))
        # self.combo.setGeometry(30,  460,  440,  50)

        self.jadval.setRowCount(len(l))
        self.jadval.setColumnCount(1)  
        self.jadval.setHorizontalHeaderLabels(["NOMI"])
        for  i in  range(len(l)):
            self.jadval.setItem(i,0,QTableWidgetItem(str(l[i][0])))

    
login = Login()
login.show()

app.exec_()
        


















        #         self.jadval = QTableWidget(self) 
        # self.jadval.setGeometry(30, 30,  440, 200)
        # self.jadval.setFont(QFont("Times",  18))
        # # self.jadval.setVisible(False)


        # def malumot_TABLE(self):
        # self.jadval.setVisible(True)
        # self.kursor.execute("SHOW  TABLES;")
        # l  =  self.kursor.fetchall()
        # for  i in  l:
        #     self.table_ls.append(str(i[0]))
        
        # self.combo =  QComboBox(self)
        # self.combo.addItems(self.table_ls)
        # self.combo.setFont(QFont("Times",  20))
        # self.combo.setGeometry(30,  260,  440,  50)

        # self.jadval.setRowCount(len(l))
        # self.jadval.setColumnCount(1)  
        # self.jadval.setHorizontalHeaderLabels(["NOMI"])
        # for  i in  range(len(l)):
        #     self.jadval.setItem(i,0,QTableWidgetItem(str(l[i][0])))
