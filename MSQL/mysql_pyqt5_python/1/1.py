from PyQt5.QtCore import Qt
from PyQt5.QtWidgets  import  QApplication ,  QWidget,  QPushButton
from PyQt5.QtWidgets  import  QLineEdit, QLabel,    QTableWidget, QTableWidgetItem
from  PyQt5.QtGui  import  QFont
import  mysql.connector  ,  sys, os
os.system("cls")
app  =  QApplication([])

class  Dokon(QWidget):
    def __init__(self):
        super().__init__()
        # !===================================
        self.mydb =  mysql.connector.connect(
            host =  "localhost",
            user  = "root",
            password = "root1"
        )
        self.kursor  = self.mydb.cursor()
        # !===================================
        self.setWindowTitle("Dokon  Loyixasi")
        self.setFixedSize(550,  850)
        self.create_database()
        self.start()
        self.show()
 # TODO   Razmer uchun  yaratilgan  funksiya
    def  Ozimizni_font(self,  ob,  x,  y, size):
        ob.setFont(QFont("Times", size))
        ob.move(x,  y)

    def  start(self):
# !==========maxsulot_ID_input ==========================
        self.id  =  QLabel("Id", self)
        self.Ozimizni_font(self.id,  30, 50, 15)

        self.maxsulot_ID_input  = QLineEdit(self)
        self.maxsulot_ID_input.setStyleSheet("""            
            QLineEdit { border-radius: 5px; 
            border : 2px solid yellow; }""")
        self.maxsulot_ID_input.setPlaceholderText("Id  ")
        self.Ozimizni_font(self.maxsulot_ID_input, 150, 50,15)

# !==========maxsulot_Nomi_input ==========================
        self.m_nomi =  QLabel("Max nomi", self)
        self.Ozimizni_font(self.m_nomi,  30, 110, 15)

        self.maxsulot_Nomi_input  = QLineEdit(self)
        self.maxsulot_Nomi_input.setStyleSheet("""
            QLineEdit { border-radius: 5px; 
            border : 2px solid red; }""")
        self.maxsulot_Nomi_input.setPlaceholderText("Nomi  ")
        self.Ozimizni_font(self.maxsulot_Nomi_input, 150, 110,15)

# !==========maxsulot_Narx_input ==========================
        self.m_narxi  =  QLabel("Max narxi", self)
        self.Ozimizni_font(self.m_narxi,  30, 170, 15)

        self.maxsulot_Narx_input  = QLineEdit(self)
        self.maxsulot_Narx_input.setStyleSheet("""
            QLineEdit{ border-radius: 5px; 
        border : 2px solid red; }""")
        self.maxsulot_Narx_input.setPlaceholderText("Narx  ")
        self.Ozimizni_font(self.maxsulot_Narx_input, 150, 170,15)

# //! /================   Qo'shish  ===============
        self.maxsulot_qoshish_db =  QPushButton("qo'shish", self)
        self.maxsulot_qoshish_db.setGeometry(50,  220,  450, 40)
        self.maxsulot_qoshish_db.setFont(QFont("Times",  18))   
        self.maxsulot_qoshish_db.clicked.connect(self.qoshish)







# //!=====================TABLE  NOMI  ==========================================
        txt  = "Bitinchi  navbatda  Table  nomi"
        self.table_t  =  QLabel(txt, self)
        self.Ozimizni_font(self.table_t,  30, 270, 15)

        self.table  =  QLabel("Table  Nomi  ", self)
        self.Ozimizni_font(self.table,  30, 320, 15)

        self.table_nomi  = QLineEdit(self)
        self.table_nomi.setStyleSheet("""
            QLineEdit{ border-radius: 5px; 
        border : 2px solid red; }""")
        self.table_nomi.setPlaceholderText("Table  Nomini  ")
        self.Ozimizni_font(self.table_nomi, 150, 320,15)

