import  os
import  math  as  m
os.system('cls')
'''
def  salom_Ber():
    print("Assalomu Alaykum")

def  hayrlash():
    print("Salomat  Bo'ling")

salom_Ber()
hayrlash()

def  qosh(a  , b):
    y  = a  +  b
    print(y)

def  sum(n: float , c :int):
    return   n  +  c


qosh ("salom",  "1234")
s  =   sum(123,3456.234)

print(s)

'''
'''
def Katta (a,b,c,d ):
    return  max(a, b, c, d)

a, b, c,d  =  map(int,  input().split())
k  =    Katta(a,b,c,d)
print(k)




def  Daraja(a,b,c):
    return """
    {}  darajasi  {},  
    {}  darajasi  {},   
    {}  darajasi  {}
    """.format(a, a **a, b,  b **b,c, c **c)


a, b, c  = map(int,  input("N:  ").split())
c  = Daraja(a, b,c)
print(c, type(c))


def  Maxsulot(dic: dict):
    narx  = list(dic.values())
    qimat = max(narx)
    for  i in  dic:
        if( dic[i] ==  qimat ):
            return  {i :  dic[i]}
        
d  = {}
n  =  int(input("N:  "))
for  i  in  range(n):
    k  =  input("Maxsulot  nomi:   ")
    v  =  int(input("Maxsulot  narxi:   "))
    d[k]  = v
m  =  Maxsulot(d)

print(m)


def  Tub_son(son):
    t  = 2
    # while( t * t  <=  son):
    for i  in range(2,  son):
        if  (son %  t  == 0):
            return False
        t  = t  +  1
    return  True
    

def  tub_son_Aniqla(ls):
    ch = False
    for  i in  ls:
        if  (Tub_son(i)  ==  True):
            ch  = True
            print(i ,  end= " :  ") 
    if   ch == False :
        print("List  ichida  Tub son  Yo'q")

ls  =   [123, 7  , 23,43, 34,54,6,56,4,76]
tub_son_Aniqla(ls)


'''



#!    Recursiv  funksiya


# def  Raqamlar(son :int):
#     for  i  in  range(1  ,  son  +  1):
#         print(i  ,  end=  "   ")
# Raqamlar(10)




# print()
# #!  To'g'i  
# def  Recursiv(n  : int):
#     if  n  == 0:
#         return  0
#     Recursiv(n  - 1)
#     print(n,  end=  "   ")

# Recursiv(10)

# print()

# #!  Teskari  
def  Recursiv1(n  : int):
    if  n  == 0:
        return  0
    print(n,  end=  "   ")
    Recursiv1(n  - 1)

Recursiv1(10)
    


def  faktorial_Def(n :  int):
    if  n  == 1:
        return  1
    else :
      return   n  * faktorial_Def(n -  1)
f  = faktorial_Def(5)
print(f)

s  =  m.factorial(5)
print(s)

x  = lambda  i  :  i  + 10
print(x(5))

q  = lambda  a, b:  a + b  * 2
print(q(1, 2))
kata  =   lambda a  ,b, c,d,e,f:  max(a,b,c,d,e,f)
print(kata(21,24,334,45,43, 23))
k  = lambda  a,  b,  c, d:  (a  +  b) *  (c  *  d)
print(k (1,2,3,4))



