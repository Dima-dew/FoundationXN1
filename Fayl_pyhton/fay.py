import  os ;  os.system("cls")
import  sys  
'''
serya =  """Muhammadrasul  doskaga  qarang.
Faruxbek o'ynamang.
Muhriddin  to'g'ri  o'tiring.\n"""

file =  open("soz.txt", "w")
file.write(serya)


lis  = ["Kimdir", "Nimadir",  "Qayerdadir"]
file.writelines(lis)


for i in  lis:
    file.write(i)
    file.write(" ")

file.close()


#!  Fayldan o'qish 
f  =  open("soz.txt", "r")
matn  =  f.read()
print(matn, end="\n\n\n")


f.seek(0)
for  i  in f:
    for  j in  i:
        print(j, end="")



f.seek(0)
print()
text  = f.readline()
print(text)
f.seek(0)

print()
print()
ls  = f.readlines()
print(ls)

for  i in  ls:
    for  j  in  i:
        print(j, end=" ")

f.seek(0)
print()
k  = f.read()
print(k)
f.close()
'''

#! Faylga  Malumot qo'shish  

f =  open("soz.txt", "r")
if  (f.readable()):
    print("Fayndan Ma'lunmot o'qishingiz  mumkin\n")
else:
    sys.exit("Sizga  Fayldan malumot  o'qishga  ruxsat  yo'q")
res,  ls = [], [] ; 
data =  f.read()
for  i in data.split("\n"):
    ls.extend(i.split("."))
for  l in  ls:
    res.extend(l.split())
natija  = sorted(res, key=len)

# for  i  in  natija:
#     print(F" {i}  ==>  {len(i)}")
# print("MAX  ==>   ",  natija[-1])
# print("MIN  ==>   ",  natija[0])

d  =  dict()
for  i in  natija:
    d[i] = len(i)
print(d)

l1, l2 =  [], []
for  i in natija:
    l1.append(i)
    l2.append(len(i))

d2  = dict(zip(l1, l2))
print(d2)









f.close()




