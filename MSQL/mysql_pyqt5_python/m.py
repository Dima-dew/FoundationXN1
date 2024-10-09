from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QRadioButton, QComboBox, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QFont
import sys, mysql.connector, os

os.system("cls")
app = QApplication([])

class Database(QWidget):
    def __init__(self):
        super().__init__()
        self.db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root1"
        )
        self.kursor = self.db.cursor()
        self.setWindowTitle("Malumotlar")
        self.setGeometry(100, 50, 1000, 600)

        self.jadval = QTableWidget(self)
        self.jadval.setGeometry(50, 200, 900, 200 )
        self.jadval.setFont(QFont("Times", 16))
        self.jadval.setVisible(False)

        # !nom
        self.nom_error = QLabel("", self)
        self.UzFont(self.nom_error, 180, 30, 8)
        self.nom_error.setStyleSheet("color: red")
        # !talaba
        self.t_soni_error1 = QLabel("", self)
        self.UzFont(self.t_soni_error1, 180, 80, 8)
        self.t_soni_error1.setStyleSheet("color: red")
        # !oylik
        self.oylik_error = QLabel("", self)
        self.UzFont(self.oylik_error, 180, 130, 8)
        self.oylik_error.setStyleSheet("color: red")
        # !manzil
        self.manzil_error = QLabel("", self)
        self.UzFont(self.manzil_error, 530, 30, 8)
        self.manzil_error.setStyleSheet("color: red")
        # ! ustozning ismi
        self.t_name_error = QLabel("", self)
        self.UzFont(self.t_name_error, 530, 80, 8)
        self.t_name_error.setStyleSheet("color: red")
        # !turi
        self.turi_error = QLabel("", self)
        self.UzFont(self.turi_error, 450, 130, 8)
        self.turi_error.setStyleSheet("color: red")    
            
        self.database()
        self.start()
        self.Update()
        
        self.show()
                    
    def start(self):
        # ! === Guruh nomi va line ===
        self.guruh_nomi = QLabel("Guruh nomi:", self)
        self.UzFont(self.guruh_nomi, 50, 50, 12)
        self.guruh_nomi_inp = QLineEdit(self)
        self.UzFont(self.guruh_nomi_inp, 180, 50, 11)        
        self.guruh_nomi_inp.setPlaceholderText("guruh nomini kiriting")
        self.guruh_nomi_inp.setStyleSheet("QLineEdit  {background-color: yellow; border-radius: 5px; border: 2px solid blue; }")
        
        # ! === Talabalar soni ===
        self.talaba_soni = QLabel("Talabalar soni:", self)
        self.UzFont(self.talaba_soni, 50, 100, 12)
        self.talaba_soni_inp = QLineEdit(self)
        self.UzFont(self.talaba_soni_inp, 180, 100, 11)
        self.talaba_soni_inp.setPlaceholderText("talaba sonini kiriting")
        self.talaba_soni_inp.setStyleSheet("QLineEdit  {background-color: yellow; border-radius: 5px; border: 2px solid blue; }")
        
        # ! === oylik tolov ===
        self.oylik = QLabel("Oylik to`lov:", self)
        self.UzFont(self.oylik, 50, 150, 12)
        self.oylik_inp = QLineEdit(self)
        self.UzFont(self.oylik_inp, 180, 150, 11)
        self.oylik_inp.setPlaceholderText("oylik tolovni kiriting")
        self.oylik_inp.setStyleSheet("QLineEdit  {background-color: yellow; border-radius: 5px; border: 2px solid blue; }")
        
        # ! === Manzil ===
        self.manzil = QLabel("Manzil:", self)
        self.UzFont(self.manzil, 400, 50, 12)
        self.manzil_inp = QLineEdit(self)
        self.manzil_inp.setGeometry(530, 50, 300, 27)
        self.manzil_inp.setPlaceholderText("manzilni kiriting")
        self.manzil_inp.setStyleSheet("QLineEdit  {background-color: yellow; border-radius: 5px; border: 2px solid blue; }")
        
        # ! === Ustoz ismi ===
        self.name = QLabel("Ustozning ismi:", self)
        self.UzFont(self.name, 400, 100, 12)
        self.name_inp = QLineEdit(self)
        self.UzFont(self.name_inp, 530, 100, 11)
        self.name_inp.setPlaceholderText("ism kiriting")
        self.name_inp.setStyleSheet("QLineEdit  {background-color: yellow; border-radius: 5px; border: 2px solid blue; }")
        
        # ! === Oqish turi ===
        self.turi = QLabel("Turi:", self)
        self.UzFont(self.turi, 400, 150, 12)
        self.standart = QRadioButton("standart",self)
        self.UzFont(self.standart, 450, 150, 11)
        self.standart.setStyleSheet("QRadioButton  {background-color: yellow; border-radius: 3px; border: 2px solid blue; }")
        
        self.intensiv = QRadioButton("intensiv",self)
        self.UzFont(self.intensiv, 550, 150, 11)
        self.intensiv.setStyleSheet("QRadioButton  {background-color: yellow; border-radius: 3px; border: 2px solid blue; }")
        
        self.bootcamp = QRadioButton("bootcamp",self)
        self.UzFont(self.bootcamp, 650, 150, 11)
        self.bootcamp.setStyleSheet("QRadioButton  {background-color: yellow; border-radius: 3px; border: 2px solid blue; }")
        
        # ! ===  insert data ===
        self.claim = QPushButton("Claim", self)
        self.UzFont(self.claim, 800, 150,  12)
        self.claim.setStyleSheet(""" QPushButton {
                background-color: #4CAF50; 
                color: white;               
                border-radius: 10px;        
                border: 2px solid #4CAF50;  
                padding: 10px 20px;        
                font-size: 16px;}
            QPushButton:hover {background-color: #45a049; }
            QPushButton:pressed {background-color: #36733c;} """)
        self.claim.clicked.connect(self.Main)

    def Main(self):
        self.xato_topildi = False
        # ! === guruh nomi ===
        if not self.guruh_nomi_inp.text():
            self.nom_error.setText("Guruh nomini kiriting")
            self.nom_error.adjustSize()
            self.xato_topildi = True
        else:
            self.m_name = self.guruh_nomi_inp.text()
            self.nom_error.clear()
        # ! === talaba soni ===
        if self.talaba_soni_inp.text():
            try:
                int(self.talaba_soni_inp.text())
                self.t_soni = self.talaba_soni_inp.text()
                self.t_soni_error1.clear()
            except ValueError:
                self.t_soni_error1.setText("Talabalar sonini to'g'ri kiriting")
                self.t_soni_error1.adjustSize()
                self.xato_topildi = True
        else:
            self.t_soni_error1.setText("Talabalar sonini kiriting")
            self.t_soni_error1.adjustSize()
            self.xato_topildi = True
        # ! === oylik ===
        if self.oylik_inp.text():
            try:
                float(self.oylik_inp.text())
                self.salary = self.oylik_inp.text()
                self.oylik_error.clear()
            except ValueError:
                self.oylik_error.setText("Oylik to'lovni to'g'ri kiriting")
                self.oylik_error.adjustSize()
                self.xato_topildi = True
        else:
            self.oylik_error.setText("Oylik to'lovni kiriting")
            self.oylik_error.adjustSize()
            self.xato_topildi = True
        # ! === manzil ===
        if self.manzil_inp.text():
            self.adress = self.manzil_inp.text()
            self.manzil_error.clear()
        else:
            self.manzil_error.setText("Manzilni kiriting")
            self.manzil_error.adjustSize()
            self.xato_topildi = True
    
        if self.name_inp.text():
            self.t_name = self.name_inp.text()
            self.t_name_error.clear()
        else:
            self.t_name_error.setText("Ustozning ismini kiriting")
            self.t_name_error.adjustSize()
            self.xato_topildi = True
    
        # !Kurs turini tekshirish
        self.turi_text = ""
        if self.standart.isChecked():
            self.turi_text += self.standart.text()
            self.turi_error.clear()
        elif self.intensiv.isChecked():
            self.turi_text += self.intensiv.text()
            self.turi_error.clear()
        elif self.bootcamp.isChecked():
            self.turi_text += self.bootcamp.text()
            self.turi_error.clear()
        else:
            self.turi_error.setText("Turini tanlang")
            self.turi_error.adjustSize()
            self.xato_topildi = True
     
        if self.xato_topildi:
            return
        self.kursor.execute("""
    INSERT INTO malumotlar (nomi, talabalar_soni, oylik_narx, manzil, ustoz_ismi, turi)
    VALUES (%s, %s, %s, %s, %s, %s)
    """, (self.m_name, self.t_soni, self.salary, self.adress, self.t_name, self.turi_text))
        self.db.commit()  
        self.jadval.setVisible(True)
        self.kursor.execute("select *from malumotlar;")
        ls = self.kursor.fetchall()
        self.jadval.clear()
        self.jadval.setRowCount(len(ls))
        self.jadval.setColumnCount(7)
        self.jadval.setHorizontalHeaderLabels(["ID", "nomi", "talabalar soni", "oylik tolov", "manzil", "Ustozning ismi", "turi"])
    
        for i in range(len(ls)):
            self.jadval.setItem(i,0,QTableWidgetItem(str(ls[i][0])))
            self.jadval.setItem(i,1,QTableWidgetItem(str(ls[i][1])))
            self.jadval.setItem(i,2,QTableWidgetItem(str(ls[i][2])))
            self.jadval.setItem(i,3,QTableWidgetItem(str(ls[i][3])))
            self.jadval.setItem(i,4,QTableWidgetItem(str(ls[i][4])))
            self.jadval.setItem(i,5,QTableWidgetItem(str(ls[i][5])))
            self.jadval.setItem(i,6,QTableWidgetItem(str(ls[i][6])))
        
        self.name_inp.clear()
        self.oylik_inp.clear()
        self.manzil_inp.clear()
        self.guruh_nomi_inp.clear()
        self.talaba_soni_inp.clear()
    
    def Update(self):
        # ! === Update ustuni ===
        self.update_turi = QLabel("Update turi:", self)
        self.UzFont(self.update_turi, 50, 450, 12)
        self.updatetype = QComboBox(self)
        self.UzFont(self.updatetype, 180, 450, 12)
        self.updatetype.setStyleSheet("QComboBox  {background-color: yellow; border-radius: 5px; border: 2px solid blue; }")
        self.updatetype.addItems(["nomi", "talabalar_soni", "oylik_narx", "manzil", "ustoz_ismi", "turi"])
        
        # ! === new info ===
        self.update_value = QLabel("New info:", self)
        self.UzFont(self.update_value, 50, 500, 12)
        self.newinfo = QLineEdit(self)
        self.UzFont(self.newinfo, 180, 500, 12)
        self.newinfo.setPlaceholderText("yangi infoni kiriting")
        self.newinfo.setStyleSheet("QLineEdit  {background-color: yellow; border-radius: 5px; border: 2px solid blue; }")

        # ! === tanlanadigan ID ===
        self.chooseID = QLabel("Malumoti ozgaritiladigan ID:", self)
        self.UzFont(self.chooseID, 400, 450, 12)
        self.chooseID_inp = QLineEdit(self)
        self.UzFont(self.chooseID_inp, 630, 450, 12)
        self.chooseID_inp.setPlaceholderText("ID kiriting")
        self.chooseID_inp.setStyleSheet("QLineEdit  {background-color: yellow; border-radius: 5px; border: 2px solid blue; }")

        self.update_claim = QPushButton("Update", self)
        self.UzFont(self.update_claim, 800, 500, 12)
        self.update_claim.setStyleSheet(""" QPushButton {
                background-color: #4CAF50; 
                color: white;               
                border-radius: 10px;      
                border: 2px solid #4CAF50; 
                padding: 10px 20px;        
                font-size: 16px;}
            QPushButton:hover {background-color: #45a049;  }
            QPushButton:pressed {background-color: #36733c; } """)
        self.update_claim.clicked.connect(self.Update_New_Info)
    
    def Update_New_Info(self):
        self.kursor.execute(f"""UPDATE malumotlar SET `{self.updatetype.currentText()}` = %s WHERE id = %s""", 
                        (self.newinfo.text(), self.chooseID_inp.text()))
        self.db.commit()
        self.jadval.setVisible(True)
        self.kursor.execute("SELECT * FROM malumotlar;")
        ls = self.kursor.fetchall()
        self.jadval.setRowCount(len(ls))
        self.jadval.setColumnCount(7)
        self.jadval.setHorizontalHeaderLabels(["ID", "nomi", "talabalar soni", "oylik tolov", "manzil", "Ustozning ismi", "turi"])

        for i in range(len(ls)):
            self.jadval.setItem(i, 0, QTableWidgetItem(str(ls[i][0])))
            self.jadval.setItem(i, 1, QTableWidgetItem(str(ls[i][1])))
            self.jadval.setItem(i, 2, QTableWidgetItem(str(ls[i][2])))
            self.jadval.setItem(i, 3, QTableWidgetItem(str(ls[i][3])))
            self.jadval.setItem(i, 4, QTableWidgetItem(str(ls[i][4])))
            self.jadval.setItem(i, 5, QTableWidgetItem(str(ls[i][5])))
            self.jadval.setItem(i, 6, QTableWidgetItem(str(ls[i][6])))
        
        self.newinfo.clear()
        self.chooseID_inp.clear()
    
    def UzFont(self, obj, x, y , size):
        obj.setFont(QFont("Times", size))
        obj.move(x, y)
        
    def database(self):
        self.kursor.execute("create database if not exists najottalim;")
        self.kursor.execute("use najottalim")
        self.kursor.execute("create table if not exists malumotlar(id int auto_increment primary key, nomi text, talabalar_soni int, oylik_narx float, manzil text, ustoz_ismi text, turi text)")

dastur = Database()


app.exec_()