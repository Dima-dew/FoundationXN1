

from PyQt5.QtWidgets import QWidget,QPushButton,QApplication
from PyQt5.QtWidgets import QLabel,QLineEdit,QCheckBox
from PyQt5.QtGui import QFont
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.start()
    def start(self):
        # 1 vqat haqida
         self.yozuv=QLabel("Bizning restaranimizga hush kelibsiz ",self)
         self.yozuv.move(700,50)
         self.yozuv.setFont(QFont("Times",20))
         self.yozuv=QLabel("1-Tamolarga nima buyurasiz ",self)
         self.yozuv.move(50,100)
         self.yozuv.setFont(QFont("Times",20))
         self.a=QCheckBox("Shashlik  14000",self)
         self.a.move(100, 160)
         self.a.setFont(QFont("Times",20))
         self.b=QCheckBox("Osh 20000",self)
         self.b.move(100, 220)
         self.b.setFont(QFont("Times",20))
         self.s=QCheckBox("Manti 15000",self)
         self.s.move(100, 280)
         self.s.setFont(QFont("Times",20))
         self.c=QCheckBox("Pomidor salat 5000",self)
         self.c.move(100, 340)
         self.c.setFont(QFont("Times",20))
         btn=QPushButton("1 - Buyurtma ",self)
         btn.setGeometry( 120, 420, 100, 50)
         btn.setFont(QFont("Times",20))
         btn.adjustSize()
         self.yozuv=QLabel(self)
         self.yozuv.move(100,500)
         self.yozuv.setFont(QFont("Times",20))
         self.papka1=QLabel(self)
         self.papka1.move(100, 550)
         self.papka1.setFont(QFont("Times",20))
         self.papka1.adjustSize()
         btn.clicked.connect(self.bajar)
         
         
         
         
         # 2 ovqat haqida
 #==============================================================================#        
         self.yozuv=QLabel("2-Tamolarga nima buyurasiz ",self)
         self.yozuv.move(500,100)
         self.yozuv.setFont(QFont("Times",20))
         self.r=QCheckBox("Kabob 35000",self)
         self.r.move(500, 160)
         self.r.setFont(QFont("Times",20))
         self.w=QCheckBox("No'xot sho'rva  27000",self)
         self.w.move(500, 220)
         self.w.setFont(QFont("Times",20))
         self.q=QCheckBox("Qaynatma sho'rva  29000",self)
         self.q.move(500, 280)
         self.q.setFont(QFont("Times",20))
         self.e=QCheckBox("Ayronosh 30000",self)
         self.e.move(500, 340)
         self.e.setFont(QFont("Times",20))
         btn1=QPushButton("2 - Buyurtma ",self)
         btn1.setGeometry( 540, 420, 100, 50)
         btn1.setFont(QFont("Times",20))
         btn1.adjustSize()
         self.yozuv=QLabel(self)
         self.yozuv.move(500,500)
         self.yozuv.setFont(QFont("Times",20))
         self.papka2=QLabel(self)
         self.papka2.move(500, 550)
         self.papka2.setFont(QFont("Times",20))
         self.papka2.adjustSize()
         btn1.clicked.connect(self.bajar1)
         
         # ivhimliklar haqida
# ================================================================================#
         self.yozuv=QLabel("Ichimliklardan  nima buyurasiz ",self)
         self.yozuv.move(950,100)
         self.yozuv.setFont(QFont("Times",20))
         self.ich1=QCheckBox("Pepsi 14000",self)
         self.ich1.move(970, 160)
         self.ich1.setFont(QFont("Times",20))
         self.ich2=QCheckBox("Yaxna choy 7000",self)
         self.ich2.move(970, 220)
         self.ich2.setFont(QFont("Times",20))
         self.ich3=QCheckBox("Fanta 13000",self)
         self.ich3.move(970, 280)
         self.ich3.setFont(QFont("Times",20))
         self.ich4=QCheckBox("Kola  10000",self)
         self.ich4.move(970, 340)
         self.ich4.setFont(QFont("Times",20))
         btn2=QPushButton(" 3 - Buyurtma ",self)
         btn2.setGeometry( 1000, 420, 100, 50)
         btn2.setFont(QFont("Times",20))
         btn2.adjustSize()
         self.yozuv=QLabel(self)
         self.yozuv.move(970,500)
         self.yozuv.setFont(QFont("Times",20))
         self.papka3=QLabel(self)
         self.papka3.move(970, 550)
         self.papka3.setFont(QFont("Times",20))
         self.papka3.adjustSize()
         btn2.clicked.connect(self.bajar2)
         #shirinliklar
