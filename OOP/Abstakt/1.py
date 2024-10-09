ls  =  []

class  INT():
    def  __init__(self):
        ls.append(int (input("Butun  son:    ")))

class  FLOAT(INT):
    def  __init__(self):
        n  =  int(input("1  int \t  2  Float\n"))
        if  n  == 1:
            super().__init__()
        else :
            ls.append(float(input("Haqiqiy  son:    ")))

class  BOOL(FLOAT):
    def  __init__(self):
        n =  int(input("  1  int yoki float\t  2  bool"))
        if  n  == 1:
            super().__init__()
        else :
            ls.append(bool(input("Bool  qiymat:   ")))

class  STR(BOOL):
    def  __init__(self):
        n =  int(input("  1  int yoki float yoki bool \t  2  str"))
        if  n  ==  1:
            super().__init__()
        else:
            ls.append(input("STR:   "))

for  i in  range(int(input("N:  "))):
   STR()

print(ls)
