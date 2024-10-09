import  os  ; os.system("cls")

class  Odam:
    pass

ls  = list()
odam1  =  Odam() 
print(type(ls))
print(type(odam1))


class  Odam():
    ismi  = ""
    familya = ""
    yoshi = 0

    def  Tanishtir():
        print(Odam.ismi)
        print(Odam.familya)
        print(Odam.yoshi)

Odam.ismi = "Kimdir"
Odam.familya = "Nimadirov"
Odam.yoshi  = 123
print(Odam().ismi)
print(Odam().familya)
print(Odam().yoshi)
Odam.Tanishtir()




class  Odam():
    ismi  = ""
    familya = ""
    yoshi = 0

    def  Tanishtir(self):
        print(self.ismi)
        print(self.familya)
        print(self.yoshi)

odam1  = Odam()
odam1.ismi  =  "Abdulla"
odam1.familya  =  "Qodirov"
odam1.yoshi  =  12
odam1.Tanishtir()



class  Odam:
    def __init__(self,  ism : str, taxallus : str,  yosh :int ):
        self.nomi  =  ism
        self.familya  = taxallus
        self.yoshi  = yosh
        print("Men  INIT  Funksiyasiman \n\n\n")
        
    def  salomlash(self):
        print("Assalomu  Alaykum ")
    
    def  tanishtir(self):
        print("Mening Ismim  ==>  ",  self.nomi)
        print("Mening Familyam  ==>  ",  self.familya)
        print("Mening Yoshim  ==>  ",  self.yoshi,  "da")
        

ob  =  Odam("Farruxbek",  "Ruzmetov", 16)
ob1  =  Odam("Muhriddin",  "Sobirjonov", 17)
ob2  =  Odam("Mirafzal",  "Qurbonov", 19)
ob3  =  Odam("Muhammadrasul",  "Shixnazarov", 15)
ob4  =  Odam("Dildora",  "Sadikova", 15)
ob5  =  Odam("Shoxista",  "Tangberganova", 15)



# ob.__init__("salom", "asdfh", 1234)

ob.salomlash()
ob.tanishtir()
print()

ob1.salomlash()
ob1.tanishtir()
print()

ob2.salomlash()
ob2.tanishtir()
print()

ob3.salomlash()
ob3.tanishtir()
print()

ob4.salomlash()
ob4.tanishtir()
print()


ob5.salomlash()
ob5.tanishtir()
print()