#============================================================================#
         self.yozuv=QLabel("Desertga  nima buyurasiz ",self)
         self.yozuv.move(1430,100)
         self.yozuv.setFont(QFont("Times",20))
         self.sh1=QCheckBox("Qulupnayli to'rt 20000",self)
         self.sh1.move(1450, 160)
         self.sh1.setFont(QFont("Times",20))
         self.sh2=QCheckBox("Olchali to'rt 17000",self)
         self.sh2.move(1450, 220)
         self.sh2.setFont(QFont("Times",20))
         self.sh3=QCheckBox("Malinali to'rt 15000",self)
         self.sh3.move(1450, 280)
         self.sh3.setFont(QFont("Times",20))
         self.sh4=QCheckBox("Jizzax muaqaymog'i  16000",self)
         self.sh4.move(1450, 340)
         self.sh4.setFont(QFont("Times",20))
         btn3=QPushButton(" 4 - Buyurtma ",self)
         btn3.setGeometry( 1530, 420, 100, 50)
         btn3.setFont(QFont("Times",20))
         btn3.adjustSize()
         self.yozuv=QLabel(self)
         self.yozuv.move(1450,500)
         self.yozuv.setFont(QFont("Times",20))
         self.papka4=QLabel(self)
         self.papka4.move(1450, 550)
         self.papka4.setFont(QFont("Times",20))
         self.papka4.adjustSize()
         btn3.clicked.connect(self.bajar3)
         chek=QPushButton("Umumiy hisob ",self)
         chek.setGeometry(50, 900, 10, 30)
         chek.setFont(QFont("Times",20))
         chek.adjustSize()
         self.yigindi=QLabel(self)
         self.yigindi.move(800,900)
         self.yigindi.setFont(QFont("Times",20))
         self.yigindi.setText("Hisob 0000000")
         self.yigindi.adjustSize()
         chek.clicked.connect(self.Umumin_hisob)
         
         
         
         
         #FUNKSIYALAR
#========================================================================================#       
  
    def bajar(self):
        self.yig=0
        self.yu=0
        if self.a.isChecked() or self.b.isChecked() or self.s.isChecked() or self.c.isChecked():
            self.papka1.setText("Siz 1- buyutmangizda \n")
            self.papka1.adjustSize()
            if self.a.isChecked():
                self.papka1.setText(self.papka1.text()+self.a.text()+"\n")
                self.yig+=int(self.a.text().split()[-1])
            if self.b.isChecked():
                self.papka1.setText(self.papka1.text()+self.b.text()+"\n")
                self.yig+=int(self.b.text().split()[-1])
            if self.s.isChecked():
                self.papka1.setText(self.papka1.text()+self.s.text()+"\n")
                self.yig+=int(self.c.text().split()[-1])
            if self.c.isChecked():
                self.papka1.setText(self.papka1.text()+self.c.text()+"\n")
                self.yig+=int(self.c.text().split()[-1])
                self.yu=self.yig
        else:
            self.papka1.setText("Buyurta qilmadingiz.")
        self.papka1.setText(self.papka1.text()+"\nHisob "+str(self.yig))
        self.papka1.adjustSize()
        
