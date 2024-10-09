import  os
import  mysql.connector
os.system("cls")

mening_db  =  mysql.connector.connect(
    host  =  "localhost",
    user  =  "root",
    password = "root1" )

mening_kursorim =  mening_db.cursor()
# !   Databaza   yaratildi
mening_kursorim.execute("CREATE  DATABASE IF NOT  EXISTS  NAJOT;")
print("Data  baza yaratildi")
# !   Data  baza ichiga  kirildi  
mening_kursorim.execute("use  NAJOT;")

# !   Table  yaratildi
mening_kursorim.execute("CREATE  TABLE  IF NOT  EXISTS xn1(id  int,  soni  int);")
mening_kursorim.execute("CREATE   Table  IF NOT  EXISTS xn2(ism  varchar(25),  oy INT);")
print("Tebil  yaratildi.  ")

# ! malumot  qo'shish  
mening_kursorim.execute("INSERT  INTO  xn1  VALUES  (1, 6)")
mening_kursorim.execute("INSERT  INTO  xn1  VALUES  (2, 12)")
mening_kursorim.execute("INSERT  INTO  xn1  VALUES  (3, 18)")
mening_kursorim.execute("INSERT  INTO  xn1  VALUES  (4, 24)")
print("Malumot  qo'shildi")
# !  malumotlarni saqlash  
mening_db.commit()
mening_kursorim.execute("select  *from xn1;")

for  i in  mening_kursorim.fetchall():
    print(i)