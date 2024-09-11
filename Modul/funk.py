def  Sonlar(n :int ):
    for  i  in  range(1, n + 1):
        print(i, end=' ')

def  Summ(ls):
    ls  = list(ls)
    sum =  0
    for  i in  range(len(ls)):
        sum  +=  ls[i]
    return  sum

def  Faktorial(son):
    if  son  == 1:
        return  1
    return son *  Faktorial(son - 1)

def  Yig(n:int,  m :float):
    return  n  +  m