#===========================================================================================#        
        
    def bajar1(self):
        self.yig1=0
        self.jk=0
        if self.r.isChecked() or self.w.isChecked() or self.q.isChecked() or self.e.isChecked():
            self.papka2.setText("Siz 2- buyutmangizda \n")
            self.papka2.adjustSize()
            if self.r.isChecked():
                self.papka2.setText(self.papka2.text()+self.r.text()+"\n")
                self.yig1+=int(self.r.text().split()[-1])
            if self.w.isChecked():
                self.papka2.setText(self.papka2.text()+self.w.text()+"\n")
                self.yig1+=int(self.w.text().split()[-1])
            if self.q.isChecked():
                self.papka2.setText(self.papka2.text()+self.q.text()+"\n")
                self.yig1+=int(self.q.text().split()[-1])
            if self.e.isChecked():
                self.papka2.setText(self.papka2.text()+self.e.text()+"\n")
                self.yig1+=int(self.e.text().split()[-1])
                self.jk=self.yig1
        else:
            self.papka2.setText("Buyurta qilmadingiz")
        self.papka2.setText(self.papka2.text()+"\nHisob "+str(self.yig1))
        self.papka2.adjustSize()
        
#==========================================================================================#       
        
    def bajar2(self):
        self.yig2=0
        self.kj=0
        if self.ich1.isChecked() or self.ich2.isChecked() or self.ich3.isChecked() or self.ich4.isChecked():
            self.papka3.setText("Siz 3- buyutmangizda \n")
            self.papka3.adjustSize()
            if self.ich1.isChecked():
                self.papka3.setText(self.papka3.text()+self.ich1.text()+"\n")
                self.yig2+=int(self.ich1.text().split()[-1])
            if self.ich2.isChecked():
                self.papka3.setText(self.papka3.text()+self.ich2.text()+"\n")
                self.yig2+=int(self.ich2.text().split()[-1])
            if self.ich3.isChecked():
                self.papka3.setText(self.papka3.text()+self.ich3.text()+"\n")
                self.yig2+=int(self.ich3.text().split()[-1])
            if self.ich4.isChecked():
                self.papka3.setText(self.papka3.text()+self.ich4.text()+"\n")
                self.yig2+=int(self.ich4.text().split()[-1])
                self.kj=self.yig2
        else:
            self.papka3.setText("Buyurta qilmadingiz.")
        self.papka3.setText(self.papka3.text()+"\nHisob "+str(self.yig2))
        self.papka3.adjustSize()       
        
#====================================================================================================#      
  
    def bajar3(self):
        self.yig3=0
        self.k=0
        if self.sh1.isChecked() or self.sh2.isChecked() or self.sh3.isChecked() or self.sh4.isChecked():
            self.papka4.setText("Siz 4- buyutmangizda \n")
            self.papka4.adjustSize()
            if self.sh1.isChecked():
                self.papka4.setText(self.papka4.text()+self.sh1.text()+"\n")
                self.yig3+=int(self.sh1.text().split()[-1])
            if self.sh2.isChecked():
                self.papka4.setText(self.papka4.text()+self.sh2.text()+"\n")
                self.yig3+=int(self.sh2.text().split()[-1])
            if self.sh3.isChecked():
                self.papka4.setText(self.papka4.text()+self.sh3.text()+"\n")
                self.yig3+=int(self.sh3.text().split()[-1])
            if self.sh4.isChecked():
                self.papka4.setText(self.papka4.text()+self.sh4.text()+"\n")
                self.yig3+=int(self.sh4.text().split()[-1])
                self.k=self.yig3
        else:
            self.papka4.setText("Buyurta qilmadingiz")
        self.papka4.setText(self.papka4.text()+"\nHisob "+str(self.yig3))
        self.papka4.adjustSize()        
#==================================================================================#      
    def Umumin_hisob(self):
        self.umumiy=0
        self.umumiy=self.yig+self.yig1+self.yig2+self.yig3 
        self.yigindi.setText("Umumiy hisob "+str(self.umumiy))
        self.yigindi.adjustSize()
        
        
        
app=QApplication(sys.argv)
oyna=Window()
oyna.setGeometry(400, 400, 1000, 1000)
oyna.show()
sys.exit(app.exec_())