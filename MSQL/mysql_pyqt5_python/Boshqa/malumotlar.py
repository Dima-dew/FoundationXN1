from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import  mysql.connector

class Malumot_Amallar(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800,  800)
        self.setWindowTitle("Malumot Qo'shish")
        # !===================================
        self.mydb =  mysql.connector.connect(
            host =  "localhost",  user  = "root",password = "root1" )
        self.kursor  = self.mydb.cursor()
        self.table_ls = []
        self.start()
        self.Info_TABLE()

    def  Ozimizni_font(self,  ob,  x,  y, size):
        ob.setFont(QFont("Times", size))
        ob.move(x,  y)       

    def  start(self):

# //! ===========  Database  ga  ulanish, kirish va chiqish   qismi  ============
        self.mydb =  mysql.connector.connect(
            host =  "localhost",
            user  = "root",
            password = "root1"
        )
        kursor  = self.mydb.cursor()
        kursor.execute("CREATE  DATABASE  IF  NOT  EXISTS  DOKON")
        kursor.execute("USE  Dokon")
        kursor.close()

# //!  =============  Qidiruv  uchun   ==========================
        self.search  =  QLineEdit(self)
        self.search.setFont(QFont("Times", 15))
        self.search.setGeometry(30, 270, 320, 40)
        self.search.setPlaceholderText("Search 🔎   ")
        self.search.setStyleSheet("""            
            QLineEdit { border-radius: 10px; 
            border : 2px solid red; }""")

# !  ================  Table  malumotlarini  ko'rish  uchun  botton ===============
        
        self.malumot_korish = QPushButton("Table Malumoti Ko'rish", self)
        self.malumot_korish.setFont(QFont("Times", 20))
        self.malumot_korish.setGeometry(300, 190, 440, 50)
        self.malumot_korish.setStyleSheet("""            
             QPushButton{ border-radius: 10px; 
            border : 2px solid red; }""")
        self.malumot_korish.clicked.connect(self.table_malumotlar)

# //!-===================  Qidirish  uchun  botton ========================

        self.qidirish = QPushButton("Qidirish", self)
        self.qidirish.setFont(QFont("Times", 20))
        self.qidirish.setGeometry(420, 270, 319, 40)
        self.qidirish.setStyleSheet("""            
             QPushButton{ border-radius: 10px; 
            border : 2px solid red; }""")
        self.qidirish.clicked.connect(self.search_maxsulot)
        
# //!=============  Tabllar  uchun  Jadval  ========================
        self.jadval = QTableWidget(self) 
        self.jadval.setGeometry(30, 50,  230, 190)
        self.jadval.setFont(QFont("Times",  18))
        self.jadval.setColumnCount(1)  
        self.jadval.setHorizontalHeaderLabels(["TABLE NOMI"])
        self.jadval.setColumnWidth(0,212)
        self.jadval.adjustSize()

        self.jadval.horizontalHeader().setStyleSheet("""
        QHeaderView::section {
        background-color: lightgray;  
        color: black;   border: 1px solid black;   } """)
        
# ! ===========  Table  Ichidagi malumotlar  uchun  jadval ====================
        self.malumot_jadval = QTableWidget(self) 
        self.malumot_jadval.setGeometry(30, 520, 740, 200)
        self.malumot_jadval.setFont(QFont("Times",  18))
        self.malumot_jadval.setVisible(False)
        self.malumot_jadval.setColumnCount(len(["Id",  "Nomi",  "Narxi"]))  
        self.malumot_jadval.setHorizontalHeaderLabels(["Id",  "Nomi",  "Narxi"])
        self.malumot_jadval.horizontalHeader().setStyleSheet("""
        QHeaderView::section {
        background-color: lightgray;  
        color: black;   border: 1px solid black;   } """)

# //!============  Qidirgan  malumot  chiqmasa   yozuv chiqishi  uchun =====================
        self.topilmadi  =  QLabel("", self)
        self.Ozimizni_font(self.topilmadi,  30, 520, 25)


    def Info_TABLE(self):
        kursor  =  self.mydb.cursor()
        kursor.execute("SHOW  TABLES;")
        l  =  kursor.fetchall()
        for  i in  l:
            self.table_ls.append(str(i[0]))
# //! ================  Tanlangan  Tanlash  uchun  ========================
        self.combo =  QComboBox(self)
        self.combo.addItems(self.table_ls)
        self.combo.setFont(QFont("Times",  20))
        self.combo.setGeometry(300, 50, 300, 40)
        self.combo.setStyleSheet("""            
            QComboBox { border-radius: 10px; 
            border : 2px solid red; }""")
# //!==============    Tabllarni  ekranga  chiqaradigan jadval  =================
        self.jadval.setRowCount(len(l))
        for  i in  range(len(l)):
            self.jadval.setItem(i,0,QTableWidgetItem(str(l[i][0])))
        kursor.close()


# //! ========Tanlangan  Table  haqida  malumotlarni  barchasini  chiqaradi==============
    def  table_malumotlar(self):
        kursor  = self.mydb.cursor()
        self.malumot_jadval.setVisible(True)
        malumot_info    =   self.combo.currentText()
        kursor.execute(f"SELECT  *FROM  {malumot_info}")
        ls  =  kursor.fetchall()
        self.malumot_jadval.setRowCount(len(ls))
        for  i in  range(len(ls)):
            self.malumot_jadval.setColumnWidth(i, 238)
            self.malumot_jadval.setItem(i,0,QTableWidgetItem(str(ls[i][0])))
            self.malumot_jadval.setItem(i,1,QTableWidgetItem(str(ls[i][1])))
            self.malumot_jadval.setItem(i,2,QTableWidgetItem(str(ls[i][2])))
        kursor.close()
# !  =========  Tanlangan  Table  ichidan  qidirilayotgan  malumot ==========
    def  search_maxsulot(self):
        kursor  = self.mydb.cursor()
        serch_table  =  self.combo.currentText()
        s_id  =  int(self.search.text())
        kursor.execute(f"Select  *from  {serch_table}  where id  =  {s_id}")
        t  = kursor.fetchall()
# //! Qidirilganda  Malumot  chiqmasa  Bunday malumot  yo'q  deb  chiqarish  qismi  
        if  list(t)  == []:
            self.malumot_jadval.clear()
            self.topilmadi.setText("Bunday Malumot  Topilmadi")
            self.topilmadi.setStyleSheet('color: red')
            self.topilmadi.adjustSize()
# !  ===========  Qidirilgan malumot  bo'lsa  ekranga  jadval  ko'rinishida  chiqarish ==========
        else :
            self.topilmadi.clear()
            self.malumot_jadval.setVisible(True)
            self.malumot_jadval.clear()
            self.malumot_jadval.setRowCount(len(t))
            for  i in  range(len(t)):
                self.malumot_jadval.setColumnWidth(i, 238)
                self.malumot_jadval.setItem(i,0,QTableWidgetItem(str(t[i][0])))
                self.malumot_jadval.setItem(i,1,QTableWidgetItem(str(t[i][1])))
                self.malumot_jadval.setItem(i,2,QTableWidgetItem(str(t[i][2])))
        kursor.close()

