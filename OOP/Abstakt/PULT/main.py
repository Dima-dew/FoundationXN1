from  pult  import  Pult

print("""---------  Menu  Pult ----------
1.  Yoqish (on/off)
2.  Kanallar
3.  Kanal  soni
4.  Ovoz  O'zgartirish
5.  Random kanal
0.  Tugatish 
""")

p =  Pult()

while True:
    amal  =  int(input("Amal:  "))
    if amal  == 0:
        print("Salomat  Bo'ling:  ")
        break
    elif amal  == 1:
        p.yondir_ochir()
    elif amal  == 2:
        print(p)
    elif amal  == 3:
        print(len(p.kanal_listi), "TV Kanal  Bor")
    elif amal  == 4:
        p. ovoz_ozgartirish()
    elif amal  == 5:
        p.random_kanal()