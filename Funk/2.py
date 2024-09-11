import os
os.system("cls")
'''
j  =  lambda a  , b :  a +  b
print(j(12, 65))

x  =  lambda  a  :  a  ** 4
t  =  x(2)
print(t)

l  = [1,3,5,2,35,3,5,0,8,24,15]

print("List  sonlar  ==>  ", l)
print()
sort_list = sorted(l,  key =  lambda son:  son)
print("Sort list  son ==>  ", sort_list)

ls  =  [("Piyoz", 7000), ("Go'sht", 96000), ("Guruch", 21000), ("Sabzi", 5000),
        ("Pomidor", 11500), ("Yog'", 18000), ("Bodring", 12500)]

narx_Maxsulotlar =  sorted(ls,  key=lambda maxsulot: maxsulot[1],  reverse=True)
print(narx_Maxsulotlar)
print()
narx_Maxsulotlar1 =  sorted(ls,  key=lambda maxsulot: maxsulot)
print(narx_Maxsulotlar1)
'''

talaba  = ['Diyora', 'Dilbek',  'Maftuna', "Dildora", 
           "Madina",'Faruxbek', 'Mirafzal', 'Muhriddin']
ls  =  list(filter(lambda n:  (n[0]  ==  'M'), talaba))
ls  =  list(filter(lambda n:  (n[1]  ==  'a'), talaba))
print(ls)


ls =   [1,32,4,5,6,7,7,8,9,88,7,65,4]
juft =  filter(lambda i  : i  %  2  != 0, ls)
juft  = list(juft)
print(juft)


ls1  = ['aziza', 'non',  'madina', 'kiyik', 'salom', "ko'k"]
palindrom =  list(filter(lambda i  : (i ==  i[::-1] ), ls1))
print(palindrom)
                  


raqam  = [1,2,3,4,5,6]
y  = map(lambda  i :  i ** 5, raqam)
print(list(y))




