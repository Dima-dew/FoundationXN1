import mysql.connector  

class  DatabazagaUlanish:
    def  __init__(self) :
        self.mysql_db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root1"
        )
        self.kursor =  self.mysql_db.cursor()
        print("Dataga  ulandi")

    def  yangi_Databaza(self):
        self.kursor.execute("CREATE  DATABASE IF  NOT  EXISTS  DIMA;")        
        print("Yangi  yaratildi.  ")

    def  databazagakirish(self):
        self.kursor.execute("USE  dima;")
        print("yangio  daatabazaga kirdi")

    def  Crate_Table(self):
        self.kursor.execute("CREATE  TABLE  if  Not  exists ZOR(ISM TEXT,   YOSH INT);")
        print("Yangi  table  yaratildi.  ")

    def  malumot_qoshish(self):
        sql = """ INSERT  INTO  ZOR   VALUES  ("DIYOR",  12), ("Elbek",  22), ("Alibek",  15);
        """
        self.kursor.execute(sql)
        self.mysql_db.commit()
        print("Malumot  yozidi")


db  = DatabazagaUlanish()
db.yangi_Databaza()
db.databazagakirish() 
db.Crate_Table()

db.malumot_qoshish()