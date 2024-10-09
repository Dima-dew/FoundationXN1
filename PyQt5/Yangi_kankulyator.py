from  PyQt5.QtWidgets  import  QApplication,  QWidget,  QPushButton
from  PyQt5.QtWidgets  import  QHBoxLayout,  QVBoxLayout,  QLineEdit
from  PyQt5  import  QtCore
import  sys
app  =  QApplication(sys.argv)
class  Button(QPushButton):
    models  = {
        "raqam": "grey",
        "operator": "orange",
        "symbol": "lightgrey"     }
    def __init__(self, raqam :str, mode =  "raqam"):
        super().__init__()
        # ! turini  olib olish  uchun  yangi  qo'shildi.
        self.mode = mode
        # =====================================
        self.setText(raqam)
        self.setFixedSize(80, 80)
        self.setStyleSheet(f""" 
        font-size: 25px  ;       
        border-radius: 40%;
        color: {"black"  if  mode  == "symbol"  else "white"};
        background-color:  {self.models[mode]};  """)
class  Input(QLineEdit):
    def  __init__(self):
        super().__init__()
        # !  yangi  qo'shilgani  
        self.setAlignment(QtCore.Qt.AlignRight)
        self.setStyleSheet(f""" 
        font-size: 80px ;
        border: none;
        color: white   """)
class  Yangi_Dastur(QWidget):
    def  __init__(self):
        super().__init__()
        self.setWindowTitle("Kalkulyator")
        self.setFixedSize(400, 600)
        # ! orqa  fondi  qoraytirish  
        self.setStyleSheet("background-color:  black")

        self.b1 = Button("1")
        self.b2 = Button("2")
        self.b3 = Button("3")
        self.b4 = Button("4")
        self.b5 = Button("5")
        self.b6 = Button("6")
        self.b7 = Button("7")
        self.b8 = Button("8")
        self.b9 = Button("9")

        
        self.AC  = Button("AC",  "symbol")
        # !    bu ham yangi  
        self.pilus_minus  = Button("C",  "symbol")
        # =============================================
        self.foiz_bolish = Button(" % ",  "symbol")
        self.oddiy_bolish  = Button("/",  "operator")
        self.kopaytiruv  = Button("x",  "operator")
        self.minus = Button("-",  "operator")        
        self.pilus  = Button("+",  "operator")

        self.nol = Button("0")
        self.nol.setFixedWidth(self.nol.frameGeometry().width() * 2 + 20)
        self.nuqta = Button(".")
        self.teng  = Button("=",  "operator")


        self.nolinchi  =  QHBoxLayout()
        self.nolinchi.addWidget(self.AC)
        self.nolinchi.addWidget(self.pilus_minus)
        self.nolinchi.addWidget(self.foiz_bolish)
        self.nolinchi.addWidget(self.oddiy_bolish)

        self.birinchi =  QHBoxLayout()
        self.birinchi.addWidget(self.b7)        
        self.birinchi.addWidget(self.b8)        
        self.birinchi.addWidget(self.b9) 
        self.birinchi.addWidget(self.kopaytiruv) 

        self.ikkinchi =  QHBoxLayout()
        self.ikkinchi.addWidget(self.b4)        
        self.ikkinchi.addWidget(self.b5)        
        self.ikkinchi.addWidget(self.b6) 
        self.ikkinchi.addWidget(self.minus) 

        self.uchunchi =  QHBoxLayout()
        self.uchunchi.addWidget(self.b1)        
        self.uchunchi.addWidget(self.b2)        
        self.uchunchi.addWidget(self.b3) 
        self.uchunchi.addWidget(self.pilus) 

        self.tortinchi =  QHBoxLayout()
        self.tortinchi.addWidget(self.nol)        
        self.tortinchi.addWidget(self.nuqta)        
        self.tortinchi.addWidget(self.teng) 
  
        self.yozuv  =  Input()
        
        self.raqam =  QVBoxLayout()
        self.raqam.addWidget(self.yozuv)
        self.raqam.addLayout(self.nolinchi)
        self.raqam.addLayout(self.birinchi)
        self.raqam.addLayout(self.ikkinchi)
        self.raqam.addLayout(self.uchunchi)
        self.raqam.addLayout(self.tortinchi)
        self.setLayout(self.raqam)

        # !  Bottonlar  bosilganda  
        self.nol.clicked.connect(lambda : self.bosildi(self.nol))
        self.b1.clicked.connect(lambda : self.bosildi(self.b1))
        self.b2.clicked.connect(lambda : self.bosildi(self.b2))
        self.b3.clicked.connect(lambda : self.bosildi(self.b3))
        self.b4.clicked.connect(lambda : self.bosildi(self.b4))
        self.b5.clicked.connect(lambda : self.bosildi(self.b5))
        self.b6.clicked.connect(lambda : self.bosildi(self.b6))
        self.b7.clicked.connect(lambda : self.bosildi(self.b7))
        self.b8.clicked.connect(lambda : self.bosildi(self.b8))
        self.b9.clicked.connect(lambda : self.bosildi(self.b9))

        #! Amallar
        self.AC.clicked.connect(lambda : self.bosildi(self.AC))
        self.minus.clicked.connect(lambda : self.bosildi(self.minus))
        self.pilus.clicked.connect(lambda : self.bosildi(self.pilus))
        self.oddiy_bolish.clicked.connect(lambda : self.bosildi(self.oddiy_bolish))
        self.kopaytiruv.clicked.connect(lambda : self.bosildi(self.kopaytiruv))
        self.nuqta.clicked.connect(lambda : self.bosildi(self.nuqta))
        self.pilus_minus.clicked.connect(lambda : self.bosildi(self.pilus_minus))
        self.foiz_bolish.clicked.connect(lambda : self.bosildi(self.foiz_bolish))
        self.teng.clicked.connect(lambda : self.bosildi(self.teng))
# ! Asosiy  amallar  tekshirish  qismi  
    def  bosildi(self, btn :Button):
        if self.yozuv.text() == '':
            self.yozuv.setText(self.yozuv.text()[1:])
        if btn.text() == '=':
            txt = self.yozuv.text()
            self.yozuv.setText(f"{eval(txt)}")
        elif btn.text() == 'C':
            exp = self.yozuv.text()
            self.yozuv.setText(exp[:-1])
        elif btn.text() == "AC":
            self.yozuv.clear()
        elif btn.mode == "raqam":
            self.yozuv.setText(self.yozuv.text() + btn.text())
        elif not self.yozuv.text()[-1].isdigit() and btn.mode == "operator":
            self.yozuv.setText(self.yozuv.text()[:-1:] + btn.text())
        elif btn.mode == "operator":
            self.yozuv.setText(self.yozuv.text() + btn.text())  
oyna  = Yangi_Dastur()
oyna.show()
app.exec_()