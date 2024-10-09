import  os
import  mysql.connector
os.system("cls")

mydb  =  mysql.connector.connect(
    host  =  "localhost",
    user  =  "root",
    password = "root1" )

kursor =  mydb.cursor()
# !   Databaza   yaratildi
kursor.execute("CREATE  DATABASE IF NOT  EXISTS  NAJOT;")
print("Data  baza yaratildi")
# !   Data  baza ichiga  kirildi  
kursor.execute("use  NAJOT;")
print("Data  bazani  ichiga  kirdi")

# # !   Table  yaratildi
kursor.execute("""CREATE   Table  IF NOT  EXISTS Guruh
                        (id  int,  ism  varchar(25),   yosh  int,  guruh Text );""")
print("Tebil  yaratildi.  ")
# !  Malumot  yozish
kursor.executemany("""INSERT  INTO  Guruh  VALUES (%s, %s, %s, %s)""",
                    [(1,  "Temur", 12, 'n1'), (2,  "Elyor", 22, 'xn3'), 
                     (3,  "Diyor", 18, 'n1'), (4,  "Sanjar", 30, 'n123')])
print("Ma'lumot  qo'shildi")
# # !  malumotlarni saqlash  
mydb.commit()
print("Saqlandi ")
kursor.execute("select  *from Guruh;")

for  i in  kursor.fetchall():
    print(i)