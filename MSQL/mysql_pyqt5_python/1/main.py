import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import mysql.connector as myc

class project(QWidget):
    def __init__(self):
        super().__init__()
        self.setMaximumSize(1920,1080)
        self.setMinimumSize(1920,1080)
        self.setWindowTitle("Universitet")
        self.setFont(QFont("Calibri",18))
        self.setWindowIcon(QIcon("C:\\Users\\User\\Downloads\\tuit.ico"))
        
        self.nm = QLabel("Universitet nomini kiriting: ",self)
        self.nm.setGeometry(50,50,350,50)
        self.nm.setStyleSheet("color:  rgb(0,0,205)")
        
        self.name = QLineEdit(self)
        self.name.setGeometry(410,50,250,50)
        self.name.setStyleSheet("""color: rgb(0,0,255);
        background-color: rgb(253,245,230);
        border-color: rgb(0,255,0);
        border-radius: 15px;
        border-width: 3px;
        border-style: solid;""")
        self.name.setAlignment(Qt.AlignCenter)
        
        self.adres = QLabel("Adressni kiriting: ",self)
        self.adres.setGeometry(810,50,250,50)
        self.adres.setStyleSheet("color:  rgb(0,0,205)")
        
        self.adress = QLineEdit(self)
        self.adress.setGeometry(1070,50,250,50)
        self.adress.setStyleSheet("""color: rgb(0,0,255);
        background-color: rgb(253,245,230);
        border-color: rgb(0,255,0);
        border-radius: 15px;
        border-width: 3px;
        border-style: solid;""")
        self.adress.setAlignment(Qt.AlignCenter)
        
        self.tbc = QLabel("Talabalar sonini kiriting: ",self)
        self.tbc.setGeometry(50,110,350,50)
        self.tbc.setStyleSheet("color:  rgb(0,0,205)")
        
        self.count_t = QLineEdit(self)
        self.count_t.setGeometry(410,110,250,50)
        self.count_t.setStyleSheet("""color: rgb(0,0,255);
        background-color: rgb(253,245,230);
        border-color: rgb(0,255,0);
        border-radius: 15px;
        border-width: 3px;
        border-style: solid;""")
        self.count_t.setAlignment(Qt.AlignCenter)
        
        self.rkt = QLabel("Rektor F.I.SH: ",self)
        self.rkt.setGeometry(810,110,250,50)
        self.rkt.setStyleSheet("color:  rgb(0,0,205)")
        
        self.rektor = QLineEdit(self)
        self.rektor.setGeometry(1070,110,250,50)
        self.rektor.setStyleSheet("""color: rgb(0,0,255);
        background-color: rgb(253,245,230);
        border-color: rgb(0,255,0);
        border-radius: 15px;
        border-width: 3px;
        border-style: solid;""")
        self.rektor.setAlignment(Qt.AlignCenter)
        
        self.knt = QLabel("Kontrakt miqdorini kiriting: ",self)
        self.knt.setGeometry(50,170,350,50)
        self.knt.setStyleSheet("color:  rgb(0,0,205)")
        
        self.kontract = QLineEdit(self)
        self.kontract.setGeometry(410,170,250,50)
        self.kontract.setStyleSheet("""color: rgb(0,0,255);
        background-color: rgb(253,245,230);
        border-color: rgb(0,255,0);
        border-radius: 15px;
        border-width: 3px;
        border-style: solid;""")
        self.kontract.setAlignment(Qt.AlignCenter)
        
        self.typ = QLabel("Turini tanlang: ",self)
        self.typ.setGeometry(810,170,250,50)
        self.typ.setStyleSheet("color:  rgb(0,0,205)")
        
        self.xususiy = QRadioButton("Xususiy",self)
        self.xususiy.setGeometry(1070,170,250,50)
        self.xususiy.setStyleSheet("""color: rgb(0,0,255);
        background-color: rgb(253,245,230);
        border-color: rgb(0,255,0);
        border-radius: 15px;
        border-width: 3px;
        border-style: solid;""")
        
        self.davlat= QRadioButton("Davlat",self)
        self.davlat.setGeometry(1325,170,250,50)
        self.davlat.setStyleSheet("""color: rgb(0,0,255);
        background-color: rgb(253,245,230);
        border-color: rgb(0,255,0);
        border-radius: 15px;
        border-width: 3px;
        border-style: solid;""")
        
        self.add_data = QPushButton("Insert data",self)
        self.add_data.setGeometry(1600,230,300,50)
        self.add_data.setStyleSheet("""color: rgb(0,0,255);
        background-color: rgb(255,140,105);
        border-color: rgb(0,255,0);
        border-radius: 15px;
        border-width: 3px;
        border-style: solid;""")
        self.add_data.setFont(QFont("Poor Richard",24))
        self.add_data.clicked.connect(self.insert_data)

        self.upda_lb= QLabel("O'zgaradigan ustunni tanlang: ",self)
        self.upda_lb.setGeometry(50,670,400,50)
        self.upda_lb.setStyleSheet("color:  rgb(0,0,205)")
        
        self.cmb = QComboBox(self)
        self.cmb.setGeometry(460,670,300,50)
        self.cmb.addItems(["name","count_students","contract","type"])
        self.cmb.setStyleSheet("""color: rgb(0,0,255);
        background-color: rgb(253,245,230);
        border-color: rgb(0,255,0);
        border-radius: 15px;
        border-width: 3px;
        border-style: solid;""")
        
        self.nm1 = QLabel("O'zgaradigan Qiymatni kiriting: ",self)
        self.nm1.setGeometry(50,730,400,50)
        self.nm1.setStyleSheet("color:  rgb(0,0,205)")
        
        self.value = QLineEdit(self)
        self.value.setGeometry(460,730,250,50)
        self.value.setStyleSheet("""color: rgb(0,0,255);
        background-color: rgb(253,245,230);
        border-color: rgb(0,255,0);
        border-radius: 15px;
        border-width: 3px;
        border-style: solid;""")
        self.value.setAlignment(Qt.AlignCenter)
        
        self.nm2 = QLabel("Idni kiriting: ",self)
        self.nm2.setGeometry(850,670,250,50)
        self.nm2.setStyleSheet("color:  rgb(0,0,205)")
        
        self.value_id = QLineEdit(self)
        self.value_id.setGeometry(1110,670,250,50)
        self.value_id.setStyleSheet("""color: rgb(0,0,255);
        background-color: rgb(253,245,230);
        border-color: rgb(0,255,0);
        border-radius: 15px;
        border-width: 3px;
        border-style: solid;""")
        self.value_id.setAlignment(Qt.AlignCenter)
        
        self.update = QPushButton("Update data",self)
        self.update.setGeometry(1110,730,250,50)
        self.update.setStyleSheet("""color: rgb(0,0,255);
        background-color: rgb(255,203,164);
        border-color: rgb(0,255,0);
        border-radius: 15px;
        border-width: 3px;
        border-style: solid;""")
        self.update.setFont(QFont("Poor Richard",24))
        self.update.clicked.connect(self.update_data)
        
        self.table = QTableWidget(self)
        self.table.move(30,400)
        self.table.setVisible(False)
        
    def add_base(self,database ='Universitet'):
        con = myc.connect(user = 'root',password= 'root1',host = 'localhost')
        kursor = con.cursor()
        kursor.execute(f"Create database if not exists {database};")
    
    
    def add_table(self,database='Universitet',table="univer"):
        con = myc.connect(user = 'root',password= 'root1',host = 'localhost',database =f"{database}")
        kursor = con.cursor()
        kursor.execute(f"""Create table if not exists {table} 
                       (id int primary key auto_increment,
                       name varchar(30),
                       adress varchar(30),
                       count_students int,
                       rector varchar(40),
                       contract int,
                       type bool);
                       """)
    def insert_data(self):
        self.add_base()
        self.add_table()
        con = myc.connect(user = 'root',password= 'root1',host = 'localhost',database ='universitet')
        kursor = con.cursor()
        sql = "Insert into univer(name,adress,count_students,rector,contract,type) Values (%s,%s,%s,%s,%s,%s);"
        name = self.name.text()
        adress = self.adress.text()
        tb_soni = int(self.count_t.text())
        rector = self.rektor.text()
        contract = int(self.kontract.text())
        typ = self.xususiy.isChecked()
        Value = (name,adress,tb_soni,rector,contract,typ)
        kursor.execute(sql,Value)
        con.commit()
        os.system("cls")
        print("Bazaga ma'lumot qo'shildi")
        self.show_data()

        
    def show_data(self):
        self.table.setVisible(True)
        con = myc.connect(user = 'root',password= 'root1',host = 'localhost',database ='universitet')
        kursor = con.cursor()
        kursor.execute("Select * from univer")
        res =kursor.fetchall()
        col_count = 7
        row_count = len(res)
        self.table.setRowCount(row_count)
        self.table.setColumnCount(col_count)
        self.table.setHorizontalHeaderLabels(["ID:","Name","Adress","Count students","Rector","Contract","Type Universitet"])
        self.table.setFont(QFont("Calibri",18))
        self.table.resize(1600,200)
        st = ","*row_count
        ls = st.split(",")
        self.table.setVerticalHeaderLabels(ls)
        header = self.table.horizontalHeader()
        for x in range(7):
            header.setSectionResizeMode(x,QHeaderView.ResizeToContents)
        sch = 0
        for x in res:
            cl = 0
            self.table.setItem(sch,0,QTableWidgetItem(str(x[0])))
            self.table.setItem(sch,1,QTableWidgetItem(x[1]))
            self.table.setItem(sch,2,QTableWidgetItem(x[2]))
            self.table.setItem(sch,3,QTableWidgetItem(str(x[3])))
            self.table.setItem(sch,4,QTableWidgetItem(x[4]))
            self.table.setItem(sch,5,QTableWidgetItem(str(x[5])))
            if x[6] == True:
                self.table.setItem(sch,6,QTableWidgetItem("Private"))
            else:
                self.table.setItem(sch,6,QTableWidgetItem("Community"))
            sch += 1
            
    def update_data(self):
        con = myc.connect(user = 'root',password= 'root1',host = 'localhost',database ='universitet')
        kursor = con.cursor()
        if self.cmb.currentText() == "type":
            if self.value.text() == "False":
                res =False
            else:
                res =True
            kursor.execute(f"""Update univer set {self.cmb.currentText()} = {res} where id = {int(self.value_id.text())}""")
        else:
            kursor.execute(f"""Update univer set {self.cmb.currentText()} = "{self.value.text()}" where id = {int(self.value_id.text())}""")
        con.commit()
        self.show_data()
            
            
            
            
            
            
        
        
        
        
       
       
        
             
app = QApplication(sys.argv)
ilova = project()
ilova.show()
sys.exit(app.exec_())