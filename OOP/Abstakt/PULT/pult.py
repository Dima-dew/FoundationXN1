import  time
import  random
import  os;  os.system("cls")


class  Pult:
    def  __init__(self,tv_holati = "Off",tv_ovozi = 0,kanal_listi =["BBC", "ST", "UZB", "Zo'r"], kanal = "BBC" ) :
        self.tv_holati  =  tv_holati
        self.tv_ovozi  =  tv_ovozi
        self.kanal  =  kanal
        self.kanal_listi  =  kanal_listi
    def  __str__(self) -> str:
        return f"""
TV Holati  {self.tv_holati}
Ovozi  {self.tv_ovozi}
Hozirgi  Kanal  {self.kanal}
Kanallar {self.kanal_listi}"""
    

    def  ovoz_ozgartirish(self):
        b  = True
        while b :
            belgi =  input("  +  ||  -  ")
            if  belgi ==  '+':
                if (self.tv_ovozi  <  5):
                    self.tv_ovozi += 1
                    print(f"Ovoz    {self.tv_ovozi}")
                    continue
                else :
                    b  =  False
            elif  (belgi  ==  '-'):
                if  (self.tv_ovozi  <= 5):
                    self.tv_ovozi  -= 1
                    print(f"Ovoz    {self.tv_ovozi}")
                    continue
            else:
                print("Ovoz  Yangilash  Tugatildi")
                break
    
    def  random_kanal(self):
        almashtirilgan_kanal = random.randint(0, len(self.kanal_listi) -1)
        self.kanal  =  self.kanal_listi[almashtirilgan_kanal]
        print("O'zgartirildi ")

    def  yondir_ochir(self):
        if  (self.tv_holati  == "Off"):
            time.sleep(1)
            time.sleep(2)
            print("\n\t\tYondirilmoqda  ..........")
            time.sleep(3)
            print("  TV Yondi  ")
            self.tv_holati  =  "On"
        else :
            print("O'chirildi  ")
            self.tv_holati  =  "Off"
