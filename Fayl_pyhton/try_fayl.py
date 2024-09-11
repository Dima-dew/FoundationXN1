import  os;  os.system("cls")
import sys

try  :
    pass
except :
    sys.exit("Fayl  Avval Yaratilgan.  Modni o'zgartiting ")


file  =  open("ni.txt", "w+")

file.write("Salom  Bolalar")
file.write("\nBu yangi  malumot")
file.close()