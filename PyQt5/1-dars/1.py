# from  PyQt5.QtWidgets import    QApplication ,  QWidget,  QLabel
# from  PyQt5.QtWidgets import     QLineEdit,  QTextEdit , QPushButton
# from  PyQt5.QtGui import QFont, QIcon 
# import  sys

# app  = QApplication(sys.argv)
# oyna  =  QWidget()
# oyna.setWindowTitle("MALUMOT")
# oyna.setFixedSize(450,  750)

# matn  =  QLabel("Nomalum", oyna)
# matn.setFont(QFont("Times", 25))
# matn.move(50,  125)
# # !  QLineEdit
# line  =  QLineEdit(oyna)
# line.setFont(QFont("Times",  15))
# line.setGeometry(50,  180,  300, 50)
# # !QTextEdit
# # text  =  QTextEdit(oyna)
# # text.setFont(QFont("Times",  15))
# # text.setGeometry(50,  190, 300, 150)

# # !  OK QPushButton
# ok   =  QPushButton("OK",  oyna)
# ok.setFont(QFont("Times", 15))
# ok.setGeometry(50,  270,  300, 50)

# def  almashtir():
#     a  = line.text()
#     matn.setText(a)
#     matn.adjustSize()
#     line.clear()
# ok.clicked.connect(almashtir)

# oyna.show()
# app.exec_()




son  =  eval("1 + 3 + 4 + 5")
print(son)