import  mysql.connector
import  os;  os.system("cls")

class  Data_Base:
    def  __init__(self) :
        self.db =  mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root1"
        )
        self.kursor  =  self.db.cursor()
        print("Malumotlar bazasiga ulandi")
    def  Yangi_database(self):
        self.kursor.execute("CREATE  DATABASE  IF  NOT  EXISTS  dima;")
        print("Yangi  data  baza  yaratildi")
        # !===============================
    def  database_kirish(self):
        self.kursor.execute("USE  dima;")
        print("Data bazaga kirildi")
        # !===============================
    def  Yangi_Table(self):
        self.kursor.execute("""CREATE  TABLE  IF  NOT  EXISTS  nima
                            (id  int  auto_increment primary key,  ism  TEXT, boy FLOAT);""")
        print("Yangi  Table  yaratildi")
        # !===============================


    def  database_malumot_K(self):
        self.kursor.execute(""" INSERT  INTO  NIMA  (ISM,BOY ) VALUES 
                            ("KIMDIR",  165.6),("SANJAR", 160.9),("FARUX", 156.7);""")
        self.db.commit()
        print("Malumotlar  qo'shildi.  ")
        # !===============================

    
    def  database_Malumot_ochirish(self):
        self.kursor.execute("DELETE  FROM  nima  ID ;")
        self.db.commit()
        print("Malumot  O'chirildi")
        # !===============================

    def  database_delete(self):
        self.kursor.execute("DROP  DATABASE DIMA;")
        self.db.commit()
        print("Database  o'chirildi")

        # !===============================

    def  TABLE_delete(self):
        self.kursor.execute("DROP  TABLE NIMA;")
        self.db.commit()
        print("Table  o'chirildi")
    
    def  databese_malumot_Chiqarish(self,  table_nomi =  "nima"):
        self.kursor.execute(f"select  *from  {table_nomi};")
        natija  =  self.kursor.fetchall()
        print(natija)
        for  i  in  natija:
            print("Id  =  " ,  i[0])
            print("ism  =  " ,  i[1])
            print("boy  =  " ,  i[2])


d  = Data_Base()
d.Yangi_database()
d.database_kirish()
d.Yangi_Table()
d.database_malumot_K()

nomi  = input("Table  Nomi  ")
d.databese_malumot_Chiqarish(nomi)



print("\nDATABASE =>  1 \nTABLE  => 2\nMalumotlar n =>  3\nBoshqa  X")
n = int(input())
if  (n  == 1):
    d.database_delete()
elif (n  == 2):
    d.TABLE_delete()
elif  (n  == 3):
    d.database_Malumot_ochirish()
else :
    print("😂😂😂😂😂😂👍👌🙌  ")