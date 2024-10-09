import  os; os.system("cls")
'''
class  Vaqt:
    def  __init__(self,  soat,  minut,  sekund):
        self.soat  =  soat
        self.minut = minut
        self.sekund =  sekund
    def  time(self):
        print(f"Soat  {self.soat:02}  Minut  {self.minut:02}  Sekund   {self.sekund:02} ")

class  Soat():
    def  info(self,  st):
        st.soat += 5
        if  (st.soat  >  24):
            st.soat -=24
        st.time()

class  Minut ():
    def info(self,  min):
        min.minut +=  5
        if  (min.minut  > 60):
            min.minut  -= 60
            min.soat  += 1
            if  (min.soat  >  24):
                min.soat -=24
        min.time()

class  Sekund():
    def  info (self , sekunddd):
        sekunddd.sekund  += 5
        if  (sekunddd.sekund    >  60):
            sekunddd.sekund  -=  60
            sekunddd.minut += 1
            if  (sekunddd.minut  > 60):
                sekunddd.minut  -= 60
                sekunddd.soat  += 1
                if  (sekunddd.soat  >  24):
                    sekunddd.soat -=24
        sekunddd.time()

vaqt =  Vaqt(15 , 55,  57)
s  =  Soat()
s.info(vaqt)
m =  Minut()
m.info(vaqt)
sekundd  =  Sekund()
sekundd.info(vaqt)

'''
'''
print(3  *  3.234)
print("salom"  +  "Bolalar", 123 + 345)
print(124 +  2345,  1234.234 +  344.23)
print("salom  "  *  2,  3  *  4)
print("salom", 2345)

print(len([1,3,4,5,65,6,76,5,3,]), len("salom bolalar"))



class  Hayvon:
    def  ovoz(self):
        print("Nomalum Jonzot")

class  Kuchuk(Hayvon):
    def ovoz(self):
        print("WOW WOW")

class  Mushuk (Hayvon):
    def  ovoz(self):
        print("MYAUV")

class  Sigir(Hayvon):
    def  ovoz(self):
        print("MUUUUW")


h  = Hayvon()
h.ovoz()
m  = Mushuk()
m.ovoz()
k = Kuchuk()
k.ovoz()
s = Sigir()
s.ovoz()



class  Moshina():
    def __init__(self,  model,  rang):
        self.model   = model
        self.rangi  =  rang
    def  otOl(self):
        print(f"{self.model}  OT  OLDI .............")
    
    def  malumotlar(self):
        print(f"Modeli  =>  {self.model}")
        print(f"Rangi   =>  {self.rangi}")

# m  = Moshina("Damas",  "oq")
# m.otOl()
# m.malumotlar()

class  Tesla(Moshina):
    def  __init__(self, model, rang,  tezlik  :int):
        super().__init__(model, rang)
        self.tezlik  =  tezlik
    def  malumotlar(self):
        super().malumotlar()
        print(f"Tezligi  =>   {self.tezlik}")

    def  otOl(self):
        return super().otOl()

t  = Tesla("Tesla", "Qora",  150)
t.otOl()
t.malumotlar()

'''


class  Humo :
    def  __init__(self,  nomi  ,  kodi):
        self.__nomi =  nomi
        self.__kod  = kodi

    def  get_kod(self):
        return  self.__kod
    
    def  get_nomi(self):
        return  self.__nomi
    

    def  set_kod(self,  yangi_kod):
        self.__kod  = yangi_kod

    def  set_nomi(self,  yangi_nom):
        self.__nomi =  yangi_nom

    def  __malumot(self):
        print(f"Nomi  ==>  {self.__nomi}")
        print(f"Kodi  ==>  {self.__kod}")
    
    def get_malumot(self):
        return  self.__malumot()

h  =  Humo("Humo",  '1234')
print()
h.set_kod(123456789)
h.set_nomi("Xalq  Banki")
print(h.get_kod())
print(h.get_nomi())
h.get_malumot()


nomer[:2]  + "** "  +  ("*"  *  4,  ' ')  *  2   + self.nomer[-4:]










        
