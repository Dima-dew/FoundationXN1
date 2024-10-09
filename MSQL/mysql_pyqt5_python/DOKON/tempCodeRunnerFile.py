  self.table_yaratish = QPushButton("Yaratish", self)
        self.table_yaratish.setFont(QFont("Times", 20))
        self.table_yaratish.setGeometry(30, 540, 440, 50)
        self.table_yaratish.setStyleSheet("""            
             QPushButton{ border-radius: 10px; 
            border : 2px solid red; }""")
        self.table_yaratish.clicked.connect(self.create_TABLE)