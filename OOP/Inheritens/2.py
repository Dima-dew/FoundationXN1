import  os;  os.system('cls')
'''
class  Hayvon():
    rangi  = ""
    turi  =""
    ogirligi  = "" 
    def  malumot(self):
        print("Hayvon  Rangi   ==>  ", self.rangi)
        print("Hayvon  Turi   ==>  ", self.turi)
        print("Hayvon  Og'irligi    ==>  ", self.ogirligi)


Hayvon.rangi  = "Qora"
Hayvon.turi  = "O'txor"
Hayvon.ogirligi  = "240"
h = Hayvon()
h.malumot()
# !==============================================================

class Hayvon():
    def  __init__(s, turi:  str, rangi :  str):
        s.taypi  =  turi
        s.rangi  = rangi
    def  malumotlar(self):
        print(f"Turi ==>   {self.taypi}\nRangi ==>  {self.rangi}")
    
h  = Hayvon("Go'sht xo'r ", "Kulrang")
h.malumotlar()


class  Talaba():
    def __init__(self,  nomi  : str,  familya : str,
      yoshi :int,  kursi :int):
        self.ism  = nomi
        self.familya  = familya
        self.yosh  = yoshi
        self.kurs  = kursi
    
    def Salom(self):
        print(f"Assalomu  Alaykum ")
    
    def  Tanish(self):
        print(f"""    Mening  Ismim  {self.ism}
    Familyam    {self.familya}
    Yoshim  {self.yosh}
    TATU  da   {self.kurs}  kurs  talabasiman""")
    
    def  Malumotlar(self, k: float):
        print(f"""\n\n    Mening  Ismim  {self.ism}
    Familyam    {self.familya}
    Yoshim  {self.yosh}
    TATU  da   {self.kurs}  kurs  talabasiman
    Kantraktim   {k}""")
        
talaba1 =  Talaba("Abdulla",  "Abdullayev", 23,  4)
talaba1.Salom()
talaba1.Tanish()
talaba1.Malumotlar(12000000.00)

    



class  Moshina():
    def __init__(self,  rangi :str,  Ot_kuchi: int,  narx:  float):
        self.rangi  =  rangi
        self.kuchlanishi =  Ot_kuchi
        self.narx =  narx
    
    def  malumot(self):
        print('Moshina   Rangi    {}Moshina  Kuchlanishi  {}Moshina  Narxi   {:.2f}'.format(self.rangi,  self.kuchlanishi,  self.narx))
        

class  Tesla(Moshina):
    def __init__(self, rangi: str, Ot_kuchi: int, narx: float, nomi: str):
        super().__init__(rangi, Ot_kuchi, narx) 
        self.nomi  =  nomi

    def  malumot(self):
       print("Moshina  Nomi   ",  self.nomi)
       super().malumot()
        

# m  = Moshina("qizil",  123,  1234567.234)
# m.malumot()

t  =  Tesla("Qora", 450,  1234567.7654,  "Testla")
t.malumot()






class  Nomalum():
    def  __init__(self, ismi : str):
        self.ismi =  ismi

class  Goshxor(Nomalum):
    def  goshtxor(self):
        print(f"{self.ismi} Go'sh yeydi quruqlikda yuradi")

class Suzuvchi(Goshxor):
    def  suzuvchi(self):
        print(f"{self.ismi} Suvda suzadi Gosh yeydi")


s  =  Suzuvchi("Timsox")
s.goshtxor()
s.suzuvchi()

n  = Goshxor("Nomalum")
n.goshtxor()





class  Ota():
    def  __init__(self,  familya) :
        self.familya = familya
    def  ota_malumot(self):
        print("Familya  ", self.familya)
    

class  Ona():
    def  __init__(self, ism):
        self.ism  =  ism
    def  ona_malumot(self):
        print("Ism  ", self.ism)


class  Bola(Ota, Ona):
    def  __init__(self, ism,  familya,  yoshi):
        Ota.__init__(self, familya)  
        Ona.__init__( self, ism)
        self.yosh  = yoshi
    
    def  malumot(self):
        super().ona_malumot()
        super().ota_malumot()
        print("Yosh  ",  self.yosh)

b   =  Bola("Jasur",  "Jabborov", 23)
b.malumot()

       

'''


class  Hodim():
    def  __init__(self, ism, familya ,  staj, yonalish, oyligi , yoshi,  korxona_soni):
        self.ismi  = ism
        self.familya = familya
        self.yonalish  = yonalish
        self.staj = staj
        self.oylik = oyligi
        self.yosh = yoshi
        self.korxona_soni = korxona_soni

    def  malumot(self):
        print(f"""Ismi  ==>  {self.ismi}
Familya  ==>  {self.familya}
Yoshi  ==>   {self.yosh}
Yonalish  ==>  {self.yonalish}
Staj  ==> {self.staj}
Korxona  Soni ==>  {self.korxona_soni}
Oylik ==>   {self.oylik}\n\n
""")


n  =   int  (input("N:  "))
xodim_SOni = []
for  i  in  range(n):
    print(f" {i  + 1} -  Xodim Malumotini  Kiriting ")
    ismI  =  input("Ism  Kiriting:   ")
    familyaI  =  input("Familyani  Kiriting:  ")
    yonalishI  =  input("Yonalishni  ")
    stjI  =  int(input("Staj  "))
    oylikI  =  float(input("OYLIK  "))
    yoshI  =  int (input("Yosh  "))
    ish_soniI   =  int(input("Nechta  Korxonada  "))
    hodim  =  Hodim(ismI,  familyaI , stjI , yonalishI,  oylikI, yoshI,  ish_soniI)
    xodim_SOni.append(hodim)

os.system("cls")
ls  = []
j  = 0
for  i in xodim_SOni:
    ls.append(xodim_SOni[j].yosh)
    j +=1

k  = max  (ls)
t  = 0
for  j  in xodim_SOni:
    if  (k  ==  j.yosh):
        continue
    else:
        j.malumot()
    














