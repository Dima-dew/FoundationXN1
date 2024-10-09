import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

app = QApplication(sys.argv)

oyna = QMainWindow()
oyna.setWindowTitle('Matplotlib yordamida rasmni ko\'rsatish')
oyna.setGeometry(100, 100, 400, 300)

# Tugma orqali rasmni ko'rsatish
tugma = QPushButton('Rasmni Ko‘rsatish', oyna)
tugma.setGeometry(150, 130, 100, 50)

# Matplotlib yordamida rasmni ochish va ko'rsatish
rasm = mpimg.imread('rasm.png')

tugma.clicked.connect(lambda: (plt.imshow(rasm), plt.axis('off'), plt.show()))

oyna.show()
sys.exit(app.exec_())
