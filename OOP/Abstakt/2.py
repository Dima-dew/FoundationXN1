import  os;  os.system("cls")
from  abc  import ABC,  abstractmethod

class  Maktab(ABC):
    @abstractmethod
    def  __init__(self, nomi,  manzil, bitiruvchilar_soni:int):
        self.nomi  =  nomi
        self.manzil =   manzil
        self.bitiruv_soni =  bitiruvchilar_soni
    @abstractmethod
    def  malumot(self):
        pass

    @abstractmethod
    def  imitixon(self):
        pass
    @abstractmethod
    def  davomat(self):
        pass
    @abstractmethod
    def  ballar(self):
        pass
    @abstractmethod
    def  forma(self):
        pass

    def  bilmadik(self):
        pass



class  Maktab_34(Maktab):
    def __init__(self, nomi, manzil, bitiruvchilar_soni):
        super().__init__(nomi, manzil, bitiruvchilar_soni)
    
    def  malumot(self):
        return super().malumot()
    def  ballar(self):
        return super().ballar()
    def forma(self):
        return super().forma()
    def  davomat(self):
        return super().davomat()
    def imitixon(self):
        return super().imitixon()
    
    def soni(self):
        print("Nomi   ", self.nomi)
        print("Adresi    ", self.manzil)
        print("B  Soni   ", self.bitiruv_soni)
        

m_34  = Maktab_34("34  - maktab",  "Yunusabot",  60)
m_34.soni()