# //!==============  Table  yaratadigan yoki  tablega   kiradigan ==================
        self.table_start =  QPushButton("Table", self)
        self.Ozimizni_font(self.table_start,  390, 320,  15  ) 
        self.table_start.clicked.connect(self.create_TABLE)





        self.qidiruv_input  = QLineEdit(self)
        self.qidiruv_input.setStyleSheet("""
            QLineEdit{ border-radius: 5px; 
        border : 2px solid red; }""")
        self.qidiruv_input.setPlaceholderText("Qiriruv  ")
        self.Ozimizni_font(self.qidiruv_input, 30, 370,15)


        self.qidiruv =  QPushButton("Malumotlar", self)
        self.Ozimizni_font(self.qidiruv,  390, 370,  15  ) 
        self.qidiruv.clicked.connect(self.serch_maxsulot)

# !/!=======================================================

        self.malumot =  QPushButton("Malumotlar", self)
        self.malumot.setGeometry(50,  460,  300, 30)
        self.malumot.setFont(QFont("Times",  18))
        self.malumot.clicked.connect(self.info)
        
        self.jadval = QTableWidget(self) 
        self.jadval.setGeometry(20, 490,  300,  300)
        self.jadval.setFont(QFont("Times",  18))
        self.jadval.setVisible(False)

        
        self.qidiruv_malumot  =  QLabel("", self)
        self.Ozimizni_font(self.qidiruv_malumot,  30, 410, 15)
# //!=======================================================================================
    def  create_database(self):
        sql  ="""CREATE  DATABASE  IF  NOT  EXISTS  DOKON """
        self.kursor.execute(sql)
        self.kursor.execute("USE  Dokon")

    def  create_TABLE(self):
        if  (self.table_nomi.text()  != ""):
            t  =  self.table_nomi.text()
            self.kursor.execute(F"""CREATE  TABLE  IF  NOT  EXISTS   {t} 
                                (id Int, Nomi Text,  narx Float)""")
            self.table_t.setText("Table  Yaratili  👌👍✅")
            self.table_t.setStyleSheet('color: green')
            self.table_t.adjustSize()

        else: 
            matn = "Tableni Kiriting.  "
            self.table_t.setText(matn)
            self.table_t.setStyleSheet('color: red')
            self.table_t.adjustSize()

    def  qoshish(self):
        m_id_db  = int(self.maxsulot_ID_input.text())
        m_nomi_db =  self.maxsulot_Nomi_input.text()
        m_narxi_db = float(self.maxsulot_Narx_input.text()) 
        qosh_table_db  = self.table_nomi.text() 
        self.kursor.execute(F"""
            INSERT  INTO  {qosh_table_db} VALUES (%s,  %s, %s) 
            """,  (m_id_db, m_nomi_db,  m_narxi_db))
        self.mydb.commit()
        self.maxsulot_ID_input.clear()
        self.maxsulot_Nomi_input.clear()
        self.maxsulot_Narx_input.clear()

    def  info(self):
        self.jadval.setVisible(True)
        malumot_info    =   self.table_nomi.text()
        self.kursor.execute(f"SELECT  *FROM  {malumot_info}")
        ls  =  self.kursor.fetchall()

        self.jadval.setRowCount(len(ls))
        self.jadval.setColumnCount(len(["id",  "nomi",  "narxi"]))  
        self.jadval.setHorizontalHeaderLabels(["id",  "nomi",  "narxi"])

        for  i in  range(len(ls)):
            self.jadval.setItem(i,0,QTableWidgetItem(str(ls[i][0])))
            self.jadval.setItem(i,1,QTableWidgetItem(str(ls[i][1])))
            self.jadval.setItem(i,2,QTableWidgetItem(str(ls[i][2])))


    def  serch_maxsulot(self):

        serch_table  =  self.table_nomi.text()
        s_id  =  int(self.qidiruv_input.text())
        self.kursor.execute(f"Select  *from  {serch_table}  where id  =  {s_id}")
        t  = self.kursor.fetchall()
        self.qidiruv_malumot.setText(f'{t}')
        self.qidiruv_malumot.adjustSize()
        print(t)

market =  Dokon()
app.exec_()
