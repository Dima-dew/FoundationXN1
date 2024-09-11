import os  ; os.system("cls")

def  hisobla(  a:  int ,  b  :int ):

    try: 
        natija  = a  /  b
    except ZeroDivisionError:
        print("Nullga  bo'lib bo'lmaydi   ")
        
    except TypeError:
        print("Bu  String   " )
    
    else: 
        print(natija)

# hisobla(20, 0)







def  son_():
    try: 
        raqam = int(input("SON:  "))
    except  TypeError:
        print("Bu boshqa  tayp ")
    except  ValueError:
        print("Xato bor")
    else: 
        print("SON  ==>  ", raqam)
# son_()







def  index_list(ls, index):
    try:
        t  = ls[index]
    except :
        print("Bunday  Index yo'q")

    else :
        print(t)


l  = [ 12,34,6,54]
# print(l)

index_list(l,  3)





