
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget,  QApplication,  QLineEdit,  QPushButton
from PyQt5.QtWidgets import QLabel ,  QTableWidgetItem,  QTableWidget
import  mysql.connector
from  malumotlar  import  Malumot_Amallar
import  os; os.system("cls")




app = QApplication([])
class Asosiy(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(900,  580)
        self.setWindowTitle("Dokon  Loyixasi")
        #!========================================
        self.mydb =  mysql.connector.connect(
            host =  "localhost",  user  = "root",password = "root1" )
        kursor  = self.mydb.cursor()
        self.table_ls = []
        self.create_DATABES()
        self.start()
        self.Info_TABLE()


    def  Ozimizni_font(self,  ob,  x,  y, size):
        ob.setFont(QFont("Times", size))
        ob.move(x,  y)

    def  start(self):   
        self.tekshir  =  QLabel("", self)
        self.Ozimizni_font(self.tekshir,  30, 5, 15)

        self.table_nomi  =  QLineEdit(self)
        self.table_nomi.setFont(QFont("Times", 20))
        self.table_nomi.setGeometry(30, 30, 340, 40)
        self.table_nomi.setPlaceholderText("Yangi  table  nomi ")
        self.table_nomi.setStyleSheet("""            
            QLineEdit { border-radius: 10px; 
            border : 2px solid red; }""")
# //!=========================================================

        self.table_yaratish = QPushButton("Yaratish", self)
        self.table_yaratish.setFont(QFont("Times", 20))
        self.table_yaratish.setGeometry(30, 320, 340, 40)
        self.table_yaratish.setStyleSheet("""            
             QPushButton{ border-radius: 10px; 
            border : 2px solid red; }""")
        self.table_yaratish.clicked.connect(self.create_TABLE)
# //!=========================================================

        self.jadval = QTableWidget(self) 
        self.jadval.setGeometry(30, 90,  340, 200)
        self.jadval.setFont(QFont("Times",  18))

        self.tekshir  =  QLabel("Qayi  tablega malumot  qo'shasiz ?", self)
        self.Ozimizni_font(self.tekshir,  30, 389, 12)
# //!===================MAXSULOT  QO'SHISH ====================
    

        self.Id_input  =  QLineEdit(self)
        self.Id_input.setFont(QFont("Times", 20))
        self.Id_input.setGeometry(430, 40, 340, 40)
        self.Id_input.setPlaceholderText("Maxsulot  id ")
        self.Id_input.setStyleSheet("""            
            QLineEdit { border-radius: 10px; 
            border : 3px solid BLUE; }""")


        self.nomi_input  =  QLineEdit(self)
        self.nomi_input.setFont(QFont("Times", 20))
        self.nomi_input.setGeometry(430, 90, 340, 40)
        self.nomi_input.setPlaceholderText("Maxsulot nomi ")
        self.nomi_input.setStyleSheet("""            
            QLineEdit { border-radius: 10px; 
            border : 3px solid BLUE; }""")

        self.narx_input  =  QLineEdit(self)
        self.narx_input.setFont(QFont("Times", 20))
        self.narx_input.setGeometry(430, 150, 340, 40)
        self.narx_input.setPlaceholderText("Maxsulot narxi ")
        self.narx_input.setStyleSheet("""            
            QLineEdit { border-radius: 10px; 
            border : 3px solid BLUE; }""")
        
        # self.narx_input  =  QLineEdit(self)
        # self.narx_input.setFont(QFont("Times", 20))
        # self.narx_input.setGeometry(430, 150, 340, 40)
        # self.narx_input.setPlaceholderText("Maxsulot narxi ")
        # self.narx_input.setStyleSheet("""            
        #     QLineEdit { border-radius: 10px; 
        #     border : 3px solid BLUE; }""")
        

        self.malumot_qoshish = QPushButton("Insert Into", self)
        self.malumot_qoshish.setFont(QFont("Times", 20))
        self.malumot_qoshish.setGeometry(430, 320, 340, 40)
        self.malumot_qoshish.setStyleSheet("""            
             QPushButton{ border-radius: 10px; 
            border : 2px solid red; }""")
        self.malumot_qoshish.clicked.connect(self.Insert_Into)
        

        self.TANLOV_TABLE  =  QLineEdit(self)
        self.TANLOV_TABLE.setFont(QFont("Times", 20))
        self.TANLOV_TABLE.setGeometry(30, 430, 340, 50)
        self.TANLOV_TABLE.setPlaceholderText("TABLNI  TANLANG")
        self.TANLOV_TABLE.setStyleSheet("QLineEdit{ "
               "background-color:green;"
                "border: 3px solid BLUE;"
                "border-radius: 10px;"
                "font-size: 16px;}" )
        
        self.amallar = QPushButton("Ma'lumotlar", self)
        self.amallar.setFont(QFont("Times", 20))
        self.amallar.setGeometry(430, 380, 340, 40)
        self.amallar.setStyleSheet("""            
             QPushButton{ border-radius: 10px; 
            border : 2px solid red; }""")
        self.amallar.clicked.connect(self.run_amallar)
        
    def create_DATABES(self):
        kursor  = self.mydb.cursor()
        kursor.execute("CREATE  DATABASE  IF  NOT  EXISTS  DOKON")
        kursor.execute("USE  Dokon")
        kursor.close()

    def create_TABLE(self):
            kursor  = self.mydb.cursor() 
            if self.table_nomi.text() != "":
               t = self.table_nomi.text()
               kursor.execute(f"CREATE TABLE IF NOT EXISTS {t} (id Int, Nomi Text, narx Float)")
               self.tekshir.setText("Table yaratildi 👍✅✅✅")
               self.tekshir.setStyleSheet('color: green')
               self.tekshir.adjustSize()
               self.table_nomi.clear()
            else:
               self.tekshir.setText("Tableni kiriting.")
               self.tekshir.setStyleSheet('color: red')
               self.tekshir.adjustSize()
            kursor.close()
            self.Info_TABLE()
        
    def Info_TABLE(self):
        kursor = self.mydb.cursor()
        kursor.execute("SHOW TABLES;")
        l = kursor.fetchall()

        # Jadvalni yangilash
        self.table_ls.clear()
        self.jadval.clearContents()

        for i in l:
            self.table_ls.append(str(i[0]))
        
        self.jadval.setRowCount(len(l))
        self.jadval.setColumnCount(1)
        self.jadval.setHorizontalHeaderLabels(["TABLE NOMI"])
        self.jadval.setColumnWidth(0, 250)

        # Ustun sarlavhasining fon rangini sozlash
        self.jadval.horizontalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: lightblue;  
                color: black;   
                border: 1px solid black; 
                font-weight: bold;
            }""")
        for i in range(len(l)):
            self.jadval.setItem(i, 0, QTableWidgetItem(str(l[i][0])))
        kursor.close()

    def Insert_Into(self):
        kursor  = self.mydb.cursor()
        t  = self.TANLOV_TABLE.text()
        id_db = int(self.Id_input.text())
        nomi_db = self.nomi_input.text()
        narxi_db =  float(self.narx_input.text())
        kursor.execute(f"INSERT  INTO  {t} values (%s, %s,  %s)",  
                       (id_db,  nomi_db,  narxi_db))
        self.mydb.commit()
        kursor.close()
        self.Id_input.clear()
        self.nomi_input.clear()
        self.narx_input.clear()

    def  run_amallar(self):
        return  self.malumot()
    
    def  malumot(self):
        self.amal  = Malumot_Amallar()
        self.amal.show()

# a  = Asosiy()
# a.show()
# app.exec_()
    


















